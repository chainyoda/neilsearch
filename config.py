"""Configuration settings for NeilSearch."""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Database
DB_PATH = BASE_DIR / "neilsearch.db"

# Data retention
DATA_RETENTION_DAYS = 30

# Scraping settings
SCRAPE_TIMEOUT = 30  # seconds
SCRAPE_DELAY = 2  # seconds between requests
MAX_RETRIES = 3
USER_AGENT = "NeilSearch/1.0 (Job Search Tool)"

# Location settings
TARGET_LOCATIONS = [
    "San Francisco, CA",
    "San Francisco",
    "SF",
    "Bay Area",
    "Remote"
]

# Job boards configuration
JOB_BOARDS = {
    "linkedin": {
        "name": "LinkedIn",
        "enabled": True,
        "method": "api",  # or 'scrape'
        "priority": 1
    },
    "indeed": {
        "name": "Indeed",
        "enabled": True,
        "method": "api",
        "priority": 1
    },
    "glassdoor": {
        "name": "Glassdoor",
        "enabled": True,
        "method": "scrape",
        "priority": 1
    },
    "angellist": {
        "name": "Wellfound (AngelList)",
        "enabled": True,
        "method": "scrape",
        "priority": 1
    },
    "ycombinator": {
        "name": "Y Combinator Jobs",
        "enabled": True,
        "method": "scrape",
        "priority": 1
    },
    "aijobs": {
        "name": "AI Jobs Board",
        "enabled": True,
        "method": "scrape",
        "priority": 1
    },
    "huggingface": {
        "name": "Hugging Face Jobs",
        "enabled": True,
        "method": "scrape",
        "priority": 1
    },
    "openai": {
        "name": "OpenAI Careers",
        "enabled": True,
        "method": "scrape",
        "priority": 1
    },
    "anthropic": {
        "name": "Anthropic Careers",
        "enabled": True,
        "method": "scrape",
        "priority": 1
    },
    "google": {
        "name": "Google Careers",
        "enabled": True,
        "method": "scrape",
        "priority": 2
    }
}

# Matching weights
MATCH_WEIGHTS = {
    "skills": 40,
    "role_fit": 30,
    "company_traits": 20,
    "experience_level": 10
}

# Location bonuses
LOCATION_BONUS = {
    "san_francisco": 5,
    "bay_area": 3,
    "remote": 2
}

# Dashboard settings
DASHBOARD_OUTPUT = BASE_DIR / "dashboard.html"
JOBS_PER_PAGE = 50

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = BASE_DIR / "neilsearch.log"
