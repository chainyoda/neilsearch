"""Job board scrapers."""
import time
import hashlib
from datetime import datetime
from typing import List, Dict, Optional
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
import config


class BaseScraper(ABC):
    """Base class for job board scrapers."""

    def __init__(self, board_name: str):
        self.board_name = board_name
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": config.USER_AGENT})

    @abstractmethod
    def scrape(self) -> List[Dict]:
        """Scrape jobs from the board. Must be implemented by subclasses."""
        pass

    def generate_job_id(self, url: str) -> str:
        """Generate unique job ID from URL."""
        return hashlib.md5(url.encode()).hexdigest()

    def normalize_location(self, location: str) -> str:
        """Normalize location string."""
        if not location:
            return ""
        location = location.strip()
        # Standardize common variations
        location = location.replace("San Francisco Bay Area", "San Francisco, CA")
        location = location.replace("SF", "San Francisco")
        return location

    def sleep(self):
        """Polite delay between requests."""
        time.sleep(config.SCRAPE_DELAY)


class LinkedInScraper(BaseScraper):
    """Scrape LinkedIn jobs."""

    def __init__(self):
        super().__init__("LinkedIn")
        self.base_url = "https://www.linkedin.com/jobs/search"

    def scrape(self) -> List[Dict]:
        """Scrape LinkedIn jobs."""
        jobs = []

        # LinkedIn requires authentication for API access
        # For now, we'll use public job search with browser automation
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                # Search for AI/ML jobs in San Francisco
                keywords = ["machine learning", "ai engineer", "ml engineer", "data scientist ai"]
                for keyword in keywords[:2]:  # Limit to avoid rate limiting
                    url = f"{self.base_url}?keywords={keyword}&location=San Francisco, CA"
                    page.goto(url, wait_until="domcontentloaded", timeout=config.SCRAPE_TIMEOUT * 1000)
                    time.sleep(3)  # Let page load

                    # Extract job cards
                    job_cards = page.query_selector_all(".job-search-card")

                    for card in job_cards[:10]:  # Limit per keyword
                        try:
                            title_elem = card.query_selector(".base-search-card__title")
                            company_elem = card.query_selector(".base-search-card__subtitle")
                            location_elem = card.query_selector(".job-search-card__location")
                            link_elem = card.query_selector("a")

                            if title_elem and company_elem and link_elem:
                                title = title_elem.inner_text().strip()
                                company = company_elem.inner_text().strip()
                                location = location_elem.inner_text().strip() if location_elem else "San Francisco, CA"
                                url = link_elem.get_attribute("href")

                                jobs.append({
                                    "id": self.generate_job_id(url),
                                    "board_name": self.board_name,
                                    "title": title,
                                    "company": company,
                                    "location": self.normalize_location(location),
                                    "url": url,
                                    "description": "",  # Would need to click through to get full description
                                    "posted_date": None,
                                    "scraped_date": datetime.now().isoformat()
                                })
                        except Exception as e:
                            print(f"Error parsing LinkedIn job card: {e}")
                            continue

                    self.sleep()

                browser.close()

        except Exception as e:
            print(f"LinkedIn scraping error: {e}")

        return jobs


class IndeedScraper(BaseScraper):
    """Scrape Indeed jobs."""

    def __init__(self):
        super().__init__("Indeed")
        self.base_url = "https://www.indeed.com/jobs"

    def scrape(self) -> List[Dict]:
        """Scrape Indeed jobs."""
        jobs = []

        keywords = ["machine learning engineer", "ai engineer", "ml engineer"]
        location = "San Francisco, CA"

        for keyword in keywords:
            try:
                params = {
                    "q": keyword,
                    "l": location,
                    "sort": "date"
                }

                response = self.session.get(self.base_url, params=params, timeout=config.SCRAPE_TIMEOUT)
                response.raise_for_status()

                soup = BeautifulSoup(response.content, "html.parser")

                # Find job cards
                job_cards = soup.find_all("div", class_="job_seen_beacon")

                for card in job_cards[:15]:  # Limit per keyword
                    try:
                        title_elem = card.find("h2", class_="jobTitle")
                        company_elem = card.find("span", class_="companyName")
                        location_elem = card.find("div", class_="companyLocation")

                        if title_elem and company_elem:
                            title_link = title_elem.find("a")
                            if title_link:
                                job_id = title_link.get("data-jk", "")
                                title = title_link.get_text(strip=True)
                                url = f"https://www.indeed.com/viewjob?jk={job_id}"

                                jobs.append({
                                    "id": self.generate_job_id(url),
                                    "board_name": self.board_name,
                                    "title": title,
                                    "company": company_elem.get_text(strip=True),
                                    "location": location_elem.get_text(strip=True) if location_elem else location,
                                    "url": url,
                                    "description": "",
                                    "posted_date": None,
                                    "scraped_date": datetime.now().isoformat()
                                })
                    except Exception as e:
                        print(f"Error parsing Indeed job card: {e}")
                        continue

                self.sleep()

            except Exception as e:
                print(f"Indeed scraping error for '{keyword}': {e}")

        return jobs


