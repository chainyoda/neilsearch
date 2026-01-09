#!/usr/bin/env python3
"""Create sample job data for demonstration purposes."""
from datetime import datetime, timedelta
import random
from database import Database
from matcher import JobMatcher

# Sample AI/ML jobs
SAMPLE_JOBS = [
    {
        "board_name": "LinkedIn",
        "company": "OpenAI",
        "title": "Machine Learning Engineer",
        "location": "San Francisco, CA",
        "description": """
        We're looking for an ML engineer to join our applied research team.

        Requirements:
        - 2+ years experience with Python and PyTorch
        - Strong understanding of LLMs and transformers
        - Experience with GPT models and fine-tuning
        - Proficiency in distributed training
        - Knowledge of RLHF and alignment techniques

        Nice to have:
        - Research experience in NLP
        - Knowledge of JAX or TensorFlow
        - Publications in ML conferences
        """,
        "url": "https://openai.com/careers/ml-engineer-123"
    },
    {
        "board_name": "Indeed",
        "company": "Anthropic",
        "title": "Research Scientist - AI Safety",
        "location": "San Francisco, CA",
        "description": """
        Join our research team working on constitutional AI and safety.

        Requirements:
        - PhD in Computer Science, ML, or related field
        - Strong publication record in NLP or AI safety
        - Expert-level Python programming
        - Experience with large language models
        - Knowledge of reinforcement learning

        Nice to have:
        - Experience with interpretability research
        - Knowledge of game theory
        """,
        "url": "https://anthropic.com/careers/research-scientist-456"
    },
    {
        "board_name": "Wellfound",
        "company": "Scale AI",
        "title": "Senior ML Platform Engineer",
        "location": "San Francisco, CA",
        "description": """
        Build the infrastructure that powers AI at scale.

        Requirements:
        - 5+ years software engineering experience
        - Strong Python and Go skills
        - Experience with Kubernetes and Docker
        - Knowledge of ML frameworks (PyTorch, TensorFlow)
        - Experience with data pipelines and ETL

        Nice to have:
        - MLOps experience
        - Cloud platform expertise (AWS, GCP)
        - Experience with Ray or Dask
        """,
        "url": "https://scale.com/careers/ml-platform-789"
    },
    {
        "board_name": "Y Combinator",
        "company": "Cursor",
        "title": "AI Engineer - Code Generation",
        "location": "Remote",
        "description": """
        Help build the next generation of AI-powered coding tools.

        Requirements:
        - Strong Python and JavaScript/TypeScript skills
        - Experience with LLMs and prompt engineering
        - Understanding of code generation and analysis
        - Familiarity with GPT-4 and Claude APIs

        Nice to have:
        - Experience building developer tools
        - Knowledge of VSCode extension development
        - Interest in AI agents
        """,
        "url": "https://cursor.sh/careers/ai-engineer-101"
    },
    {
        "board_name": "LinkedIn",
        "company": "Google Brain",
        "title": "Research Engineer - LLMs",
        "location": "San Francisco, CA",
        "description": """
        Push the boundaries of large language model research.

        Requirements:
        - MS or PhD in Computer Science
        - Strong research background in ML/NLP
        - Expert Python and TensorFlow/JAX skills
        - Publication record at top conferences
        - Experience with transformer models

        Nice to have:
        - Experience with multimodal models
        - Knowledge of diffusion models
        - Systems optimization background
        """,
        "url": "https://careers.google.com/jobs/ml-research-202"
    },
    {
        "board_name": "Indeed",
        "company": "Hugging Face",
        "title": "ML Engineer - Open Source",
        "location": "Remote",
        "description": """
        Build tools for the ML community.

        Requirements:
        - 3+ years ML engineering experience
        - Deep knowledge of transformers library
        - Strong Python skills
        - Open source contributions
        - Experience with PyTorch

        Nice to have:
        - Knowledge of diffusion models
        - Experience with ONNX and model optimization
        - Community building experience
        """,
        "url": "https://huggingface.co/careers/ml-engineer-303"
    },
    {
        "board_name": "Wellfound",
        "company": "Perplexity AI",
        "title": "Founding ML Engineer",
        "location": "San Francisco, CA",
        "description": """
        Early-stage startup building next-gen search with AI.

        Requirements:
        - Strong Python skills
        - Experience with LLMs and retrieval systems
        - Knowledge of vector databases
        - RAG implementation experience
        - Fast-paced startup experience

        Nice to have:
        - Knowledge of search algorithms
        - Experience with embeddings
        - Full-stack web development skills
        """,
        "url": "https://perplexity.ai/careers/founding-ml-404"
    },
    {
        "board_name": "LinkedIn",
        "company": "Meta",
        "title": "Applied ML Engineer - Recommendations",
        "location": "Menlo Park, CA",
        "description": """
        Build ML systems powering recommendations for billions of users.

        Requirements:
        - 4+ years ML experience in production systems
        - Strong Python and C++ skills
        - Experience with recommendation systems
        - Knowledge of PyTorch
        - Distributed systems experience

        Nice to have:
        - Experience with ranking algorithms
        - Knowledge of graph neural networks
        - Large-scale system design
        """,
        "url": "https://metacareers.com/jobs/ml-recommendations-505"
    },
    {
        "board_name": "Indeed",
        "company": "Cohere",
        "title": "Applied Scientist - NLP",
        "location": "San Francisco, CA",
        "description": """
        Apply cutting-edge NLP research to production systems.

        Requirements:
        - MS/PhD in CS or related field
        - Strong NLP research background
        - Expert Python and deep learning skills
        - Experience with language models
        - Publication record

        Nice to have:
        - Industry experience in NLP
        - Knowledge of retrieval-augmented generation
        - Experience with evaluation methodologies
        """,
        "url": "https://cohere.com/careers/applied-scientist-606"
    },
    {
        "board_name": "Y Combinator",
        "company": "Replicate",
        "title": "ML Infrastructure Engineer",
        "location": "San Francisco, CA",
        "description": """
        Build the platform that makes ML models easy to deploy.

        Requirements:
        - Strong systems engineering background
        - Experience with Docker and Kubernetes
        - Python proficiency
        - Knowledge of ML model deployment
        - API design experience

        Nice to have:
        - Experience with serverless architectures
        - Knowledge of GPU optimization
        - DevOps background
        """,
        "url": "https://replicate.com/careers/ml-infra-707"
    }
]

