# NeilSearch - AI/ML Job Matching Tool Specification

## Overview
A command-line tool that scans top AI/ML job boards, matches jobs against a candidate's resume, ranks them by match quality, and presents results in a simple HTML dashboard.

## Core Requirements

### 1. Resume Processing
- **Input**: PDF or DOCX resume file
- **Processing**: Extract text content including:
  - Technical skills (programming languages, ML frameworks, tools)
  - Experience level and years
  - Role types and responsibilities from past positions
  - Education and certifications
  - Preferred company traits (if mentioned)
- **Output**: Structured profile with extracted information for matching

### 2. Job Board Coverage
Target the top 30 AI/ML job boards focusing on San Francisco. Priority boards include:

**High Priority (API-friendly or reliable scraping):**
1. LinkedIn Jobs
2. Indeed
3. Glassdoor
4. AngelList/Wellfound (startup jobs)
5. Y Combinator Work at a Startup
6. AI Jobs Board (ai-jobs.net)
7. Remote AI Jobs
8. Hugging Face Jobs
9. OpenAI Careers
10. Anthropic Careers

**Medium Priority:**
11. Google Careers
12. Meta Careers
13. Microsoft Careers
14. Amazon Jobs
15. Apple Jobs
16. Kaggle Jobs
17. MLOps Community Jobs
18. builtin.com (SF tech jobs)
19. hired.com
20. dice.com

**Lower Priority (backup sources):**
21. ZipRecruiter
22. Monster
23. SimplyHired
24. Crunchboard
25. techjobsasia.com (AI section)
26. otta.com
27. cord.co
28. techstars.com/jobs
29. toptal.com
30. gun.io

**Collection Strategy:**
- Use official APIs where available (LinkedIn, Indeed, etc.)
- Use browser automation (Playwright/Selenium) for sites without APIs
- Implement polite rate limiting (respect robots.txt, add delays)
- Handle CAPTCHAs and blocks gracefully (skip and log)
- Retry failed requests with exponential backoff

### 3. Matching Algorithm

**Scoring System (0-100):**

**Skills Match (40 points)**
- Required skills present: +8 points each (up to 40)
- Nice-to-have skills: +4 points each
- Missing critical skills: -5 points each
- Deduct for skills significantly beyond candidate level

**Role Fit (30 points)**
- Responsibilities align with past experience: +30 points
- Partial alignment: +15-25 points
- Poor alignment: +0-10 points
- Consider: IC vs management, research vs engineering, product focus

**Company Traits (20 points)**
- Company size matches preference: +10 points
- Company stage matches (startup/growth/enterprise): +5 points
- Industry/domain alignment: +5 points

**Experience Level (10 points)**
- Job seniority matches candidate: +10 points
- One level off: +5 points
- Mismatch: 0 points

**Location Bonus:**
- San Francisco proper: +5 bonus points
- Bay Area: +3 bonus points
- Remote: +2 bonus points

**Output for each job:**
- Overall score (0-100)
- Breakdown by category
- Matched skills (green highlighting)
- Missing required skills (red highlighting)
- Match explanation (2-3 sentences)

### 4. Dashboard Requirements

**Technology:**
- Static HTML/CSS/JavaScript (no server required)
- Single page application
- Works by opening HTML file in browser

**Features:**

**Main View:**
- Job cards showing:
  - Company name and logo (if available)
  - Job title
  - Match score (with color coding: >80=green, 60-80=yellow, <60=gray)
  - Location
  - Date posted
  - Quick match summary
  - Application status badge

**Filtering:**
- Score range slider (e.g., "Show only >70")
- Company size filter (startup/mid/enterprise)
- Date posted (last 24h, 7d, 14d, 30d)
- Application status (not applied, applied, interviewing, rejected, archived)
- Location filter

**Sorting:**
- By match score (default, descending)
- By date posted (newest first)
- By company name (alphabetical)

**Detailed View (click to expand):**
- Full job description
- Complete match breakdown with scores
- Matched skills highlighted in green
- Missing required skills in red
- Application notes textarea
- Status update dropdown
- Direct link to job posting

**Analytics Section:**
- Total jobs found
- Average match score
- Top 5 most in-demand skills
- Companies hiring most actively
- Line chart: jobs posted over time (last 30 days)
- Bar chart: jobs by company size

**Application Tracking:**
- Mark jobs as: "Applied", "Interviewing", "Offer", "Rejected", "Not Interested"
- Add notes to each job
- Track application date
- Filter/hide jobs by status

### 5. Data Storage

**Format:** SQLite database (simple, file-based, no server)

**Schema:**

