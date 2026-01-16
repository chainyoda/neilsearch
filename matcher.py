"""Job matching and scoring algorithm."""
import re
from typing import Dict, List, Tuple, Set
import config


class JobMatcher:
    """Match jobs against candidate profile and generate scores."""

    def __init__(self, profile: Dict):
        """Initialize matcher with candidate profile."""
        self.profile = profile
        self.candidate_skills = set(s.lower() for s in profile.get("skills", []))
        self.experience_level = profile.get("experience_level", "mid")
        self.years_experience = profile.get("years_of_experience", 0)
        self.role_types = set(profile.get("role_types", []))
        self.company_prefs = profile.get("company_preferences", {})

    def match_job(self, job: Dict) -> Dict:
        """
        Match a job against the profile and return scoring details.

        Returns dict with:
        - match_score: Overall score (0-100)
        - match_breakdown: Scores by category
        - skills_matched: List of matched skills
        - skills_missing: List of required skills not in profile
        - match_explanation: Human-readable explanation
        """
        title = job.get("title", "").lower()
        description = job.get("description", "").lower()
        location = job.get("location", "").lower()
        full_text = f"{title} {description}"

        # Calculate component scores
        skills_score, skills_matched, skills_missing = self._score_skills(full_text)
        role_score = self._score_role_fit(title, description)
        company_score = self._score_company_traits(job)
        experience_score = self._score_experience_level(title, description)
        fresh_grad_score = self._score_fresh_grad_friendly(title, description)

        # Calculate total with weights
        weights = config.MATCH_WEIGHTS
        total_score = (
            (skills_score / 40) * weights["skills"] +
            (role_score / 30) * weights["role_fit"] +
            (company_score / 20) * weights["company_traits"] +
            (experience_score / 10) * weights["experience_level"] +
            (fresh_grad_score / 30) * weights["fresh_grad_friendly"]
        )

        # Add location bonus
        location_bonus = self._get_location_bonus(location)
        total_score = min(100, total_score + location_bonus)

        # Generate explanation
        explanation = self._generate_explanation(
            total_score, skills_matched, skills_missing,
            role_score, company_score, experience_score
        )

        return {
            "match_score": round(total_score, 1),
            "match_breakdown": {
                "skills": round(skills_score, 1),
                "role_fit": round(role_score, 1),
                "company_traits": round(company_score, 1),
                "experience_level": round(experience_score, 1),
                "fresh_grad_friendly": round(fresh_grad_score, 1),
                "location_bonus": location_bonus
            },
            "skills_matched": skills_matched,
            "skills_missing": skills_missing,
            "match_explanation": explanation
        }

    def _score_skills(self, text: str) -> Tuple[float, List[str], List[str]]:
        """Score based on skills match. Returns (score, matched_skills, missing_skills)."""
        # Extract required and nice-to-have skills from job posting
        required_skills = self._extract_required_skills(text)
        nice_to_have_skills = self._extract_nice_to_have_skills(text)

        matched_required = []
        matched_nice = []
        missing_required = []

        # Check required skills
        for skill in required_skills:
            if skill.lower() in self.candidate_skills:
                matched_required.append(skill)
            else:
                missing_required.append(skill)

        # Check nice-to-have skills
        for skill in nice_to_have_skills:
            if skill.lower() in self.candidate_skills:
                matched_nice.append(skill)

        # Calculate score
        score = 0
        score += len(matched_required) * 8  # 8 points per required skill
        score += len(matched_nice) * 4      # 4 points per nice-to-have
        score -= len(missing_required) * 5  # -5 for missing required skills

        # Cap at 40 (max for skills category)
        score = max(0, min(40, score))

        all_matched = matched_required + matched_nice
        return score, all_matched, missing_required

    def _extract_required_skills(self, text: str) -> Set[str]:
        """Extract required skills from job description."""
        required_skills = set()

        # Look for requirements section
        req_section = re.search(
            r'(?:requirements?|required|qualifications?|must have)[:\s]+(.*?)(?=(?:nice to have|preferred|responsibilities|about|$))',
            text,
            re.IGNORECASE | re.DOTALL
        )

        text_to_search = req_section.group(1) if req_section else text

        # Common skill patterns
        skill_patterns = [
            r'experience (?:with|in) ([\w\s,/\+\-\.]+)',
            r'proficiency in ([\w\s,/\+\-\.]+)',
            r'strong ([\w\s,/\+\-\.]+) skills',
            r'knowledge of ([\w\s,/\+\-\.]+)',
        ]

        for pattern in skill_patterns:
            matches = re.findall(pattern, text_to_search, re.IGNORECASE)
            for match in matches:
                # Split by comma and extract individual skills
                for skill in match.split(','):
                    skill = skill.strip()
                    if len(skill) > 2 and len(skill) < 50:
                        # Check if it's a known tech skill
                        skill_lower = skill.lower()
                        for known_skill in self._get_all_tech_skills():
                            if known_skill in skill_lower:
                                required_skills.add(known_skill)

        return required_skills

    def _extract_nice_to_have_skills(self, text: str) -> Set[str]:
        """Extract nice-to-have skills."""
        nice_skills = set()

        # Look for nice-to-have section
        nice_section = re.search(
            r'(?:nice to have|preferred|bonus|plus)[:\s]+(.*?)(?=(?:responsibilities|about|$))',
            text,
            re.IGNORECASE | re.DOTALL
        )

        if nice_section:
            text_to_search = nice_section.group(1)
            for known_skill in self._get_all_tech_skills():
                if known_skill in text_to_search.lower():
                    nice_skills.add(known_skill)

        return nice_skills

    def _get_all_tech_skills(self) -> Set[str]:
        """Get all known tech skills from resume parser."""
        from resume_parser import ResumeParser
        return ResumeParser.TECH_SKILLS

    def _score_role_fit(self, title: str, description: str) -> float:
        """Score based on role type alignment."""
        score = 0

        # Check if role matches candidate's experience
        role_keywords = {
            "research": ["research", "scientist", "phd"],
            "engineering": ["engineer", "developer", "software"],
            "applied_ml": ["machine learning engineer", "ml engineer", "applied"],
            "leadership": ["lead", "senior", "staff", "principal"],
            "product": ["product"]
        }

        matches = 0
        for role_type in self.role_types:
            if role_type in role_keywords:
                keywords = role_keywords[role_type]
                for keyword in keywords:
                    if keyword in title or keyword in description:
                        matches += 1
                        break

        if matches >= 2:
            score = 30
        elif matches == 1:
            score = 20
        else:
            score = 10

        return score

    def _score_company_traits(self, job: Dict) -> float:
        """Score based on company traits."""
        score = 20  # Default score

        company = job.get("company", "").lower()
        description = job.get("description", "").lower()

        # Company size matching
        preferred_size = self.company_prefs.get("size")
        if preferred_size:
            size_indicators = {
                "startup": ["startup", "seed", "series a", "early stage"],
                "enterprise": ["enterprise", "fortune", "established", "global"]
            }

            if preferred_size in size_indicators:
                for indicator in size_indicators[preferred_size]:
                    if indicator in description or indicator in company:
                        score += 5
                        break

        # Industry matching
        preferred_industries = self.company_prefs.get("industries", [])
        for industry in preferred_industries:
            if industry in description or industry in company:
                score += 5
                break

        return min(20, score)

    def _score_experience_level(self, title: str, description: str) -> float:
        """Score based on experience level match."""
        job_level = self._detect_job_level(title, description)

        level_hierarchy = ["entry", "mid", "senior", "management"]
        candidate_idx = level_hierarchy.index(self.experience_level)
        job_idx = level_hierarchy.index(job_level)

        diff = abs(candidate_idx - job_idx)

        if diff == 0:
            return 10
        elif diff == 1:
            return 5
        else:
            return 0

    def _detect_job_level(self, title: str, description: str) -> str:
        """Detect job seniority level."""
        text = f"{title} {description}".lower()

        if any(word in text for word in ["senior", "sr", "staff", "principal", "lead", "5+ years", "7+ years"]):
            return "senior"
        elif any(word in text for word in ["manager", "director", "head of"]):
            return "management"
        elif any(word in text for word in ["junior", "entry", "associate", "0-2 years", "new grad"]):
            return "entry"
        else:
            return "mid"

    def _score_fresh_grad_friendly(self, title: str, description: str) -> float:
        """Score based on how suitable the job is for fresh graduates."""
        title_lower = title.lower()
        text = f"{title} {description}".lower()
        score = 15  # Start with neutral score

        # HIGHEST priority: Internship/Intern in job title (big bonus)
        if "intern" in title_lower or "internship" in title_lower:
            score += 25  # Major bonus for internship positions

        # Strong positive indicators for fresh grads (high bonus)
        fresh_grad_keywords = [
            "new grad", "new graduate", "recent graduate", "fresh graduate",
            "entry level", "entry-level", "junior", "associate",
            "university graduate", "college graduate",
            "0-2 years", "0-1 years", "1-2 years", "0 years",
            "no experience required", "will train",
            "early career", "early-career", "starting your career",
            "rotational program", "graduate program", "new college",
            "internship", "summer intern", "fall intern", "spring intern",
            "co-op", "coop program", "apprentice", "apprenticeship",
            "graduate trainee", "trainee program", "campus hire"
        ]

        for keyword in fresh_grad_keywords:
            if keyword in text:
                score += 10  # Big bonus for each fresh grad indicator

        # Internship mentions in description (even if not in title)
        if "intern" in text and "intern" not in title_lower:
            score += 8

        # Moderate positive indicators
        moderate_keywords = [
            "mentorship", "training program", "learn", "growth opportunity",
            "develop your skills", "bachelor", "master", "phd",
            "recent grads welcome", "all levels"
        ]

        for keyword in moderate_keywords:
            if keyword in text:
                score += 3

        # Negative indicators (require too much experience)
        experience_patterns = [
            (r"(\d+)\+?\s*years?\s*(of)?\s*(experience|exp)", -5),  # "X years experience"
            (r"(\d+)-(\d+)\s*years", -3),  # "X-Y years"
        ]

        for pattern, penalty in experience_patterns:
            match = re.search(pattern, text)
            if match:
                years = int(match.group(1))
                if years >= 5:
                    score -= 20  # Heavy penalty for 5+ years required
                elif years >= 3:
                    score -= 10  # Moderate penalty for 3-4 years
                elif years >= 2:
                    score -= 3   # Small penalty for 2 years

        # Strong negative indicators
        senior_keywords = [
            "senior", "staff", "principal", "lead", "director",
            "manager", "head of", "vp ", "vice president",
            "extensive experience", "proven track record",
            "10+ years", "8+ years", "7+ years", "6+ years"
        ]

        for keyword in senior_keywords:
            if keyword in title.lower():  # Extra penalty if in title
                score -= 15
            elif keyword in text:
                score -= 5

        # Cap score between 0 and 30
        return max(0, min(30, score))

    def _get_location_bonus(self, location: str) -> float:
        """Calculate location bonus points."""
        location_lower = location.lower()

        if "san francisco" in location_lower or location_lower == "sf":
            return config.LOCATION_BONUS["san_francisco"]
        elif any(area in location_lower for area in ["bay area", "palo alto", "mountain view", "oakland", "berkeley"]):
            return config.LOCATION_BONUS["bay_area"]
        elif "london" in location_lower:
            return config.LOCATION_BONUS["london"]
        elif any(area in location_lower for area in ["united kingdom", "uk", "england", "cambridge", "oxford", "edinburgh", "manchester"]):
            return config.LOCATION_BONUS["uk"]
        elif "remote" in location_lower:
            return config.LOCATION_BONUS["remote"]

        return 0

    def _generate_explanation(
        self,
        total_score: float,
        skills_matched: List[str],
        skills_missing: List[str],
        role_score: float,
        company_score: float,
        experience_score: float
    ) -> str:
        """Generate human-readable match explanation."""
        parts = []

        # Overall assessment
        if total_score >= 80:
            parts.append("Excellent match!")
        elif total_score >= 60:
            parts.append("Good match.")
        else:
            parts.append("Moderate match.")

        # Skills
        if skills_matched:
            top_skills = skills_matched[:5]
            parts.append(f"Matched skills: {', '.join(top_skills)}.")

        if skills_missing:
            parts.append(f"Missing: {', '.join(skills_missing[:3])}.")

        # Role fit
        if role_score >= 25:
            parts.append("Role aligns well with experience.")
        elif role_score < 15:
            parts.append("Role alignment unclear.")

        # Experience
        if experience_score >= 8:
            parts.append("Seniority level matches.")

        return " ".join(parts)
