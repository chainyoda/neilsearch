# AI Company Scraping Guide

## Overview

This guide shows how to scrape AI/ML jobs directly from company career pages, which is more reliable than job aggregators (Indeed, LinkedIn) that often block automated requests.

## Why Company Career Pages?

### Advantages:
1. **No Rate Limiting**: Companies want you to see their jobs
2. **Public APIs**: Many use ATS (Applicant Tracking Systems) with public APIs
3. **Fresh Data**: Direct from the source, no delays
4. **Complete Information**: Full job descriptions, not truncated
5. **Legal**: Using public APIs is legitimate

### Disadvantages:
1. **More Scrapers**: Need individual scrapers per company
2. **API Changes**: Companies may change ATS providers
3. **Manual Maintenance**: Need to update when sites change

## Top 30 AI/ML Companies

We've identified 30 top AI companies organized by tier:

### Tier 1: Leading AI Labs (5 companies)
- OpenAI (Lever API)
- Anthropic (Greenhouse API)
- Google DeepMind
- Meta AI (FAIR)
- Google Brain/Research

### Tier 2: AI-First Startups (7 companies)
- Cohere (Lever API)
- Hugging Face
- Adept (Ashby API)
- Inflection AI (Lever API)
- Character.AI
- Perplexity AI (Greenhouse API)
- Replicate

### Tier 3: AI Tools & Platforms (5 companies)
- Scale AI (Greenhouse API)
- Databricks
- Weights & Biases (Greenhouse API)
- Anyscale (Lever API)
- Modal

### Tier 4: AI-Powered Products (6 companies)
- Notion (Greenhouse API)
- Cursor
- Replit (Lever API)
- Midjourney
- Runway (Greenhouse API)
- Stability AI

### Tier 5: Robotics & Applied AI (4 companies)
- Tesla AI
- Cruise
- Waymo
- Figure AI (Lever API)

### Tier 6: Enterprise AI (3 companies)
- Microsoft AI Research
- AWS AI/ML
- Snowflake

## ATS Systems & Their APIs

### Greenhouse API
**Companies**: Anthropic, Perplexity, Scale AI, Weights & Biases, Notion, Runway

**API Format**:
```
https://boards-api.greenhouse.io/v1/boards/{company}/jobs
```

**Example**:
```bash
curl https://boards-api.greenhouse.io/v1/boards/anthropic/jobs
```

**Response**: JSON with job listings, no authentication required

### Lever API
**Companies**: OpenAI, Cohere, Inflection, Anyscale, Replit, Figure AI

**API Format**:
```
https://api.lever.co/v0/postings/{company}
```

**Example**:
```bash
curl https://api.lever.co/v0/postings/openai
```

**Response**: JSON with job listings, no authentication required

### Ashby API
**Companies**: Adept, Replicate, Cursor, Modal

**API Format**:
```
https://jobs.ashbyhq.com/{company}
```

**Note**: Ashby doesn't have a simple public API, requires web scraping

### Custom/Workday
**Companies**: Google, Meta, Microsoft, Amazon

**Note**: These use custom systems or Workday, require web scraping

## Usage

### Scrape Specific Companies

```python
from company_scrapers import scrape_ai_companies

# Scrape specific companies
jobs = scrape_ai_companies(['openai', 'anthropic', 'cohere'])

# Scrape all Greenhouse companies
from company_scrapers import CompanyScraperManager
manager = CompanyScraperManager()
jobs = manager.scrape_all_companies()

# Scrape by tier
jobs = manager.scrape_tier(1)  # Tier 1 companies only

# Scrape top 10 companies
jobs = manager.scrape_top_companies(limit=10)
```

### Command Line (Enhanced)

Add to `neilsearch.py`:

```bash
# Scan AI companies only
python neilsearch.py scan-companies

# Scan specific companies
python neilsearch.py scan-companies --companies openai,anthropic,cohere

# Scan by tier
python neilsearch.py scan-companies --tier 1

# Scan top N companies
python neilsearch.py scan-companies --top 10
```

## Implementation Strategy

### Phase 1: API-Based Companies (Done)
✅ Greenhouse API scraper
✅ Lever API scraper
✅ Company database with 30 companies
✅ Filtering by location and job type

### Phase 2: Web Scraping (To Do)
- Ashby page scraper
- Google/Meta custom scrapers
- Playwright-based scraping for dynamic sites

