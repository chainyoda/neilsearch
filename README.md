# NeilSearch

An intelligent job matching tool that scans AI/ML job boards, matches positions against your resume, and presents ranked results in an interactive dashboard.

## Features

- **Resume Parsing**: Automatically extracts skills, experience, and preferences from PDF/DOCX resumes
- **Multi-Board Scraping**: Collects jobs from 30+ top AI/ML job boards including LinkedIn, Indeed, Wellfound, YC, and company career pages
- **Smart Matching**: Scores jobs (0-100) based on skills, role fit, company traits, and experience level
- **Interactive Dashboard**: Beautiful HTML dashboard with filtering, sorting, and analytics
- **Application Tracking**: Track application status and notes for each job
- **Analytics**: View hiring trends, top companies, and skill demand

## Setup

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**

2. **Create and activate a virtual environment**

```bash
# Create virtual environment
python3 -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers** (required for web scraping)

```bash
playwright install chromium
```

5. **Download spaCy language model** (required for NLP)

```bash
python -m spacy download en_core_web_sm
```

## Usage

### 1. Create Your Profile

First, parse your resume to create a candidate profile:

```bash
python neilsearch.py profile --resume /path/to/your/resume.pdf
```

This will extract:
- Technical skills (Python, PyTorch, ML frameworks, etc.)
- Experience level (entry, mid, senior, management)
- Years of experience
- Role types and preferences

### 2. Scan for Jobs

Run a scan to find and match jobs:

```bash
python neilsearch.py scan
```

This will:
- Scrape multiple job boards for AI/ML positions in San Francisco
- Match each job against your profile
- Calculate match scores (0-100)
- Save results to the database

**Scan specific boards only:**

```bash
python neilsearch.py scan --boards linkedin,indeed,angellist
```

### 3. View Dashboard

Open the interactive dashboard:

```bash
python neilsearch.py dashboard
```

This generates an HTML file and opens it in your browser. The dashboard includes:
- Job cards with match scores
- Filtering by score, status, and keywords
- Sorting by score, date, or company
- Match explanations showing why jobs scored high/low
- Skills matching visualization
- Application status tracking
- Analytics charts

### 4. Quick Summary

View a terminal summary:

```bash
python neilsearch.py summary
```

Shows top matches, statistics, and hiring trends without opening the browser.

### 5. Export to CSV

Export job data to CSV:

```bash
python neilsearch.py export --output jobs.csv
```

Filter by minimum score:

```bash
python neilsearch.py export --output high-matches.csv --min-score 80
```

### 6. Clean Old Jobs

Remove jobs older than 30 days:

```bash
python neilsearch.py clean
```

Custom retention period:

```bash
python neilsearch.py clean --days 14
```

## Dashboard Features

### Filtering

- **Min Match Score**: Slider to show only jobs above a certain score
- **Search**: Text search across titles, companies, and skills
- **Application Status**: Filter by applied, interviewing, rejected, etc.
- **Sort**: By match score, date posted, or company name

### Job Cards

Each job card shows:
- Match score with color coding (green >80, yellow 60-80, gray <60)
- Company, title, and location
- Match explanation
- Matched skills (green tags)
- Missing skills (red tags)
- Detailed breakdown by category (skills, role fit, company, experience)

### Application Tracking

- Mark jobs as: Applied, Interviewing, Rejected, Not Interested
- Filter by status to focus on active opportunities
- Note: Status updates in the dashboard are currently demo-only

### Analytics

- **Top Hiring Companies**: Bar chart showing most active employers
- **Match Score Distribution**: Doughnut chart of low/medium/high matches
- Overall statistics and trends

## How Matching Works

Jobs are scored 0-100 based on four categories:

### Skills Match (40 points)
- Required skills present: +8 points each
- Nice-to-have skills: +4 points each
- Missing critical skills: -5 points each

### Role Fit (30 points)
- Alignment with past responsibilities and role types
- Research vs engineering vs applied ML vs leadership

### Company Traits (20 points)
- Company size match (startup, mid-size, enterprise)
- Company stage (early, growth, established)
- Industry alignment

### Experience Level (10 points)
- Seniority match (entry, mid, senior, management)
- Years of experience alignment

### Location Bonus (+5 max)
- San Francisco proper: +5
- Bay Area: +3
- Remote: +2

## Job Boards Covered

**Currently Implemented:**
1. LinkedIn
2. Indeed
3. Wellfound (AngelList)
4. Y Combinator Jobs
5. OpenAI Careers
6. Anthropic Careers
7. Google Careers
8. Meta Careers
9. And more...

The tool attempts comprehensive coverage but may skip boards with aggressive rate limiting or CAPTCHAs.

## File Structure

```
neilsearch/
├── neilsearch.py      # Main CLI interface
├── config.py          # Configuration settings
├── database.py        # Database operations
├── resume_parser.py   # Resume parsing and NLP
├── matcher.py         # Job matching algorithm
├── scrapers.py        # Job board scrapers
├── dashboard.py       # HTML dashboard generator
├── requirements.txt   # Python dependencies
├── neilsearch.db      # SQLite database (created on first run)
└── dashboard.html     # Generated dashboard (created when opened)
```

## Configuration

Edit `config.py` to customize:

- **Job boards**: Enable/disable specific boards
- **Target locations**: Add more locations beyond SF
- **Match weights**: Adjust scoring algorithm weights
- **Data retention**: Change how long jobs are kept
- **Scraping settings**: Adjust delays and timeouts

## Troubleshooting

### "No profile found" error
Run `python neilsearch.py profile --resume <path>` first to create your profile.

### No jobs found
- Some job boards may be temporarily blocking scraping
- Try running at different times of day
- Use `--boards` to target specific boards

### Playwright errors
Make sure you installed browsers: `playwright install chromium`

### Slow scanning
This is normal! Scraping 30+ job boards takes 5-10 minutes to be polite and avoid rate limits.

## Limitations

- **Scraping fragility**: Job boards frequently change their HTML structure
- **Rate limiting**: Some boards may temporarily block requests
- **No authentication**: Can't access jobs requiring login
- **Status tracking**: Application status updates are not persisted in current version
- **SF-focused**: Configured for San Francisco by default

## Future Enhancements

- Email notifications for high-match jobs
- Persistent application status tracking
- More sophisticated NLP for better skill extraction
- API integrations where available
- Broader location support
- Automatic re-scanning on a schedule

## Privacy

- All data stays on your local machine
- Resume content never leaves your computer
- No external services or tracking
- Database is a local SQLite file

## License

For personal use only.

## Support

If you encounter issues:
1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Try running with a single board first: `--boards indeed`
4. Check `neilsearch.log` for error details