class AngelListScraper(BaseScraper):
    """Scrape Wellfound (AngelList) jobs."""

    def __init__(self):
        super().__init__("Wellfound")
        self.base_url = "https://wellfound.com/jobs"

    def scrape(self) -> List[Dict]:
        """Scrape AngelList/Wellfound jobs."""
        jobs = []

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                url = f"{self.base_url}?role=l-machine-learning&location=San Francisco"
                page.goto(url, wait_until="networkidle", timeout=config.SCRAPE_TIMEOUT * 1000)
                time.sleep(3)

                # Scroll to load more jobs
                for _ in range(3):
                    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(2)

                # Extract job listings
                job_elements = page.query_selector_all("[data-test='JobSearchCard']")

                for elem in job_elements[:20]:
                    try:
                        title = elem.query_selector("[data-test='JobSearchCardTitle']")
                        company = elem.query_selector("[data-test='CompanyName']")
                        location = elem.query_selector("[data-test='JobSearchCardLocation']")
                        link = elem.query_selector("a")

                        if title and company and link:
                            url = "https://wellfound.com" + link.get_attribute("href")

                            jobs.append({
                                "id": self.generate_job_id(url),
                                "board_name": self.board_name,
                                "title": title.inner_text().strip(),
                                "company": company.inner_text().strip(),
                                "location": location.inner_text().strip() if location else "San Francisco, CA",
                                "url": url,
                                "description": "",
                                "posted_date": None,
                                "scraped_date": datetime.now().isoformat()
                            })
                    except Exception as e:
                        print(f"Error parsing Wellfound job: {e}")
                        continue

                browser.close()

        except Exception as e:
            print(f"Wellfound scraping error: {e}")

        return jobs


class YCombinatorScraper(BaseScraper):
    """Scrape Y Combinator Work at a Startup."""

    def __init__(self):
        super().__init__("Y Combinator")
        self.base_url = "https://www.ycombinator.com/jobs"

    def scrape(self) -> List[Dict]:
        """Scrape YC jobs."""
        jobs = []

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                # YC job search for ML roles in SF
                url = f"{self.base_url}?query=machine%20learning&location=San%20Francisco"
                page.goto(url, wait_until="domcontentloaded", timeout=config.SCRAPE_TIMEOUT * 1000)
                time.sleep(3)

                # Extract job listings
                job_links = page.query_selector_all("a[href^='/companies/']")

                for link in job_links[:15]:
                    try:
                        # Get job details from the link context
                        parent = link.evaluate_handle("element => element.closest('div')")
                        text_content = link.inner_text()

                        # Parse company and role
                        href = link.get_attribute("href")
                        url = f"https://www.ycombinator.com{href}"

                        # Extract title and company from context
                        # YC structure may vary, this is a basic extraction
                        parts = text_content.split("\n")
                        title = parts[0] if parts else "ML Engineer"
                        company = parts[1] if len(parts) > 1 else "YC Company"

                        jobs.append({
                            "id": self.generate_job_id(url),
                            "board_name": self.board_name,
                            "title": title,
                            "company": company,
                            "location": "San Francisco, CA",
                            "url": url,
                            "description": "",
                            "posted_date": None,
                            "scraped_date": datetime.now().isoformat()
                        })
                    except Exception as e:
                        print(f"Error parsing YC job: {e}")
                        continue

                browser.close()

        except Exception as e:
            print(f"YC scraping error: {e}")

        return jobs


