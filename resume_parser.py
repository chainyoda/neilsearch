"""Resume parsing and profile extraction."""
import re
from pathlib import Path
from typing import Dict, List, Set
import PyPDF2
import pdfplumber
import docx


class ResumeParser:
    """Parse resumes and extract structured information."""

    # Common AI/ML skills to look for
    TECH_SKILLS = {
        # Programming languages
        "python", "r", "java", "c++", "julia", "scala", "javascript", "typescript",

        # ML Frameworks
        "pytorch", "tensorflow", "keras", "jax", "scikit-learn", "sklearn", "xgboost",
        "lightgbm", "catboost", "hugging face", "transformers", "langchain",

        # Deep Learning
        "deep learning", "neural networks", "cnn", "rnn", "lstm", "gru", "transformer",
        "attention mechanisms", "bert", "gpt", "llm", "large language models",

        # ML Techniques
        "machine learning", "supervised learning", "unsupervised learning",
        "reinforcement learning", "computer vision", "nlp", "natural language processing",
        "time series", "forecasting", "recommendation systems",

        # Tools & Platforms
        "aws", "gcp", "google cloud", "azure", "docker", "kubernetes", "k8s",
        "mlflow", "weights & biases", "wandb", "tensorboard", "airflow",

        # Data
        "sql", "postgresql", "mongodb", "redis", "spark", "hadoop", "pandas",
        "numpy", "dask", "ray",

        # MLOps
        "mlops", "ci/cd", "git", "github", "gitlab", "model deployment",
        "model monitoring", "a/b testing",

        # Specialized
        "rag", "retrieval augmented generation", "vector databases", "embeddings",
        "fine-tuning", "prompt engineering", "llmops", "generative ai"
    }

    EXPERIENCE_LEVELS = {
        "entry": ["entry", "junior", "associate", "intern", "graduate", "0-2 years"],
        "mid": ["mid", "intermediate", "engineer", "2-5 years", "3-7 years"],
        "senior": ["senior", "lead", "staff", "principal", "5+ years", "7+ years"],
        "management": ["manager", "director", "vp", "head of", "chief"]
    }

    def parse_file(self, file_path: Path) -> str:
        """Extract text from PDF or DOCX file."""
        file_path = Path(file_path)

        if file_path.suffix.lower() == ".pdf":
            return self._parse_pdf(file_path)
        elif file_path.suffix.lower() in [".docx", ".doc"]:
            return self._parse_docx(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_path.suffix}")

    def _parse_pdf(self, file_path: Path) -> str:
        """Extract text from PDF."""
        text = ""

        # Try pdfplumber first (better for complex PDFs)
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception:
            # Fallback to PyPDF2
            try:
                with open(file_path, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        text += page.extract_text() + "\n"
            except Exception as e:
                raise ValueError(f"Failed to parse PDF: {e}")

        return text

    def _parse_docx(self, file_path: Path) -> str:
        """Extract text from DOCX."""
        try:
            doc = docx.Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text
        except Exception as e:
            raise ValueError(f"Failed to parse DOCX: {e}")

    def extract_profile(self, text: str) -> Dict:
        """Extract structured profile from resume text."""
        text_lower = text.lower()

        profile = {
            "skills": self._extract_skills(text_lower),
            "experience_level": self._extract_experience_level(text_lower),
            "years_of_experience": self._extract_years_experience(text_lower),
            "education": self._extract_education(text_lower),
            "role_types": self._extract_role_types(text_lower),
            "company_preferences": self._extract_company_preferences(text_lower),
            "raw_text": text
        }

        return profile

    def _extract_skills(self, text: str) -> List[str]:
        """Extract technical skills from text."""
        found_skills = set()

        # Look for skills in the text
        for skill in self.TECH_SKILLS:
            # Use word boundaries for exact matches
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                found_skills.add(skill)

        # Also look for skills in common formats like "Skills: Python, ML, ..."
        skills_section = re.search(r'skills?[:\s]+(.*?)(?:\n\n|\n[A-Z]|$)', text, re.IGNORECASE | re.DOTALL)
        if skills_section:
            skills_text = skills_section.group(1)
            for skill in self.TECH_SKILLS:
                if skill in skills_text.lower():
                    found_skills.add(skill)

        return sorted(list(found_skills))

    def _extract_experience_level(self, text: str) -> str:
        """Determine experience level from text."""
        # Count indicators for each level
        level_scores = {level: 0 for level in ["entry", "mid", "senior", "management"]}

        for level, keywords in self.EXPERIENCE_LEVELS.items():
            for keyword in keywords:
                if keyword in text:
                    level_scores[level] += 1

        # Return the level with highest score
        if level_scores["management"] > 2:
            return "management"
        elif level_scores["senior"] > 2:
            return "senior"
        elif level_scores["mid"] > 2:
            return "mid"
        else:
            return "entry"

    def _extract_years_experience(self, text: str) -> int:
        """Extract years of experience."""
        # Look for patterns like "5 years", "5+ years", "2-5 years"
        patterns = [
            r'(\d+)\+?\s*years?\s*(?:of\s*)?experience',
            r'experience[:\s]+(\d+)\+?\s*years?',
            r'(\d+)\s*years?\s*in\s*(?:machine learning|ai|ml|data)',
        ]

        max_years = 0
        for pattern in patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                try:
                    years = int(match)
                    max_years = max(max_years, years)
                except ValueError:
                    pass

        return max_years

    def _extract_education(self, text: str) -> List[str]:
        """Extract education information."""
        education = []

        # Common degrees
        degrees = ["phd", "ph.d", "doctorate", "master", "ms", "m.s", "msc", "mba",
                   "bachelor", "bs", "b.s", "bsc", "ba", "b.a"]

        for degree in degrees:
            if degree in text:
                education.append(degree.upper())

        return list(set(education))

    def _extract_role_types(self, text: str) -> List[str]:
        """Extract types of roles from experience."""
        role_types = set()

        role_keywords = {
            "research": ["research", "scientist", "phd", "publication", "paper"],
            "engineering": ["engineer", "developer", "software", "production", "deployment"],
            "applied_ml": ["applied", "ml engineer", "machine learning engineer", "data scientist"],
            "leadership": ["lead", "manager", "director", "head of", "team lead"],
            "product": ["product", "pm", "product manager"],
        }

        for role_type, keywords in role_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    role_types.add(role_type)
                    break

        return list(role_types)

    def _extract_company_preferences(self, text: str) -> Dict[str, any]:
        """Extract company preferences if mentioned."""
        preferences = {
            "size": None,  # startup, mid, enterprise
            "stage": None,  # early, growth, established
            "industries": []
        }

        # Size preferences
        if any(word in text for word in ["startup", "early stage", "seed", "series a"]):
            preferences["size"] = "startup"
        elif any(word in text for word in ["enterprise", "large company", "fortune"]):
            preferences["size"] = "enterprise"

        # Industry mentions
        industries = ["healthcare", "finance", "fintech", "ecommerce", "robotics",
                      "autonomous", "climate", "education", "edtech"]
        for industry in industries:
            if industry in text:
                preferences["industries"].append(industry)

        return preferences


def parse_resume(file_path: str) -> Dict:
    """Main function to parse a resume file and return profile."""
    parser = ResumeParser()
    text = parser.parse_file(Path(file_path))
    profile = parser.extract_profile(text)
    return profile
