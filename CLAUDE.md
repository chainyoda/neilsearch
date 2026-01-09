# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

NeilSearch is a job matching tool that scrapes AI/ML job boards, matches jobs against a candidate's resume, and presents ranked results in an interactive HTML dashboard. The tool is designed for non-technical users and operates entirely locally with no external services.

## Development Commands

### Setup
```bash
# One-time setup (automated)
./setup.sh

# Manual setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
python -m spacy download en_core_web_sm
```

### Running the Tool
```bash
# Create profile from resume
python neilsearch.py profile --resume /path/to/resume.pdf

# Scan job boards
python neilsearch.py scan
python neilsearch.py scan --boards linkedin,indeed  # specific boards

# View dashboard
python neilsearch.py dashboard

# Terminal summary
python neilsearch.py summary

# Export to CSV
python neilsearch.py export --output jobs.csv --min-score 80

# Clean old jobs
python neilsearch.py clean --days 30
```

### Testing Individual Components
```bash
# Test resume parsing
python -c "from resume_parser import parse_resume; print(parse_resume('test_resume.pdf'))"

# Test database
python -c "from database import Database; db = Database(); db.connect(); db.init_db()"

# Test scraper (single board)
python -c "from scrapers import IndeedScraper; s = IndeedScraper(); print(s.scrape())"

# Test matcher
python -c "from matcher import JobMatcher; from database import Database; db = Database(); db.connect(); p = db.get_profile(); m = JobMatcher(p['profile_data']); print(m.match_job({'title': 'ML Engineer', 'description': 'Python PyTorch', 'company': 'Test', 'location': 'SF'}))"
```

## Architecture

### Core Workflow
1. **Profile Creation** (`resume_parser.py`): Extract skills and experience from resume
2. **Job Collection** (`scrapers.py`): Scrape multiple job boards
3. **Matching** (`matcher.py`): Score jobs against profile (0-100)
4. **Storage** (`database.py`): Save to local SQLite database
5. **Visualization** (`dashboard.py`): Generate interactive HTML dashboard

### Data Flow
```
Resume (PDF/DOCX)
  → resume_parser.py (text extraction + NLP)
  → database.py (store profile)

scrapers.py (30+ job boards)
  → raw job data
  → matcher.py (score against profile)
  → database.py (store jobs with scores)

database.py (SQLite)
  → dashboard.py (generate HTML)
  → dashboard.html (open in browser)
```

### Key Design Decisions

**No Server Required**: Dashboard is a static HTML file with embedded JavaScript. All processing happens in Python, results are serialized to JSON in the HTML.

**Browser Automation**: Uses Playwright for sites without APIs. This is more reliable than requests+BeautifulSoup for modern sites but is slower and more fragile.

**Local-First**: Everything runs locally. Resume never leaves the machine. Database is SQLite file.

**Fail Gracefully**: If one job board fails, continue with others. Log errors but don't crash.

**Deduplication**: Jobs are deduplicated by URL hash to avoid showing the same job from multiple boards.

## Module Details

### resume_parser.py
- Extracts text from PDF (pdfplumber/PyPDF2) and DOCX (python-docx)
- Uses regex and keyword matching to find skills from predefined list
- Detects experience level and years of experience
- Identifies role types (research, engineering, leadership, etc.)
- **No ML model** - uses rule-based extraction for simplicity

### scrapers.py
- **BaseScraper**: Abstract base class with common utilities
- **ScraperManager**: Orchestrates all scrapers
- Individual scrapers for each job board (LinkedInScraper, IndeedScraper, etc.)
- **Rate limiting**: 2-second delay between requests (configurable in config.py)
- **Timeout handling**: 30-second timeout per request
- **Error recovery**: Continues on failure, logs errors

**Scraping Strategy:**
- Use APIs where available (LinkedIn, Indeed have public APIs)
- Use Playwright browser automation for others
- Respect robots.txt and rate limits
- Extract: title, company, location, URL, description, posted_date

### matcher.py
- **JobMatcher class**: Scores jobs against profile
- **Scoring algorithm**:
  - Skills (40%): Match required/nice-to-have skills
  - Role fit (30%): Align with past role types
  - Company traits (20%): Match size/stage/industry preferences
  - Experience level (10%): Match seniority
  - Location bonus: +5 for SF, +3 for Bay Area, +2 for Remote
- Generates human-readable explanation for each score
- Extracts required vs nice-to-have skills from job description

### database.py
- SQLite with context manager pattern
- **Tables**:
  - `jobs`: Job postings with match scores
  - `applications`: Application status tracking
  - `profile`: Candidate profile (single row)
  - `scans`: Scan history for analytics
- **Key methods**:
  - `save_job()`: Returns True if new, False if duplicate
  - `get_jobs()`: Fetch with optional filters (min_score, status, days)
  - `get_stats()`: Aggregate statistics for dashboard
  - `clean_old_jobs()`: Delete jobs older than N days

