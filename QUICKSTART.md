# Quick Start Guide

Get NeilSearch running in 5 minutes!

## Step 1: Setup (One-time)

```bash
# Run the automated setup script
./setup.sh
```

Or manually:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
python -m spacy download en_core_web_sm
```

## Step 2: Create Your Profile

```bash
python neilsearch.py profile --resume /path/to/your/resume.pdf
```

This extracts your skills and experience from your resume.

## Step 3: Find Jobs

```bash
python neilsearch.py scan
```

This will:
- Scrape 30+ AI/ML job boards
- Match each job against your profile
- Calculate match scores (0-100)
- Takes 5-10 minutes

## Step 4: View Results

```bash
python neilsearch.py dashboard
```

Opens an interactive HTML dashboard in your browser showing:
- All jobs ranked by match score
- Skills matched/missing
- Filtering and sorting
- Analytics charts

## Tips

**See top matches quickly:**
```bash
python neilsearch.py summary
```

**Scan specific boards only:**
```bash
python neilsearch.py scan --boards linkedin,indeed
```

**Export to spreadsheet:**
```bash
python neilsearch.py export --output jobs.csv --min-score 70
```

**Re-scan periodically:**
Run `python neilsearch.py scan` daily or weekly to find new jobs.

## Dashboard Features

- **Filter by score**: Use the slider to show only high matches
- **Search**: Find jobs by keyword, company, or skill
- **Sort**: By match score, date, or company
- **Track status**: Mark jobs as applied, interviewing, etc.
- **View details**: Click "Details" to see full score breakdown

## Troubleshooting

**"No profile found"**: Run the profile command first

**No jobs found**: Some boards may be temporarily blocking. Try again later or use `--boards` to target specific ones.

**Slow scanning**: Normal! We're polite to job boards and wait between requests.

## What's Next?

- Update your resume and re-run the profile command
- Scan regularly to catch new postings
- Use filters to focus on best matches (>80 score)
- Track your applications in the dashboard

Happy job hunting!
