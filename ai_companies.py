"""Top AI/ML companies and their career pages."""

AI_COMPANIES = {
    # Tier 1: Leading AI Labs & Research
    "openai": {
        "name": "OpenAI",
        "url": "https://openai.com/careers",
        "jobs_url": "https://openai.com/careers/search",
        "api_url": "https://api.lever.co/v0/postings/openai",
        "locations": ["San Francisco", "Remote"],
        "type": "api"  # Uses Lever API
    },
    "anthropic": {
        "name": "Anthropic",
        "url": "https://www.anthropic.com/careers",
        "jobs_url": "https://boards.greenhouse.io/anthropic",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/anthropic/jobs",
        "locations": ["San Francisco"],
        "type": "api"  # Uses Greenhouse API
    },
    "deepmind": {
        "name": "Google DeepMind",
        "url": "https://www.deepmind.com/careers",
        "jobs_url": "https://www.deepmind.com/careers/jobs",
        "locations": ["Mountain View", "San Francisco"],
        "type": "scrape"
    },
    "meta_ai": {
        "name": "Meta AI (FAIR)",
        "url": "https://ai.meta.com/careers",
        "jobs_url": "https://www.metacareers.com/jobs",
        "api_url": "https://www.metacareers.com/graphql",
        "locations": ["Menlo Park", "San Francisco"],
        "type": "api"
    },
    "google_brain": {
        "name": "Google Brain/Research",
        "url": "https://research.google/careers",
        "jobs_url": "https://careers.google.com/jobs/results/?q=machine%20learning",
        "locations": ["Mountain View", "San Francisco"],
        "type": "scrape"
    },

    # Tier 2: AI-First Startups (Well-Funded)
    "cohere": {
        "name": "Cohere",
        "url": "https://cohere.com/careers",
        "jobs_url": "https://jobs.lever.co/cohere",
        "api_url": "https://api.lever.co/v0/postings/cohere",
        "locations": ["San Francisco", "Remote"],
        "type": "api"
    },
    "huggingface": {
        "name": "Hugging Face",
        "url": "https://huggingface.co/careers",
        "jobs_url": "https://apply.workable.com/huggingface",
        "locations": ["Remote", "San Francisco"],
        "type": "scrape"
    },
    "adept": {
        "name": "Adept",
        "url": "https://www.adept.ai/careers",
        "jobs_url": "https://jobs.ashbyhq.com/Adept",
        "api_url": "https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobBoardWithTeams",
        "locations": ["San Francisco"],
        "type": "api"
    },
    "inflection": {
        "name": "Inflection AI",
        "url": "https://inflection.ai/careers",
        "jobs_url": "https://jobs.lever.co/inflection-ai",
        "api_url": "https://api.lever.co/v0/postings/inflection-ai",
        "locations": ["Palo Alto"],
        "type": "api"
    },
    "character": {
        "name": "Character.AI",
        "url": "https://character.ai/careers",
        "jobs_url": "https://jobs.ashbyhq.com/character",
        "locations": ["Menlo Park"],
        "type": "scrape"
    },
    "perplexity": {
        "name": "Perplexity AI",
        "url": "https://www.perplexity.ai/careers",
        "jobs_url": "https://boards.greenhouse.io/perplexity",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/perplexity/jobs",
        "locations": ["San Francisco"],
        "type": "api"
    },
    "replicate": {
        "name": "Replicate",
        "url": "https://replicate.com/careers",
        "jobs_url": "https://jobs.ashbyhq.com/replicate",
        "locations": ["San Francisco"],
        "type": "scrape"
    },

    # Tier 3: AI Tools & Platforms
    "scale": {
        "name": "Scale AI",
        "url": "https://scale.com/careers",
        "jobs_url": "https://boards.greenhouse.io/scaleai",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/scaleai/jobs",
        "locations": ["San Francisco"],
        "type": "api"
    },
    "databricks": {
        "name": "Databricks",
        "url": "https://www.databricks.com/company/careers",
        "jobs_url": "https://www.databricks.com/company/careers/open-positions",
        "locations": ["San Francisco", "Mountain View"],
        "type": "scrape"
    },
    "weights_biases": {
        "name": "Weights & Biases",
        "url": "https://wandb.ai/careers",
        "jobs_url": "https://boards.greenhouse.io/wandb",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/wandb/jobs",
        "locations": ["San Francisco"],
        "type": "api"
    },
    "anyscale": {
        "name": "Anyscale",
        "url": "https://www.anyscale.com/careers",
        "jobs_url": "https://jobs.lever.co/anyscale",
        "api_url": "https://api.lever.co/v0/postings/anyscale",
        "locations": ["San Francisco"],
        "type": "api"
    },
    "modal": {
        "name": "Modal",
        "url": "https://modal.com/careers",
        "jobs_url": "https://jobs.ashbyhq.com/modal",
        "locations": ["San Francisco", "Remote"],
        "type": "scrape"
    },

    # Tier 4: AI-Powered Products
    "notion": {
        "name": "Notion",
        "url": "https://www.notion.so/careers",
        "jobs_url": "https://boards.greenhouse.io/notion",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/notion/jobs",
        "locations": ["San Francisco"],
        "type": "api"
    },
    "cursor": {
        "name": "Cursor",
        "url": "https://cursor.sh/careers",
        "jobs_url": "https://jobs.ashbyhq.com/cursor",
        "locations": ["Remote", "San Francisco"],
        "type": "scrape"
    },
    "replit": {
        "name": "Replit",
        "url": "https://replit.com/careers",
        "jobs_url": "https://jobs.lever.co/replit",
        "api_url": "https://api.lever.co/v0/postings/replit",
        "locations": ["San Francisco", "Remote"],
        "type": "api"
    },
    "midjourney": {
        "name": "Midjourney",
        "url": "https://www.midjourney.com/jobs",
        "jobs_url": "https://www.midjourney.com/jobs",
        "locations": ["San Francisco", "Remote"],
        "type": "scrape"
    },
    "runway": {
        "name": "Runway",
        "url": "https://runwayml.com/careers",
        "jobs_url": "https://boards.greenhouse.io/runwayml",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/runwayml/jobs",
        "locations": ["San Francisco", "Remote"],
        "type": "api"
    },
    "stability": {
        "name": "Stability AI",
        "url": "https://stability.ai/careers",
        "jobs_url": "https://stability.ai/careers",
        "locations": ["Remote"],
        "type": "scrape"
    },

    # Tier 5: Robotics & Applied AI
    "tesla_ai": {
        "name": "Tesla AI",
        "url": "https://www.tesla.com/careers",
        "jobs_url": "https://www.tesla.com/careers/search/?query=AI",
        "locations": ["Palo Alto"],
        "type": "scrape"
    },
    "cruise": {
        "name": "Cruise",
        "url": "https://getcruise.com/careers",
        "jobs_url": "https://getcruise.com/careers/jobs",
        "locations": ["San Francisco"],
        "type": "scrape"
    },
    "waymo": {
        "name": "Waymo",
        "url": "https://waymo.com/careers",
        "jobs_url": "https://waymo.com/careers/search",
        "locations": ["Mountain View", "San Francisco"],
        "type": "scrape"
    },
    "figure_ai": {
        "name": "Figure AI",
        "url": "https://www.figure.ai/careers",
        "jobs_url": "https://jobs.lever.co/figureai",
        "api_url": "https://api.lever.co/v0/postings/figureai",
        "locations": ["Sunnyvale"],
        "type": "api"
    },

    # Tier 6: Enterprise AI
    "microsoft_ai": {
        "name": "Microsoft AI Research",
        "url": "https://www.microsoft.com/en-us/research/careers",
        "jobs_url": "https://careers.microsoft.com/us/en/search-results?keywords=AI",
        "locations": ["Mountain View", "San Francisco"],
        "type": "scrape"
    },
    "aws_ai": {
        "name": "AWS AI/ML",
        "url": "https://aws.amazon.com/careers",
        "jobs_url": "https://www.amazon.jobs/en/search?base_query=machine+learning&loc_query=San+Francisco",
        "locations": ["San Francisco", "Palo Alto"],
        "type": "scrape"
    },
    "snowflake": {
        "name": "Snowflake",
        "url": "https://careers.snowflake.com",
        "jobs_url": "https://careers.snowflake.com/us/en/search-results?keywords=machine%20learning",
        "locations": ["San Mateo"],
        "type": "scrape"
    },
}