```sql
-- Jobs table
CREATE TABLE jobs (
    id TEXT PRIMARY KEY,  -- unique hash of (board_name + job_url)
    board_name TEXT,
    company TEXT,
    title TEXT,
    location TEXT,
    description TEXT,
    url TEXT UNIQUE,
    posted_date TEXT,
    scraped_date TEXT,
    match_score REAL,
    match_breakdown TEXT,  -- JSON
    skills_matched TEXT,    -- JSON array
    skills_missing TEXT,    -- JSON array
    match_explanation TEXT
);

-- Application tracking
CREATE TABLE applications (
    job_id TEXT PRIMARY KEY,
    status TEXT,  -- applied, interviewing, offer, rejected, not_interested
    notes TEXT,
    status_date TEXT,
    FOREIGN KEY(job_id) REFERENCES jobs(id)
);

-- Profile (stores extracted resume data)
CREATE TABLE profile (
    id INTEGER PRIMARY KEY,
    resume_path TEXT,
    last_updated TEXT,
    profile_data TEXT  -- JSON with skills, experience, preferences
);

-- Scan history
CREATE TABLE scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_date TEXT,
    jobs_found INTEGER,
    boards_scanned INTEGER,
    duration_seconds REAL
);
```

**Data Retention:**
- Automatically delete jobs older than 30 days
- Keep application tracking indefinitely
- Keep scan history for analytics

### 6. Command-Line Interface

**Installation:**
```bash
# Setup (one-time)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
playwright install chromium  # for browser automation
```

**Commands:**

```bash
# Parse resume and create/update profile
python neilsearch.py profile --resume path/to/resume.pdf

# Run a scan
python neilsearch.py scan

# Run scan for specific boards only
python neilsearch.py scan --boards linkedin,indeed,angellist

# Open dashboard
python neilsearch.py dashboard

# Show quick summary in terminal
python neilsearch.py summary

# Clean old jobs (>30 days)
python neilsearch.py clean

# Export results to CSV
python neilsearch.py export --output jobs.csv
```

**Expected Output:**
```
Starting scan...
[1/30] LinkedIn: Found 24 jobs
[2/30] Indeed: Found 18 jobs
[3/30] Glassdoor: Rate limited, waiting...
[4/30] AngelList: Found 31 jobs
...
[30/30] gun.io: Found 3 jobs

Scan complete!
Total jobs found: 247
New jobs: 89
Duplicate jobs removed: 158
Match scores calculated: 89
Average match score: 67.3

Top matches:
1. [94] Senior ML Engineer - Anthropic (SF)
2. [91] AI Research Scientist - OpenAI (SF)
3. [88] ML Platform Engineer - Scale AI (SF)
4. [87] Applied ML Engineer - Cursor (Remote)
5. [85] AI Engineer - Replit (SF)

Opening dashboard...
```

## Technical Stack

**Core Dependencies:**
- Python 3.10+
- PyPDF2 / pdfplumber - PDF parsing
- python-docx - DOCX parsing
- spacy / transformers - NLP for skill extraction
- playwright - Browser automation
- beautifulsoup4 - HTML parsing
- requests - HTTP requests
- sqlite3 - Database (built-in)
- jinja2 - HTML template generation

**Dashboard:**
- Pure HTML/CSS/JavaScript
- Chart.js - Charts and graphs
- No framework needed (vanilla JS sufficient)

## Implementation Phases

### Phase 1: Foundation
- Resume parser
- Profile extraction (skills, experience)
- Database setup
- Basic CLI structure

### Phase 2: Job Collection
- Implement scrapers for top 10 boards
- Rate limiting and error handling
- Deduplication logic
- Store raw job data

### Phase 3: Matching Engine
- Implement scoring algorithm
- Skill matching logic
- Role and company trait matching
- Generate match explanations

### Phase 4: Dashboard
- Generate HTML dashboard from data
- Job cards with filtering/sorting
- Detailed view modal
- Application status tracking

### Phase 5: Analytics & Polish
- Historical trends charts
- Export functionality
- Data cleanup automation
- Error reporting and logs

## Key Design Decisions

1. **Static Dashboard**: HTML file generated from data, no web server needed. Simple for non-technical users.

2. **Browser Automation**: Use Playwright instead of just requests/BeautifulSoup for better success rate with modern sites.

3. **Intelligent Deduplication**: Hash job postings by (normalized_title + company + location) to catch duplicates across boards.

4. **Offline-First**: All data stored locally. No external services or API keys required (except for job boards that need them).

5. **Fail Gracefully**: If a board fails, log it and continue. Don't let one broken scraper kill the whole scan.

6. **Resume Privacy**: Resume never leaves the local machine. All processing is local.

## Success Metrics

- Successfully scan at least 25 of 30 target boards per run
- Find at least 50 relevant AI/ML jobs in SF per scan
- Match scores correlate with user's manual assessment (validate with first 20 jobs)
- Dashboard loads in <2 seconds even with 500+ jobs
- Complete scan in <10 minutes
- Zero crashes or data corruption

## Future Enhancements (Out of Scope for V1)

- Email/Slack notifications for high-match jobs
- Automatic application submission
- Integration with ATS systems
- Mobile app
- Cover letter generation
- Interview prep suggestions based on job requirements
- Salary data scraping and comparison
