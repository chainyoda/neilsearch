"""Enhanced scrapers for AI company career pages using ATS APIs - US & Remote only."""
import time
import json
from datetime import datetime
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup
import config
from scrapers import BaseScraper
import re
from ai_companies_100 import (
    AI_COMPANIES_100,
    get_greenhouse_companies,
    get_lever_companies,
    get_ashby_companies,
    is_us_location,
    get_company_sector
)

# ML/AI role detection - shared across all scrapers
ML_TITLE_KEYWORDS = [
    # Core ML/AI titles
    "machine learning", "deep learning", "artificial intelligence",
    "data scientist", "data science", "research scientist", "research engineer",
    "ml engineer", "ai engineer", "applied scientist",
    # Specific domains
    "nlp", "natural language", "computer vision", "cv engineer",
    "speech", "robotics", "perception", "autonomous",
    "llm", "large language model", "generative ai", "genai",
    # Research
    "neural network", "reinforcement learning", "recommendation",
]

# Word-bounded keywords (must match as whole words)
ML_TITLE_KEYWORDS_BOUNDED = [
    "ml", "ai", "cv"  # These need word boundaries to avoid false matches
]

# Negative keywords - roles that are NOT ML-related
NON_ML_KEYWORDS = [
    "blockchain", "crypto", "web3", "wallet", "defi", "smart contract",
    "solidity", "rust engineer", "protocol engineer",
    "account executive", "sales", "marketing", "recruiter", "hr ",
    "legal", "counsel", "attorney", "paralegal",
    "accountant", "finance manager", "controller",
    "facilities", "office manager", "executive assistant",
    "customer support", "customer success", "community manager",
    "content writer", "copywriter", "social media",
    "security engineer", "security analyst", "soc analyst",
    "network engineer", "it support", "helpdesk",
    "product designer", "graphic designer", "ux writer",
    "devops", "sre", "site reliability", "infrastructure engineer",
    "backend engineer", "frontend engineer", "fullstack engineer",
    "mobile engineer", "ios engineer", "android engineer",
    "qa engineer", "test engineer", "quality assurance",
]

def is_ml_ai_role(title: str, description: str = "") -> bool:
    """
    Check if a job is ML/AI related based on title and description.
    More strict filtering to avoid false positives.
    """
    title_lower = title.lower()
    desc_lower = description.lower() if description else ""

    # First check for negative keywords in title - immediate rejection
    for neg_keyword in NON_ML_KEYWORDS:
        if neg_keyword in title_lower:
            return False

    # Check for ML keywords in title
    for keyword in ML_TITLE_KEYWORDS:
        if keyword in title_lower:
            return True

    # Check word-bounded keywords (avoid matching "email" for "ml", etc.)
    for keyword in ML_TITLE_KEYWORDS_BOUNDED:
        pattern = r'\b' + re.escape(keyword) + r'\b'
        if re.search(pattern, title_lower):
            return True

    # If title doesn't match, check if description has strong ML signals
    if desc_lower:
        ml_description_signals = [
            "machine learning", "deep learning", "neural network",
            "pytorch", "tensorflow", "model training", "model development",
            "nlp", "computer vision", "reinforcement learning",
            "large language model", "llm", "transformer",
        ]
        signal_count = sum(1 for signal in ml_description_signals if signal in desc_lower)
        # Require at least 2 ML signals in description if title didn't match
        if signal_count >= 2:
            return True

    return False
from web_scrapers import get_web_scraper, WEB_SCRAPERS


