"""Web scrapers for companies without public APIs using Playwright."""
import time
from datetime import datetime
from typing import List, Dict, Optional
from playwright.sync_api import sync_playwright, Page, Browser
from bs4 import BeautifulSoup
import config
from scrapers import BaseScraper
from ai_companies_100 import AI_COMPANIES_100, is_us_location


class PlaywrightScraper(BaseScraper):
    """Base class for Playwright-based web scrapers."""

    def __init__(self, company_key: str):
        if company_key not in AI_COMPANIES_100:
            raise ValueError(f"Unknown company: {company_key}")

        self.company_config = AI_COMPANIES_100[company_key]
        super().__init__(self.company_config["name"])
        self.jobs_url = self.company_config.get("jobs_url")
        self.company_key = company_key

    def scrape(self) -> List[Dict]:
        """Override in subclass - scrape jobs using Playwright."""
        raise NotImplementedError("Subclass must implement scrape()")

    def _is_ml_related(self, title: str, description: str = "") -> bool:
        """Check if job is ML/AI related."""
        text = (title + " " + description).lower()
        keywords = [
            "machine learning", "ml", "ai", "artificial intelligence",
            "deep learning", "data scientist", "research scientist",
            "nlp", "computer vision", "llm", "neural", "model",
            "pytorch", "tensorflow", "data science", "ml engineer",
            "ai engineer", "research engineer"
        ]
        return any(keyword in text for keyword in keywords)


class MicrosoftScraper(PlaywrightScraper):
    """Scraper for Microsoft Research/AI jobs."""

    def scrape(self) -> List[Dict]:
        """Scrape Microsoft career page."""
        jobs = []

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                # Navigate to Microsoft careers search
                page.goto(self.jobs_url, wait_until="domcontentloaded", timeout=60000)
                time.sleep(5)  # Wait for dynamic content to load

                # Get page content
                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')

                # Find job listings - Microsoft uses specific structure
                job_elements = soup.find_all(['div', 'article'], class_=lambda x: x and ('job' in x.lower() or 'result' in x.lower()))

                for elem in job_elements[:50]:  # Limit to first 50
                    try:
                        # Extract title
                        title_elem = elem.find(['h2', 'h3', 'a'], class_=lambda x: x and 'title' in x.lower())
                        if not title_elem:
                            title_elem = elem.find('a')

                        if not title_elem:
                            continue

                        title = title_elem.get_text(strip=True)

                        # Check if ML/AI related
                        if not self._is_ml_related(title):
                            continue

                        # Extract location
                        location_elem = elem.find(['span', 'div'], class_=lambda x: x and 'location' in x.lower())
                        location = location_elem.get_text(strip=True) if location_elem else ""

                        # Filter for US locations
                        if location and not is_us_location(location):
                            continue

                        # Extract URL
                        link = title_elem.get('href', '') if title_elem.name == 'a' else elem.find('a').get('href', '')
                        if link and not link.startswith('http'):
                            link = 'https://careers.microsoft.com' + link

                        jobs.append({
                            "id": self.generate_job_id(link),
                            "board_name": self.board_name,
                            "title": title,
                            "company": self.board_name,
                            "location": self.normalize_location(location) if location else "Remote",
                            "description": title,  # Limited description from listing
                            "url": link,
                            "posted_date": None,
                            "scraped_date": datetime.now().isoformat()
                        })

                    except Exception as e:
                        continue

                browser.close()
                print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} scraping error: {e}")

        return jobs