class CompanyCareersPageScraper(BaseScraper):
    """Scrape career pages of specific AI companies."""

    COMPANIES = {
        "openai": {
            "name": "OpenAI",
            "url": "https://openai.com/careers/search",
            "selectors": {
                "job_card": ".job-listing",
                "title": ".job-title",
                "location": ".job-location"
            }
        },
        "anthropic": {
            "name": "Anthropic",
            "url": "https://www.anthropic.com/careers",
            "selectors": {
                "job_card": "[class*='job']",
                "title": "h3, h4",
                "location": "[class*='location']"
            }
        }
    }

    def __init__(self, company_key: str):
        if company_key not in self.COMPANIES:
            raise ValueError(f"Unknown company: {company_key}")

        self.company_config = self.COMPANIES[company_key]
        super().__init__(self.company_config["name"])

    def scrape(self) -> List[Dict]:
        """Scrape company careers page."""
        jobs = []

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                page.goto(self.company_config["url"], wait_until="domcontentloaded",
                         timeout=config.SCRAPE_TIMEOUT * 1000)
                time.sleep(3)

                # Try to find job listings using configured selectors
                job_elements = page.query_selector_all("a[href*='job'], a[href*='career'], a[href*='position']")

                for elem in job_elements[:10]:
                    try:
                        text = elem.inner_text().strip()
                        href = elem.get_attribute("href")

                        # Filter for ML/AI related roles in SF
                        if any(keyword in text.lower() for keyword in ["machine learning", "ml", "ai", "engineer", "scientist"]):
                            url = href if href.startswith("http") else f"https://www.{self.board_name.lower().replace(' ', '')}.com{href}"

                            jobs.append({
                                "id": self.generate_job_id(url),
                                "board_name": self.board_name,
                                "title": text,
                                "company": self.board_name,
                                "location": "San Francisco, CA",
                                "url": url,
                                "description": "",
                                "posted_date": None,
                                "scraped_date": datetime.now().isoformat()
                            })
                    except Exception as e:
                        print(f"Error parsing {self.board_name} job: {e}")
                        continue

                browser.close()

        except Exception as e:
            print(f"{self.board_name} scraping error: {e}")

        return jobs


class HackerNewsWhoIsHiringScraper(BaseScraper):
    """Scrape Hacker News 'Who is Hiring' monthly threads."""

    def __init__(self):
        super().__init__("HN Who is Hiring")
        self.api_base = "https://hacker-news.firebaseio.com/v0"
        self.ml_keywords = [
            "machine learning", "ml engineer", "ai engineer", "deep learning",
            "data scientist", "nlp", "computer vision", "pytorch", "tensorflow",
            "llm", "gpt", "transformers", "neural network", "mlops",
            "research scientist", "applied scientist", "ai/ml", "ml/ai"
        ]

    def scrape(self) -> List[Dict]:
        """Scrape the latest Who is Hiring thread for ML/AI jobs."""
        jobs = []

        try:
            # Search for the latest "Who is hiring" post using Algolia HN API
            search_url = "https://hn.algolia.com/api/v1/search_by_date"
            params = {
                "query": "Ask HN: Who is hiring",
                "tags": "story",
                "numericFilters": "created_at_i>{}".format(
                    int(time.time()) - 60 * 24 * 60 * 60  # Last 60 days
                )
            }

            response = self.session.get(search_url, params=params, timeout=config.SCRAPE_TIMEOUT)
            response.raise_for_status()
            data = response.json()

            # Find the most recent "Who is hiring" post
            hiring_post = None
            for hit in data.get("hits", []):
                title = hit.get("title", "").lower()
                if "who is hiring" in title and "ask hn" in title:
                    hiring_post = hit
                    break

            if not hiring_post:
                print("  No recent 'Who is Hiring' post found")
                return jobs

            post_id = hiring_post["objectID"]
            post_title = hiring_post.get("title", "")
            print(f"  Found: {post_title}")

            # Get all comments (job postings) from this thread
            item_url = f"{self.api_base}/item/{post_id}.json"
            response = self.session.get(item_url, timeout=config.SCRAPE_TIMEOUT)
            response.raise_for_status()
            post_data = response.json()

            comment_ids = post_data.get("kids", [])[:150]  # Limit to first 150 comments
            print(f"  Processing {len(comment_ids)} job postings...")

            for comment_id in comment_ids:
                try:
                    time.sleep(0.5)  # HN API is generous, use shorter delay
                    comment_url = f"{self.api_base}/item/{comment_id}.json"
                    resp = self.session.get(comment_url, timeout=config.SCRAPE_TIMEOUT)
                    resp.raise_for_status()
                    comment = resp.json()

                    if not comment or comment.get("deleted") or comment.get("dead"):
                        continue

                    text = comment.get("text", "")
                    if not text:
                        continue

                    text_lower = text.lower()

                    # Filter for ML/AI jobs
                    if not any(kw in text_lower for kw in self.ml_keywords):
                        continue

                    # Parse the job posting
                    job_info = self._parse_hn_job(text, comment_id)
                    if job_info:
                        jobs.append(job_info)

                except Exception as e:
                    continue

            print(f"  Found {len(jobs)} ML/AI jobs")

        except Exception as e:
            print(f"HN Who is Hiring scraping error: {e}")

        return jobs

    def _parse_hn_job(self, text: str, comment_id: int) -> Optional[Dict]:
        """Parse a HN job posting comment into structured data."""
        import re
        from html import unescape

        # Clean HTML
        text_clean = unescape(text)
        text_clean = re.sub(r'<[^>]+>', ' ', text_clean)
        text_clean = re.sub(r'\s+', ' ', text_clean).strip()

        # Extract company name (usually first line or starts with company name)
        lines = text_clean.split('|')
        company = "Unknown"
        title = "ML/AI Role"
        location = ""

        if lines:
            # First part often has: Company | Location | Role | ...
            first_part = lines[0].strip()
            company = first_part[:50] if first_part else "Unknown"

            for part in lines[1:4]:
                part = part.strip().lower()
                if any(loc in part for loc in ["remote", "sf", "nyc", "london", "san francisco",
                                                 "new york", "bay area", "onsite", "hybrid"]):
                    location = part.title()
                elif any(role in part for role in ["engineer", "scientist", "researcher", "ml", "ai", "data"]):
                    title = part.title()[:60]

        # Try to extract a more specific title from the text
        title_patterns = [
            r'((?:senior |sr\.? |staff |principal |lead )?(?:machine learning|ml|ai|data|research|applied) (?:engineer|scientist|researcher))',
            r'((?:senior |sr\.? |staff )?(?:software engineer)(?:,? (?:ml|ai|machine learning)))',
        ]
        for pattern in title_patterns:
            match = re.search(pattern, text_clean.lower())
            if match:
                title = match.group(1).title()
                break

        url = f"https://news.ycombinator.com/item?id={comment_id}"

        return {
            "id": self.generate_job_id(url),
            "board_name": self.board_name,
            "title": title[:100],
            "company": company[:100],
            "location": location[:100] if location else "Remote/Various",
            "url": url,
            "description": text_clean[:2000],
            "posted_date": None,
            "scraped_date": datetime.now().isoformat()
        }