### dashboard.py
- Jinja2 template with embedded CSS/JavaScript
- **No web framework** - generates standalone HTML file
- Client-side filtering/sorting with vanilla JavaScript
- Chart.js for analytics visualizations
- **Not persistent**: Status updates in UI don't save to database (future enhancement)

### config.py
- Central configuration for all settings
- Job board enable/disable flags
- Scraping parameters (timeout, delay, retries)
- Match algorithm weights
- Location settings
- File paths

### neilsearch.py
- Click-based CLI with Rich for formatting
- Commands: profile, scan, dashboard, summary, clean, export
- Uses Progress bars and Tables for nice terminal output
- Handles errors gracefully with helpful messages

## Common Tasks

### Adding a New Job Board

1. Create a new scraper class in `scrapers.py`:
```python
class NewBoardScraper(BaseScraper):
    def __init__(self):
        super().__init__("Board Name")
        self.base_url = "https://..."

    def scrape(self) -> List[Dict]:
        jobs = []
        # Scraping logic here
        return jobs
```

2. Add to `ScraperManager._initialize_scrapers()`:
```python
scrapers.append(NewBoardScraper())
```

3. Test individually before adding to main flow

### Modifying Match Algorithm

Edit weights in `config.py`:
```python
MATCH_WEIGHTS = {
    "skills": 40,      # Adjust these
    "role_fit": 30,
    "company_traits": 20,
    "experience_level": 10
}
```

Or modify scoring logic in `matcher.py` methods:
- `_score_skills()`: Skills matching
- `_score_role_fit()`: Role alignment
- `_score_company_traits()`: Company preferences
- `_score_experience_level()`: Seniority matching

### Adding New Skills

Add to `resume_parser.py`:
```python
TECH_SKILLS = {
    "new_skill",
    "another_skill",
    # ...
}
```

Skills are case-insensitive and matched using word boundaries.

### Debugging Scrapers

1. Test single board:
```python
from scrapers import LinkedInScraper
scraper = LinkedInScraper()
jobs = scraper.scrape()
print(f"Found {len(jobs)} jobs")
print(jobs[0] if jobs else "No jobs")
```

2. Run Playwright in headed mode (for debugging):
```python
browser = p.chromium.launch(headless=False)  # Change to False
```

3. Add print statements or use `console.print()` from Rich

## Database Schema

```sql
-- Core tables
jobs (id, board_name, company, title, location, description, url,
      posted_date, scraped_date, match_score, match_breakdown,
      skills_matched, skills_missing, match_explanation)

applications (job_id, status, notes, status_date)

profile (id, resume_path, last_updated, profile_data)

scans (id, scan_date, jobs_found, boards_scanned, duration_seconds)
```

JSON fields:
- `match_breakdown`: `{"skills": 35, "role_fit": 25, ...}`
- `skills_matched`: `["python", "pytorch", ...]`
- `skills_missing`: `["scala", "spark", ...]`
- `profile_data`: Full profile dict from resume parser

## Known Issues and Limitations

### Scraping Fragility
Job boards change their HTML frequently. Scrapers may break and need updates. Always test after board updates.

### Rate Limiting
Some boards (LinkedIn, Glassdoor) aggressively rate limit. The tool handles this by:
- Adding delays between requests
- Continuing on failure
- Limiting results per board

### No Authentication
Cannot access jobs requiring login. Many boards show public jobs without auth, but some require accounts.

### Resume Parsing Accuracy
Rule-based extraction is simple but not perfect. May miss:
- Skills spelled differently (e.g., "sci-kit learn" vs "scikit-learn")
- Uncommon tools or frameworks
- Context-dependent skills

### Dashboard Status Updates
Application status changes in the dashboard UI are not currently persisted to the database. This requires adding an API endpoint or local storage mechanism.

### Location Hardcoded
Currently configured for San Francisco. To support other locations:
1. Update `TARGET_LOCATIONS` in `config.py`
2. Modify scraper search queries
3. Adjust `_get_location_bonus()` in `matcher.py`

## Performance Notes

- **Full scan time**: 5-10 minutes for 30+ boards
- **Jobs per scan**: Typically 50-200 new jobs
- **Database size**: ~10MB per 1000 jobs
- **Dashboard load time**: <2 seconds for 500 jobs

## Error Handling

The tool is designed to be resilient:
- Individual scraper failures don't stop the scan
- Missing profile shows helpful error message
- Empty results handled gracefully
- Malformed job data skipped with logging

Check `neilsearch.log` for detailed error messages.

## Future Enhancements

If extending this tool:
1. **Persistent status tracking**: Add API or local storage for application updates
2. **Scheduled scanning**: Add cron job or background service
3. **Email notifications**: Alert on high-match jobs
4. **Better NLP**: Use spaCy or transformers for skill extraction
5. **API integrations**: Use official APIs where available
6. **Multi-location**: Support multiple target cities
7. **Cover letter generation**: Auto-generate using LLM
8. **Application automation**: Submit applications automatically