class AmazonScraper(PlaywrightScraper):
    """Scraper for Amazon Science/ML jobs."""

    def scrape(self) -> List[Dict]:
        """Scrape Amazon jobs page."""
        jobs = []

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                # Navigate to Amazon jobs search
                page.goto(self.jobs_url, wait_until="domcontentloaded", timeout=60000)
                time.sleep(5)

                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')

                # Find job cards
                job_elements = soup.find_all(['div', 'article'], class_=lambda x: x and 'job' in x.lower())

                for elem in job_elements[:50]:
                    try:
                        # Extract title
                        title_elem = elem.find(['h3', 'h2', 'a'])
                        if not title_elem:
                            continue

                        title = title_elem.get_text(strip=True)

                        if not self._is_ml_related(title):
                            continue

                        # Extract location
                        location_elem = elem.find(['span', 'div'], text=lambda x: x and any(city in str(x).lower() for city in ['seattle', 'san francisco', 'new york', 'remote']))
                        location = location_elem.get_text(strip=True) if location_elem else ""

                        if location and not is_us_location(location):
                            continue

                        # Extract URL
                        link = elem.find('a').get('href', '') if elem.find('a') else ''
                        if link and not link.startswith('http'):
                            link = 'https://www.amazon.jobs' + link

                        jobs.append({
                            "id": self.generate_job_id(link),
                            "board_name": self.board_name,
                            "title": title,
                            "company": self.board_name,
                            "location": self.normalize_location(location) if location else "Remote",
                            "description": title,
                            "url": link,
                            "posted_date": None,
                            "scraped_date": datetime.now().isoformat()
                        })

                    except Exception as e:
                        continue

                browser.close()
                print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} scraping error: {e}")

        return jobs


class GoogleScraper(PlaywrightScraper):
    """Scraper for Google Brain/DeepMind jobs."""

    def scrape(self) -> List[Dict]:
        """Scrape Google careers page."""
        jobs = []

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                page.goto(self.jobs_url, wait_until="domcontentloaded", timeout=60000)
                time.sleep(5)

                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')

                # Find job listings
                job_elements = soup.find_all(['li', 'div'], class_=lambda x: x and 'job' in x.lower())

                for elem in job_elements[:50]:
                    try:
                        title_elem = elem.find(['h3', 'h2', 'a'])
                        if not title_elem:
                            continue

                        title = title_elem.get_text(strip=True)

                        if not self._is_ml_related(title):
                            continue

                        # Extract location
                        location_elem = elem.find(['span', 'div'], class_=lambda x: x and 'location' in x.lower())
                        location = location_elem.get_text(strip=True) if location_elem else ""

                        if location and not is_us_location(location):
                            continue

                        # Extract URL
                        link = elem.find('a').get('href', '') if elem.find('a') else ''
                        if link and not link.startswith('http'):
                            link = 'https://careers.google.com' + link

                        jobs.append({
                            "id": self.generate_job_id(link),
                            "board_name": self.board_name,
                            "title": title,
                            "company": self.board_name,
                            "location": self.normalize_location(location) if location else "Remote",
                            "description": title,
                            "url": link,
                            "posted_date": None,
                            "scraped_date": datetime.now().isoformat()
                        })

                    except Exception as e:
                        continue

                browser.close()
                print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} scraping error: {e}")

        return jobs


class AppleScraper(PlaywrightScraper):
    """Scraper for Apple Machine Learning jobs."""

    def scrape(self) -> List[Dict]:
        """Scrape Apple jobs page."""
        jobs = []

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                page.goto(self.jobs_url, wait_until="domcontentloaded", timeout=60000)
                time.sleep(5)

                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')

                # Find job table rows
                job_elements = soup.find_all(['tr', 'div'], class_=lambda x: x and ('row' in x.lower() or 'result' in x.lower()))

                for elem in job_elements[:50]:
                    try:
                        title_elem = elem.find(['a', 'h3'])
                        if not title_elem:
                            continue

                        title = title_elem.get_text(strip=True)

                        if not self._is_ml_related(title):
                            continue

                        # Extract location
                        location_elem = elem.find(['span', 'td'], class_=lambda x: x and 'location' in x.lower())
                        location = location_elem.get_text(strip=True) if location_elem else ""

                        if location and not is_us_location(location):
                            continue

                        # Extract URL
                        link = title_elem.get('href', '') if title_elem.name == 'a' else elem.find('a').get('href', '')
                        if link and not link.startswith('http'):
                            link = 'https://jobs.apple.com' + link

                        jobs.append({
                            "id": self.generate_job_id(link),
                            "board_name": self.board_name,
                            "title": title,
                            "company": self.board_name,
                            "location": self.normalize_location(location) if location else "Remote",
                            "description": title,
                            "url": link,
                            "posted_date": None,
                            "scraped_date": datetime.now().isoformat()
                        })

                    except Exception as e:
                        continue

                browser.close()
                print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} scraping error: {e}")

        return jobs