class GreenhouseScraper(BaseScraper):
    """Scrape jobs from Greenhouse ATS API."""

    def __init__(self, company_key: str):
        if company_key not in AI_COMPANIES_100:
            raise ValueError(f"Unknown company: {company_key}")

        self.company_key = company_key
        self.company_config = AI_COMPANIES_100[company_key]
        super().__init__(self.company_config["name"])
        self.api_url = self.company_config.get("api_url")

    def scrape(self) -> List[Dict]:
        """Scrape jobs from Greenhouse API."""
        if not self.api_url:
            return []

        jobs = []
        try:
            response = self.session.get(self.api_url, timeout=config.SCRAPE_TIMEOUT)
            response.raise_for_status()
            data = response.json()

            for job in data.get("jobs", []):
                # Filter for relevant locations
                location = job.get("location", {}).get("name", "")
                if not self._is_relevant_location(location):
                    continue

                # Filter for AI/ML related roles (check both title and description)
                title = job.get("title", "")
                description = self._extract_text(job.get("content", ""))
                if not is_ml_ai_role(title, description):
                    continue

                jobs.append({
                    "id": self.generate_job_id(job.get("absolute_url", "")),
                    "board_name": self.board_name,
                    "title": title,
                    "company": self.board_name,
                    "location": self.normalize_location(location),
                    "description": description,
                    "url": job.get("absolute_url", ""),
                    "posted_date": job.get("updated_at"),
                    "scraped_date": datetime.now().isoformat(),
                    "sector": get_company_sector(self.company_key)
                })

            print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} API error: {e}")

        return jobs

    def _is_relevant_location(self, location: str) -> bool:
        """Check if location is US-based or remote (excluding international)."""
        return is_us_location(location)

    def _extract_text(self, html: str) -> str:
        """Extract plain text from HTML."""
        if not html:
            return ""
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text(separator=" ", strip=True)[:5000]  # Limit length


class AshbyScraper(BaseScraper):
    """Scrape jobs from Ashby ATS API."""

    def __init__(self, company_key: str):
        if company_key not in AI_COMPANIES_100:
            raise ValueError(f"Unknown company: {company_key}")

        self.company_key = company_key
        self.company_config = AI_COMPANIES_100[company_key]
        super().__init__(self.company_config["name"])
        self.api_url = self.company_config.get("api_url")

    def scrape(self) -> List[Dict]:
        """Scrape jobs from Ashby API."""
        if not self.api_url:
            return []

        jobs = []
        try:
            response = self.session.get(self.api_url, timeout=config.SCRAPE_TIMEOUT)
            response.raise_for_status()
            data = response.json()

            for job in data.get("jobs", []):
                # Filter for relevant locations
                location = job.get("location", "")
                if not self._is_relevant_location(location):
                    continue

                # Filter for AI/ML related roles (check both title and description)
                title = job.get("title", "")
                description = job.get("descriptionPlain", "")[:5000]
                if not is_ml_ai_role(title, description):
                    continue

                jobs.append({
                    "id": self.generate_job_id(job.get("jobUrl", "")),
                    "board_name": self.board_name,
                    "title": title,
                    "company": self.board_name,
                    "location": self.normalize_location(location),
                    "description": description,
                    "url": job.get("jobUrl", ""),
                    "posted_date": job.get("publishedAt"),
                    "scraped_date": datetime.now().isoformat(),
                    "sector": get_company_sector(self.company_key)
                })

            print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} API error: {e}")

        return jobs

    def _is_relevant_location(self, location: str) -> bool:
        """Check if location is US-based or remote (excluding international)."""
        return is_us_location(location)


class LeverScraper(BaseScraper):
    """Scrape jobs from Lever ATS API."""

    def __init__(self, company_key: str):
        if company_key not in AI_COMPANIES_100:
            raise ValueError(f"Unknown company: {company_key}")

        self.company_key = company_key
        self.company_config = AI_COMPANIES_100[company_key]
        super().__init__(self.company_config["name"])
        self.api_url = self.company_config.get("api_url")

    def scrape(self) -> List[Dict]:
        """Scrape jobs from Lever API."""
        if not self.api_url:
            return []

        jobs = []
        try:
            response = self.session.get(self.api_url, timeout=config.SCRAPE_TIMEOUT)
            response.raise_for_status()
            data = response.json()

            for job in data:
                # Filter for relevant locations
                location = job.get("categories", {}).get("location", "")
                if not self._is_relevant_location(location):
                    continue

                # Filter for AI/ML related roles (check both title and description)
                title = job.get("text", "")
                description = self._extract_description(job)
                if not is_ml_ai_role(title, description):
                    continue

                jobs.append({
                    "id": self.generate_job_id(job.get("hostedUrl", "")),
                    "board_name": self.board_name,
                    "title": title,
                    "company": self.board_name,
                    "location": self.normalize_location(location),
                    "description": description,
                    "url": job.get("hostedUrl", ""),
                    "posted_date": None,
                    "scraped_date": datetime.now().isoformat(),
                    "sector": get_company_sector(self.company_key)
                })

            print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} API error: {e}")

        return jobs

    def _is_relevant_location(self, location: str) -> bool:
        """Check if location is US-based or remote (excluding international)."""
        return is_us_location(location)

    def _extract_description(self, job: Dict) -> str:
        """Extract job description."""
        desc_lists = job.get("lists", [])
        description = ""
        for item in desc_lists:
            description += item.get("text", "") + " " + item.get("content", "") + "\n"
        return description[:5000]  # Limit length