### Phase 3: Enhancement (To Do)
- Job board aggregation (combine with existing scrapers)
- Duplicate detection across sources
- Company priority weighting
- Notification for new jobs at specific companies

## Best Practices

### 1. Respect Rate Limits
```python
import time
time.sleep(2)  # 2 seconds between requests
```

### 2. Filter Jobs Locally
- Download all jobs first
- Filter by location, role, seniority locally
- Reduces API calls

### 3. Cache Results
- Store results in database
- Only fetch new jobs
- Check by job ID or URL

### 4. Error Handling
```python
try:
    jobs = scraper.scrape()
except Exception as e:
    print(f"Error: {e}")
    continue  # Move to next company
```

### 5. User-Agent Headers
```python
headers = {
    "User-Agent": "JobSearchBot/1.0 (yourname@email.com)"
}
```

## Monitoring & Maintenance

### Check API Health
```python
from company_scrapers import CompanyScraperManager

manager = CompanyScraperManager()

# Test each company
for company_key in ["openai", "anthropic", "cohere"]:
    jobs = scrape_ai_companies([company_key])
    print(f"{company_key}: {len(jobs)} jobs")
```

### Update Company List
- Check quarterly for new AI companies
- Update ATS URLs if companies switch providers
- Remove defunct companies

### Monitor Success Rate
```python
# Track success rate per company
stats = {
    "openai": {"attempts": 10, "successes": 9},
    "anthropic": {"attempts": 10, "successes": 10},
}
```

## Alternative Strategies

### 1. RSS Feeds
Some companies offer RSS feeds for jobs:
```
https://company.com/careers/feed.xml
```

### 2. GitHub Jobs
Many AI companies post on GitHub:
```
https://jobs.github.com/positions.json?description=machine+learning
```

### 3. Company-Specific APIs
Some companies have their own APIs:
```python
# Example: Anthropic might have
GET https://api.anthropic.com/v1/careers
```

### 4. LinkedIn Company Pages
Scrape specific company pages:
```
https://www.linkedin.com/company/{company}/jobs
```

### 5. AngelList by Company
```
https://angel.co/{company}/jobs
```

### 6. Y Combinator Company List
```
https://www.ycombinator.com/companies?industry=AI
```

## Legal Considerations

### ✅ Allowed:
- Using public APIs (Greenhouse, Lever)
- Scraping publicly accessible career pages
- Respecting robots.txt
- Personal, non-commercial use

### ⚠️ Caution:
- Don't overload servers (rate limit)
- Don't bypass authentication
- Don't scrape personal data
- Don't resell job data

### ❌ Avoid:
- Ignoring robots.txt
- DDoS-level request rates
- Circumventing CAPTCHAs
- Commercial scraping without permission

## Troubleshooting

### API Returns Empty
- Check if company changed ATS provider
- Verify API URL is correct
- Check if company is hiring

### Rate Limited
- Increase delay between requests
- Implement exponential backoff
- Spread requests over time

### Jobs Not Filtered Properly
- Update location keywords
- Adjust ML/AI keyword matching
- Check job description parsing

## Future Enhancements

1. **Email Alerts**: Notify when specific companies post jobs
2. **Company Priority**: Weight matches by company tier
3. **Application Tracking**: Track applications per company
4. **Company Research**: Fetch company info (size, funding, stage)
5. **Social Integration**: Link to company Twitter, GitHub, etc.
6. **Salary Data**: Integrate with levels.fyi or H1B data
7. **Culture Fit**: Analyze company values vs preferences

## Example Workflow

```bash
# Weekly scan of top AI companies
python neilsearch.py scan-companies --tier 1

# Check new jobs
python neilsearch.py summary

# Focus on high-value companies
python neilsearch.py scan-companies --companies openai,anthropic,cohere,google_brain

# Export for review
python neilsearch.py export --output weekly-ai-jobs.csv --min-score 60
```

## Success Metrics

Track these to measure improvement:
- Jobs found per company
- Match score distribution
- Time to scrape
- API success rate
- False positive rate (irrelevant jobs)
- Application response rate

## Resources

- [Greenhouse API Docs](https://developers.greenhouse.io/)
- [Lever API Docs](https://github.com/lever/postings-api)
- [robots.txt Checker](http://www.robotstxt.org/robotstxt.html)
- [User-Agent Best Practices](https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers)

---

**Pro Tip**: Companies using the same ATS (Greenhouse, Lever) have identical API structures. Once you build one scraper, you can reuse it for all companies on that platform!