class MetaScraper(PlaywrightScraper):
    """Scraper for Meta AI (FAIR) jobs."""

    def scrape(self) -> List[Dict]:
        """Scrape Meta careers page."""
        jobs = []

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                page.goto(self.jobs_url, wait_until="domcontentloaded", timeout=60000)
                time.sleep(5)

                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')

                # Find job cards
                job_elements = soup.find_all(['div', 'a'], attrs={'data-testid': lambda x: x and 'job' in x.lower() if x else False})
                if not job_elements:
                    job_elements = soup.find_all(['div'], class_=lambda x: x and 'job' in x.lower())

                for elem in job_elements[:50]:
                    try:
                        title_elem = elem.find(['a', 'h2', 'h3'])
                        if not title_elem:
                            continue

                        title = title_elem.get_text(strip=True)

                        if not self._is_ml_related(title):
                            continue

                        # Extract location
                        location_elem = elem.find(['span', 'div'], class_=lambda x: x and 'location' in x.lower())
                        location = location_elem.get_text(strip=True) if location_elem else ""

                        if location and not is_us_location(location):
                            continue

                        # Extract URL
                        link = title_elem.get('href', '') if title_elem.name == 'a' else elem.find('a').get('href', '')
                        if link and not link.startswith('http'):
                            link = 'https://www.metacareers.com' + link

                        jobs.append({
                            "id": self.generate_job_id(link),
                            "board_name": self.board_name,
                            "title": title,
                            "company": self.board_name,
                            "location": self.normalize_location(location) if location else "Remote",
                            "description": title,
                            "url": link,
                            "posted_date": None,
                            "scraped_date": datetime.now().isoformat()
                        })

                    except Exception as e:
                        continue

                browser.close()
                print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} scraping error: {e}")

        return jobs


class NetflixScraper(PlaywrightScraper):
    """Scraper for Netflix ML jobs."""

    def scrape(self) -> List[Dict]:
        """Scrape Netflix jobs page."""
        jobs = []

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                page.goto(self.jobs_url, wait_until="domcontentloaded", timeout=60000)
                time.sleep(5)

                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')

                # Find job cards
                job_elements = soup.find_all(['div', 'li', 'article'], class_=lambda x: x and ('job' in x.lower() or 'position' in x.lower()))

                for elem in job_elements[:50]:
                    try:
                        title_elem = elem.find(['h2', 'h3', 'a'])
                        if not title_elem:
                            continue

                        title = title_elem.get_text(strip=True)

                        if not self._is_ml_related(title):
                            continue

                        # Extract location
                        location_elem = elem.find(['span', 'div'], class_=lambda x: x and 'location' in x.lower())
                        location = location_elem.get_text(strip=True) if location_elem else ""

                        if location and not is_us_location(location):
                            continue

                        # Extract URL
                        link = title_elem.get('href', '') if title_elem.name == 'a' else elem.find('a').get('href', '')
                        if link and not link.startswith('http'):
                            link = 'https://jobs.netflix.com' + link

                        jobs.append({
                            "id": self.generate_job_id(link),
                            "board_name": self.board_name,
                            "title": title,
                            "company": self.board_name,
                            "location": self.normalize_location(location) if location else "Remote",
                            "description": title,
                            "url": link,
                            "posted_date": None,
                            "scraped_date": datetime.now().isoformat()
                        })

                    except Exception as e:
                        continue

                browser.close()
                print(f"  Found {len(jobs)} jobs from {self.board_name}")

        except Exception as e:
            print(f"  {self.board_name} scraping error: {e}")

        return jobs


# Mapping of company keys to scraper classes
WEB_SCRAPERS = {
    "microsoft_research": MicrosoftScraper,
    "amazon_science": AmazonScraper,
    "google_brain": GoogleScraper,
    "deepmind": GoogleScraper,
    "apple_ml": AppleScraper,
    "meta_ai": MetaScraper,
    "netflix": NetflixScraper,
}


def get_web_scraper(company_key: str) -> Optional[PlaywrightScraper]:
    """Get the appropriate web scraper for a company."""
    scraper_class = WEB_SCRAPERS.get(company_key)
    if scraper_class:
        return scraper_class(company_key)
    return None