def create_sample_data():
    """Create sample job data in the database."""
    with Database() as db:
        # Get profile
        profile_data = db.get_profile()
        if not profile_data:
            print("Error: No profile found. Run profile command first.")
            return

        print("Creating sample job data...")

        # Initialize matcher
        matcher = JobMatcher(profile_data['profile_data'])

        # Add jobs
        jobs_added = 0
        for i, job in enumerate(SAMPLE_JOBS):
            # Add some variation in posting dates
            days_ago = random.randint(0, 14)
            job["posted_date"] = (datetime.now() - timedelta(days=days_ago)).isoformat()
            job["scraped_date"] = datetime.now().isoformat()

            # Generate job ID
            import hashlib
            job["id"] = hashlib.md5(job["url"].encode()).hexdigest()

            # Match job against profile
            match_result = matcher.match_job(job)
            job.update(match_result)

            # Save to database
            is_new = db.save_job(job)
            if is_new:
                jobs_added += 1
                print(f"  [{i+1}/{len(SAMPLE_JOBS)}] Added: {job['title']} at {job['company']} (Score: {job['match_score']:.0f})")

        # Save scan history
        db.save_scan_history(jobs_added, 5, 45.5)

        print(f"\n✓ Created {jobs_added} sample jobs")
        print(f"\nNext step: Run 'python neilsearch.py dashboard' to view results!")

if __name__ == "__main__":
    create_sample_data()
