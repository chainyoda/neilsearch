"""Enhanced scrapers for AI company career pages using ATS APIs - US & Remote only."""
import time
import json
from datetime import datetime
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup
import config
from scrapers import BaseScraper
from ai_companies_100 import (
    AI_COMPANIES_100,
    get_greenhouse_companies,
    get_lever_companies,
    is_us_location
)
from web_scrapers import get_web_scraper, WEB_SCRAPERS


class GreenhouseScraper(BaseScraper):
    """Scrape jobs from Greenhouse ATS API."""

    def __init__(self, company_key: str):
        if company_key not in AI_COMPANIES_100:
            raise ValueError(f"Unknown company: {company_key}")

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

                # Filter for AI/ML related roles
                title = job.get("title", "")
                if not self._is_ml_related(title):
                    continue

                jobs.append({
                    "id": self.generate_job_id(job.get("absolute_url", "")),
                    "board_name": self.board_name,
                    "title": title,
                    "company": self.board_name,
                    "location": self.normalize_location(location),
                    "description": self._extract_text(job.get("content", "")),
                    "url": job.get("absolute_url", ""),
                    "posted_date": job.get("updated_at"),
                    "scraped_date": datetime.now().isoformat()
                })

            print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} API error: {e}")

        return jobs

    def _is_relevant_location(self, location: str) -> bool:
        """Check if location is US-based or remote (excluding international)."""
        return is_us_location(location)

    def _is_ml_related(self, title: str) -> bool:
        """Check if job title is ML/AI related."""
        title_lower = title.lower()
        keywords = ["machine learning", "ml", "ai", "artificial intelligence",
                   "deep learning", "data scientist", "research scientist",
                   "nlp", "computer vision", "llm", "neural", "model"]
        return any(keyword in title_lower for keyword in keywords)

    def _extract_text(self, html: str) -> str:
        """Extract plain text from HTML."""
        if not html:
            return ""
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text(separator=" ", strip=True)[:5000]  # Limit length


class LeverScraper(BaseScraper):
    """Scrape jobs from Lever ATS API."""

    def __init__(self, company_key: str):
        if company_key not in AI_COMPANIES_100:
            raise ValueError(f"Unknown company: {company_key}")

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

                # Filter for AI/ML related roles
                title = job.get("text", "")
                if not self._is_ml_related(title):
                    continue

                jobs.append({
                    "id": self.generate_job_id(job.get("hostedUrl", "")),
                    "board_name": self.board_name,
                    "title": title,
                    "company": self.board_name,
                    "location": self.normalize_location(location),
                    "description": self._extract_description(job),
                    "url": job.get("hostedUrl", ""),
                    "posted_date": None,
                    "scraped_date": datetime.now().isoformat()
                })

            print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} API error: {e}")

        return jobs

    def _is_relevant_location(self, location: str) -> bool:
        """Check if location is US-based or remote (excluding international)."""
        return is_us_location(location)

    def _is_ml_related(self, title: str) -> bool:
        """Check if job title is ML/AI related."""
        title_lower = title.lower()
        keywords = ["machine learning", "ml", "ai", "artificial intelligence",
                   "deep learning", "data scientist", "research scientist",
                   "nlp", "computer vision", "llm", "neural", "model"]
        return any(keyword in title_lower for keyword in keywords)

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
            web_to_scrape = [k for k in self.web_scraping_companies if k in company_keys]
        else:
            greenhouse_to_scrape = self.greenhouse_companies
            lever_to_scrape = self.lever_companies
            web_to_scrape = self.web_scraping_companies

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
        """Scrape companies by tier (1-6)."""
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