class RedditMLJobsScraper(BaseScraper):
    """Scrape Reddit for ML/AI job postings."""

    def __init__(self):
        super().__init__("Reddit ML Jobs")
        self.subreddits = [
            "MachineLearning",  # Weekly job threads
            "MLjobs",           # Dedicated ML job board
            "DataScienceJobs",  # Data science jobs
        ]
        self.ml_keywords = [
            "machine learning", "ml engineer", "ai engineer", "deep learning",
            "data scientist", "nlp", "computer vision", "pytorch", "tensorflow",
            "llm", "research scientist", "applied scientist", "mlops"
        ]

    def scrape(self) -> List[Dict]:
        """Scrape Reddit for ML/AI jobs."""
        jobs = []

        for subreddit in self.subreddits:
            try:
                subreddit_jobs = self._scrape_subreddit(subreddit)
                jobs.extend(subreddit_jobs)
                print(f"    r/{subreddit}: {len(subreddit_jobs)} jobs")
                self.sleep()
            except Exception as e:
                print(f"    Error scraping r/{subreddit}: {e}")
                continue

        return jobs

    def _scrape_subreddit(self, subreddit: str) -> List[Dict]:
        """Scrape a single subreddit for job postings."""
        jobs = []

        # Reddit JSON API (no auth needed for public subreddits)
        url = f"https://www.reddit.com/r/{subreddit}/new.json?limit=100"
        headers = {"User-Agent": "NeilSearch/1.0 Job Aggregator"}

        try:
            response = self.session.get(url, headers=headers, timeout=config.SCRAPE_TIMEOUT)
            response.raise_for_status()
            data = response.json()

            posts = data.get("data", {}).get("children", [])

            for post in posts:
                post_data = post.get("data", {})

                title = post_data.get("title", "")
                selftext = post_data.get("selftext", "")
                link_flair = (post_data.get("link_flair_text") or "").lower()
                full_text = f"{title} {selftext}".lower()

                # Filter for actual job posts (not discussions)
                # Strong hiring indicators
                is_hiring = (
                    "[hiring]" in title.lower() or
                    "hiring" in link_flair or
                    "job" in link_flair or
                    any(phrase in full_text for phrase in [
                        "we are hiring", "we're hiring", "now hiring",
                        "job opening", "open position", "apply here",
                        "join our team", "looking to hire", "seeking",
                        "come work with us", "job opportunity"
                    ])
                )

                # Must have ML/AI keywords
                has_ml = any(kw in full_text for kw in self.ml_keywords)

                # Exclude discussion posts
                is_discussion = any(phrase in full_text for phrase in [
                    "interview question", "interview experience", "how to",
                    "what is the", "can someone explain", "eli5",
                    "looking for advice", "career advice", "should i"
                ])

                if not (is_hiring and has_ml) or is_discussion:
                    continue

                # Parse the job posting
                job_info = self._parse_reddit_job(post_data, subreddit)
                if job_info:
                    jobs.append(job_info)

        except Exception as e:
            print(f"Error fetching r/{subreddit}: {e}")

        return jobs

    def _parse_reddit_job(self, post_data: Dict, subreddit: str) -> Optional[Dict]:
        """Parse a Reddit post into structured job data."""
        import re

        title = post_data.get("title", "")
        selftext = post_data.get("selftext", "")
        permalink = post_data.get("permalink", "")
        created_utc = post_data.get("created_utc", 0)

        # Extract company name from title (often in brackets or first part)
        company = "Unknown"
        job_title = title

        # Common patterns: [Company] Title, Company - Title, Company | Title
        patterns = [
            r'\[([^\]]+)\]\s*(.+)',           # [Company] Title
            r'\(([^)]+)\)\s*(.+)',             # (Company) Title
            r'^([^|\-–]+?)\s*[|\-–]\s*(.+)',   # Company | Title or Company - Title
        ]

        for pattern in patterns:
            match = re.match(pattern, title)
            if match:
                company = match.group(1).strip()[:100]
                job_title = match.group(2).strip()[:100]
                break

        # Extract location from title or body
        location = ""
        location_patterns = [
            r'\b(remote)\b',
            r'\b(san francisco|sf|bay area)\b',
            r'\b(new york|nyc|ny)\b',
            r'\b(london|uk)\b',
            r'\b(seattle|wa)\b',
            r'\b(austin|tx)\b',
            r'\b(boston|ma)\b',
        ]

        full_text = f"{title} {selftext}".lower()
        for pattern in location_patterns:
            match = re.search(pattern, full_text, re.IGNORECASE)
            if match:
                location = match.group(1).title()
                break

        url = f"https://www.reddit.com{permalink}"
        posted_date = datetime.fromtimestamp(created_utc).isoformat() if created_utc else None

        return {
            "id": self.generate_job_id(url),
            "board_name": f"Reddit r/{subreddit}",
            "title": job_title[:100],
            "company": company[:100],
            "location": location if location else "Remote/Various",
            "url": url,
            "description": selftext[:2000] if selftext else title,
            "posted_date": posted_date,
            "scraped_date": datetime.now().isoformat()
        }