class CompanyScraperManager:
    """Manager for all company-specific scrapers."""

    def __init__(self):
        self.greenhouse_companies = get_greenhouse_companies()
        self.lever_companies = get_lever_companies()
        self.ashby_companies = get_ashby_companies()
        self.web_scraping_companies = list(WEB_SCRAPERS.keys())

    def scrape_all_companies(self, company_keys: Optional[List[str]] = None) -> List[Dict]:
        """
        Scrape all companies or specific ones.

        Args:
            company_keys: Optional list of company keys to scrape

        Returns:
            List of all jobs found
        """
        all_jobs = []

        # Determine which companies to scrape
        if company_keys:
            greenhouse_to_scrape = {k: v for k, v in self.greenhouse_companies.items() if k in company_keys}
            lever_to_scrape = {k: v for k, v in self.lever_companies.items() if k in company_keys}
            ashby_to_scrape = {k: v for k, v in self.ashby_companies.items() if k in company_keys}
            web_to_scrape = [k for k in self.web_scraping_companies if k in company_keys]
        else:
            greenhouse_to_scrape = self.greenhouse_companies
            lever_to_scrape = self.lever_companies
            ashby_to_scrape = self.ashby_companies
            web_to_scrape = self.web_scraping_companies

        # Scrape Ashby companies
        for company_key in ashby_to_scrape:
            try:
                scraper = AshbyScraper(company_key)
                jobs = scraper.scrape()
                all_jobs.extend(jobs)
                time.sleep(config.SCRAPE_DELAY)
            except Exception as e:
                print(f"  Error scraping {company_key}: {e}")

        # Scrape Greenhouse companies
        for company_key in greenhouse_to_scrape:
            try:
                scraper = GreenhouseScraper(company_key)
                jobs = scraper.scrape()
                all_jobs.extend(jobs)
                time.sleep(config.SCRAPE_DELAY)
            except Exception as e:
                print(f"  Error scraping {company_key}: {e}")

        # Scrape Lever companies
        for company_key in lever_to_scrape:
            try:
                scraper = LeverScraper(company_key)
                jobs = scraper.scrape()
                all_jobs.extend(jobs)
                time.sleep(config.SCRAPE_DELAY)
            except Exception as e:
                print(f"  Error scraping {company_key}: {e}")

        # Scrape web scraping companies (Playwright)
        for company_key in web_to_scrape:
            try:
                scraper = get_web_scraper(company_key)
                if scraper:
                    jobs = scraper.scrape()
                    all_jobs.extend(jobs)
                    time.sleep(config.SCRAPE_DELAY * 2)  # Slower for web scraping
            except Exception as e:
                print(f"  Error scraping {company_key}: {e}")

        return all_jobs

    def scrape_tier(self, tier: int) -> List[Dict]:
        """Scrape companies by tier (1-8)."""
        from ai_companies_100 import get_companies_by_tier

        tier_companies = get_companies_by_tier(tier)
        company_keys = list(tier_companies.keys())
        return self.scrape_all_companies(company_keys)

    def scrape_top_companies(self, limit: int = 10) -> List[Dict]:
        """Scrape top N companies (by tier)."""
        from ai_companies_100 import get_companies_by_tier

        # Get Tier 1 and 2 companies
        tier1 = list(get_companies_by_tier(1).keys())
        tier2 = list(get_companies_by_tier(2).keys())
        top_companies = (tier1 + tier2)[:limit]

        return self.scrape_all_companies(top_companies)


def scrape_ai_companies(company_keys: Optional[List[str]] = None) -> List[Dict]:
    """
    Convenience function to scrape AI companies.

    Args:
        company_keys: Optional list of company keys from ai_companies.AI_COMPANIES

    Returns:
        List of job dictionaries
    """
    manager = CompanyScraperManager()
    return manager.scrape_all_companies(company_keys)
