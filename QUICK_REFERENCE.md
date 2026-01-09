# NeilSearch Quick Reference

## 🆕 Version 2.0 - 100 Companies + US-Only Filter

### What's New
- ✅ **100 AI/ML companies** (up from 30)
- ✅ **42 companies with public APIs** (instant access)
- ✅ **US & Remote only** (international jobs filtered out)
- ✅ **6 tiers** for better organization

## Company Scraping Commands

### List Available Companies
```bash
python neilsearch.py list-companies
```
Shows all 100 AI companies organized by tier with API availability.

### Scan Specific Companies
```bash
# Individual companies
python neilsearch.py scan-companies --companies openai,anthropic,cohere

# By tier (1-6)
python neilsearch.py scan-companies --tier 1

# Top N companies
python neilsearch.py scan-companies --top 10
```

### Recommended Daily Workflow
```bash
# Quick daily scan (top 5 companies)
python neilsearch.py scan-companies --top 5
python neilsearch.py dashboard

# Or scan specific companies you're targeting
python neilsearch.py scan-companies --companies anthropic,openai,scale
python neilsearch.py dashboard
```

## All Commands

| Command | Description | Example |
|---------|-------------|---------|
| `profile` | Create profile from resume | `python neilsearch.py profile --resume resume.pdf` |
| `scan` | Scan job boards (LinkedIn, YC, etc.) | `python neilsearch.py scan` |
| `scan-companies` | **NEW** Scan AI company career pages | `python neilsearch.py scan-companies --top 10` |
| `list-companies` | **NEW** List all available companies | `python neilsearch.py list-companies` |
| `dashboard` | Open interactive dashboard | `python neilsearch.py dashboard` |
| `summary` | Terminal summary | `python neilsearch.py summary` |
| `export` | Export to CSV | `python neilsearch.py export --output jobs.csv` |
| `clean` | Remove old jobs | `python neilsearch.py clean --days 30` |

## Company Tiers

**Tier 1: Leading AI Labs** (10 companies)
- OpenAI, Anthropic, Google DeepMind, Meta AI, Google Brain, Microsoft Research, NVIDIA AI, Apple ML, Amazon Science, IBM Research

**Tier 2: AI-First Unicorns** (15 companies)
- Cohere, Hugging Face, Adept, Inflection, Character.AI, Perplexity, Mistral, Together, Fireworks, AI21, Contextual, Glean, etc.

**Tier 3: AI Infrastructure** (20 companies)
- Scale AI, Databricks, Weights & Biases, Anyscale, Modal, Pinecone, Weaviate, Chroma, Roboflow, Labelbox, Snorkel, Tecton, etc.

**Tier 4: AI Applications** (25 companies)
- Notion, Cursor, Replit, Grammarly, Jasper, Runway, Midjourney, Figma, Synthesia, Descript, Otter, Harvey, etc.

**Tier 5: Robotics & Autonomous** (15 companies)
- Tesla AI, Cruise, Waymo, Figure AI, 1X, Physical Intelligence, Covariant, Skydio, Aurora, Nuro, etc.

**Tier 6: Enterprise AI** (15 companies)
- Snowflake, Palantir, C3.ai, DataRobot, H2O.ai, Domino, Samsara, Upstart, Affirm, Plaid, etc.

## Results So Far

**Current Database:**
- 120 total jobs (US & Remote only)
- 46 from Scale AI
- 38 from Anthropic (US only)
- 14 from LinkedIn
- 15 from Y Combinator

**Potential with 100 Companies:**
- 42 API companies × 30 jobs = 1,260+ jobs
- All filtered for US & Remote only

**Match Scores:**
- High (70-100): 2 jobs ⭐
- Medium (50-69): ~30 jobs ✓
- Low (0-49): ~90 jobs

## Tips

### Get More Jobs
```bash
# Combine board scan + company scan
python neilsearch.py scan
python neilsearch.py scan-companies --tier 1
python neilsearch.py scan-companies --tier 2
```

### Focus on Quality
```bash
# Scan only top companies
python neilsearch.py scan-companies --companies anthropic,openai,cohere,scale
```

### Weekly Routine
```bash
# Monday morning
python neilsearch.py scan-companies --top 10
python neilsearch.py dashboard
python neilsearch.py export --output jobs-weekly.csv --min-score 60
```

## Troubleshooting

### No Jobs Found
- Some companies may not be hiring
- API endpoints may have changed (check `ai_companies.py`)
- Try different companies

### Low Match Scores
- Update resume with more AI/ML skills
- Re-run: `python neilsearch.py profile --resume updated-resume.pdf`
- Adjust weights in `config.py`

### API Errors
- Company may have changed ATS provider
- Check internet connection
- Some endpoints may be temporarily down

## File Locations

- **Database**: `neilsearch.db`
- **Dashboard**: `dashboard.html`
- **Config**: `config.py`
- **Company List**: `ai_companies.py`
- **Logs**: `neilsearch.log`

## Documentation

- **User Guide**: `README.md`
- **Quick Start**: `QUICKSTART.md`
- **Developer Guide**: `CLAUDE.md`
- **Company Scraping**: `COMPANY_SCRAPING_GUIDE.md`
- **Results**: `COMPANY_SCRAPING_RESULTS.md`

## Support

**GitHub Issues**: Report bugs or request features
**Documentation**: Check guides above
**Logs**: Check `neilsearch.log` for errors

---

**Pro Tip**: Company APIs (Greenhouse, Lever) are much more reliable than job boards. Use `scan-companies` as your primary method!