class ScraperManager:
    """Manage all job board scrapers."""

    def __init__(self):
        self.scrapers = self._initialize_scrapers()

    def _initialize_scrapers(self) -> List[BaseScraper]:
        """Initialize all enabled scrapers."""
        scrapers = []

        # Add main scrapers
        scrapers.append(IndeedScraper())
        scrapers.append(LinkedInScraper())
        scrapers.append(AngelListScraper())
        scrapers.append(YCombinatorScraper())
        scrapers.append(HackerNewsWhoIsHiringScraper())
        scrapers.append(RedditMLJobsScraper())

        # Add company-specific scrapers
        for company_key in ["openai", "anthropic"]:
            try:
                scrapers.append(CompanyCareersPageScraper(company_key))
            except Exception as e:
                print(f"Failed to initialize {company_key} scraper: {e}")

        return scrapers

    def scrape_all(self, board_names: Optional[List[str]] = None) -> List[Dict]:
        """
        Scrape all enabled boards or specific boards if provided.

        Args:
            board_names: Optional list of board names to scrape

        Returns:
            List of all jobs found
        """
        all_jobs = []

        scrapers_to_run = self.scrapers
        if board_names:
            scrapers_to_run = [s for s in self.scrapers if s.board_name.lower() in [n.lower() for n in board_names]]

        for scraper in scrapers_to_run:
            print(f"Scraping {scraper.board_name}...")
            try:
                jobs = scraper.scrape()
                all_jobs.extend(jobs)
                print(f"  Found {len(jobs)} jobs from {scraper.board_name}")
            except Exception as e:
                print(f"  Error scraping {scraper.board_name}: {e}")
                continue

        return all_jobs