def get_companies_by_tier(tier: int = None):
    """Get companies by tier (1-6)."""
    tier_mapping = {
        1: ["openai", "anthropic", "deepmind", "meta_ai", "google_brain"],
        2: ["cohere", "huggingface", "adept", "inflection", "character", "perplexity", "replicate"],
        3: ["scale", "databricks", "weights_biases", "anyscale", "modal"],
        4: ["notion", "cursor", "replit", "midjourney", "runway", "stability"],
        5: ["tesla_ai", "cruise", "waymo", "figure_ai"],
        6: ["microsoft_ai", "aws_ai", "snowflake"]
    }

    if tier:
        return {k: AI_COMPANIES[k] for k in tier_mapping.get(tier, [])}
    return AI_COMPANIES

def get_api_companies():
    """Get companies that have public APIs."""
    return {k: v for k, v in AI_COMPANIES.items() if v.get("type") == "api"}

def get_greenhouse_companies():
    """Get companies using Greenhouse ATS."""
    return {k: v for k, v in AI_COMPANIES.items() if "greenhouse" in v.get("api_url", "")}

def get_lever_companies():
    """Get companies using Lever ATS."""
    return {k: v for k, v in AI_COMPANIES.items() if "lever" in v.get("api_url", "")}

def get_ashby_companies():
    """Get companies using Ashby ATS."""
    return {k: v for k, v in AI_COMPANIES.items() if "ashby" in v.get("jobs_url", "")}
