#!/usr/bin/env python3
"""NeilSearch - AI/ML Job Matching Tool CLI."""
import sys
import time
import webbrowser
from pathlib import Path
from datetime import datetime

import click
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box

import config
from database import Database
from resume_parser import parse_resume
from scrapers import ScraperManager
from matcher import JobMatcher
from dashboard import generate_dashboard


console = Console()


@click.group()
def cli():
    """NeilSearch - AI/ML Job Matching Tool for San Francisco."""
    pass


@cli.command()
@click.option("--resume", required=True, type=click.Path(exists=True), help="Path to resume file (PDF or DOCX)")
def profile(resume):
    """Parse resume and create/update candidate profile."""
    console.print(f"\n[bold blue]Parsing resume:[/bold blue] {resume}")

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Extracting text from resume...", total=None)
            profile_data = parse_resume(resume)
            progress.update(task, completed=True)

        # Display extracted information
        console.print("\n[bold green]Profile created successfully![/bold green]\n")

        console.print(f"[bold]Skills found:[/bold] {len(profile_data['skills'])}")
        if profile_data['skills']:
            console.print(f"  {', '.join(profile_data['skills'][:10])}")
            if len(profile_data['skills']) > 10:
                console.print(f"  ... and {len(profile_data['skills']) - 10} more")

        console.print(f"\n[bold]Experience level:[/bold] {profile_data['experience_level']}")
        console.print(f"[bold]Years of experience:[/bold] {profile_data['years_of_experience']}")

        if profile_data['education']:
            console.print(f"[bold]Education:[/bold] {', '.join(profile_data['education'])}")

        if profile_data['role_types']:
            console.print(f"[bold]Role types:[/bold] {', '.join(profile_data['role_types'])}")

        # Save to database
        with Database() as db:
            db.init_db()
            db.save_profile(resume, profile_data)

        console.print("\n[green]Profile saved to database.[/green]")
        console.print("\n[yellow]Next step:[/yellow] Run 'python neilsearch.py scan' to find matching jobs!")

    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}")
        sys.exit(1)


@cli.command()
@click.option("--boards", help="Comma-separated list of boards to scan (e.g., 'linkedin,indeed')")
def scan(boards):
    """Scan job boards and match against profile."""
    console.print("\n[bold blue]Starting job scan...[/bold blue]\n")

    # Check if profile exists
    with Database() as db:
        db.init_db()
        profile_data = db.get_profile()

        if not profile_data:
            console.print("[bold red]Error:[/bold red] No profile found. Run 'python neilsearch.py profile --resume <path>' first.")
            sys.exit(1)

        console.print(f"[green]Using profile from:[/green] {profile_data['resume_path']}")
        console.print(f"[green]Last updated:[/green] {profile_data['last_updated']}\n")

    start_time = time.time()

    # Initialize scraper
    board_list = [b.strip() for b in boards.split(",")] if boards else None
    scraper_manager = ScraperManager()

    # Scrape jobs
    console.print("[bold]Scraping job boards...[/bold]")
    jobs = scraper_manager.scrape_all(board_names=board_list)


@cli.command("scan-companies")
@click.option("--companies", help="Comma-separated list of companies (e.g., 'openai,anthropic,cohere')")
@click.option("--tier", type=int, help="Scan companies by tier (1-6)")
@click.option("--top", type=int, help="Scan top N companies")
def scan_companies(companies, tier, top):
    """Scan AI company career pages directly (more reliable than job boards)."""
    console.print("\n[bold blue]Starting AI company scan...[/bold blue]\n")

    # Check if profile exists
    with Database() as db:
        db.init_db()
        profile_data = db.get_profile()

        if not profile_data:
            console.print("[bold red]Error:[/bold red] No profile found. Run 'python neilsearch.py profile --resume <path>' first.")
            sys.exit(1)

        console.print(f"[green]Using profile from:[/green] {profile_data['resume_path']}")
        console.print(f"[green]Last updated:[/green] {profile_data['last_updated']}\n")

    start_time = time.time()

    # Import company scraper
    try:
        from company_scrapers import CompanyScraperManager
    except ImportError as e:
        console.print(f"[bold red]Error:[/bold red] Could not import company scrapers: {e}")
        sys.exit(1)

    manager = CompanyScraperManager()

    # Determine what to scrape
    if companies:
        company_list = [c.strip() for c in companies.split(",")]
        console.print(f"[bold]Scraping companies:[/bold] {', '.join(company_list)}\n")
        jobs = manager.scrape_all_companies(company_list)
    elif tier:
        console.print(f"[bold]Scraping Tier {tier} companies...[/bold]\n")
        jobs = manager.scrape_tier(tier)
    elif top:
        console.print(f"[bold]Scraping top {top} companies...[/bold]\n")
        jobs = manager.scrape_top_companies(limit=top)
    else:
        console.print("[bold]Scraping all AI companies with public APIs...[/bold]\n")
        jobs = manager.scrape_all_companies()

    console.print(f"\n[green]Total jobs found:[/green] {len(jobs)}")

    if not jobs:
        console.print("[yellow]No jobs found. Companies may not be hiring or APIs may have changed.[/yellow]")
        return

    # Match jobs against profile
    console.print("\n[bold]Matching jobs against profile...[/bold]")
    matcher = JobMatcher(profile_data['profile_data'])

    new_jobs = 0
    duplicates = 0

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Processing jobs...", total=len(jobs))

        with Database() as db:
            for job in jobs:
                # Match job
                match_result = matcher.match_job(job)

                # Add match results to job data
                job.update(match_result)

                # Save to database
                is_new = db.save_job(job)
                if is_new:
                    new_jobs += 1
                else:
                    duplicates += 1

                progress.update(task, advance=1)

            # Save scan history
            duration = time.time() - start_time
            boards_scanned = len(company_list) if companies else (top if top else 10)
            db.save_scan_history(new_jobs, boards_scanned, duration)

    # Display results
    console.print(f"\n[bold green]Scan complete![/bold green]")
    console.print(f"[green]New jobs:[/green] {new_jobs}")
    console.print(f"[yellow]Duplicate jobs removed:[/yellow] {duplicates}")
    console.print(f"[blue]Duration:[/blue] {duration:.1f}s\n")

    # Show top matches
    if new_jobs > 0:
        with Database() as db:
            top_jobs = db.get_jobs(min_score=60)[:5]

        if top_jobs:
            console.print("[bold]Top matches:[/bold]\n")

            table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
            table.add_column("Score", style="cyan", width=6)
            table.add_column("Title", style="white", width=35)
            table.add_column("Company", style="green", width=20)
            table.add_column("Location", style="blue", width=15)

            for job in top_jobs:
                score = f"{job['match_score']:.0f}"
                table.add_row(score, job['title'][:35], job['company'][:20], job['location'][:15])

            console.print(table)

    console.print("\n[yellow]Next step:[/yellow] Run 'python neilsearch.py dashboard' to view all jobs!")


@cli.command("list-companies")
def list_companies():
    """List all available AI companies that can be scraped."""
    from ai_companies_100 import (
        AI_COMPANIES_100,
        get_companies_by_tier,
        get_all_companies_count,
        get_api_companies_count
    )

    console.print("\n[bold blue]Top 100 AI/ML Companies (US & Remote Jobs Only)[/bold blue]\n")
    console.print(f"[green]Total Companies:[/green] {get_all_companies_count()}")
    console.print(f"[green]With Public APIs:[/green] {get_api_companies_count()}\n")

    for tier_num in range(1, 7):
        tier_companies = get_companies_by_tier(tier_num)
        if tier_companies:
            tier_names = {
                1: "Leading AI Labs",
                2: "AI-First Startups",
                3: "AI Tools & Platforms",
                4: "AI-Powered Products",
                5: "Robotics & Applied AI",
                6: "Enterprise AI"
            }

            console.print(f"[bold]Tier {tier_num}: {tier_names[tier_num]}[/bold]")

            for key, company in tier_companies.items():
                api_type = company.get("type", "scrape")
                api_indicator = "✓ API" if api_type == "api" else "○ Web"
                console.print(f"  {api_indicator} {key:20s} - {company['name']}")

            console.print()

    console.print("[yellow]Usage examples:[/yellow]")
    console.print("  python neilsearch.py scan-companies --companies openai,anthropic")
    console.print("  python neilsearch.py scan-companies --tier 1")
    console.print("  python neilsearch.py scan-companies --top 10\n")


@cli.command()
def dashboard():
    """Generate and open the job dashboard."""
    console.print("\n[bold blue]Generating dashboard...[/bold blue]\n")

    with Database() as db:
        profile_data = db.get_profile()
        if not profile_data:
            console.print("[bold red]Error:[/bold red] No profile found. Run 'python neilsearch.py profile --resume <path>' first.")
            sys.exit(1)

        jobs = db.get_jobs()
        stats = db.get_stats()

        if not jobs:
            console.print("[yellow]No jobs found. Run 'python neilsearch.py scan' first.[/yellow]")
            sys.exit(1)

    # Generate HTML dashboard
    html_content = generate_dashboard(jobs, stats, profile_data)

    # Write to file
    output_path = config.DASHBOARD_OUTPUT
    output_path.write_text(html_content)

    console.print(f"[green]Dashboard generated:[/green] {output_path}")
    console.print(f"[green]Total jobs:[/green] {len(jobs)}")
    console.print(f"[green]Average match score:[/green] {stats['avg_match_score']}\n")

    # Open in browser
    console.print("[bold]Opening dashboard in browser...[/bold]")
    webbrowser.open(f"file://{output_path.absolute()}")


@cli.command()
def summary():
    """Generate and open the job dashboard."""
    console.print("\n[bold blue]Generating dashboard...[/bold blue]\n")

    with Database() as db:
        profile_data = db.get_profile()
        if not profile_data:
            console.print("[bold red]Error:[/bold red] No profile found. Run 'python neilsearch.py profile --resume <path>' first.")
            sys.exit(1)

        jobs = db.get_jobs()
        stats = db.get_stats()

        if not jobs:
            console.print("[yellow]No jobs found. Run 'python neilsearch.py scan' first.[/yellow]")
            sys.exit(1)

    # Generate HTML dashboard
    html_content = generate_dashboard(jobs, stats, profile_data)

    # Write to file
    output_path = config.DASHBOARD_OUTPUT
    output_path.write_text(html_content)

    console.print(f"[green]Dashboard generated:[/green] {output_path}")
    console.print(f"[green]Total jobs:[/green] {len(jobs)}")
    console.print(f"[green]Average match score:[/green] {stats['avg_match_score']}\n")

    # Open in browser
    console.print("[bold]Opening dashboard in browser...[/bold]")
    webbrowser.open(f"file://{output_path.absolute()}")


@cli.command()
def summary():
    """Show quick summary of jobs in terminal."""
    with Database() as db:
        stats = db.get_stats()
        jobs = db.get_jobs()

        if not jobs:
            console.print("[yellow]No jobs found. Run 'python neilsearch.py scan' first.[/yellow]")
            return

        console.print("\n[bold blue]Job Search Summary[/bold blue]\n")

        # Overall stats
        console.print(f"[bold]Total jobs:[/bold] {stats['total_jobs']}")
        console.print(f"[bold]Average match score:[/bold] {stats['avg_match_score']}")

        if stats.get('last_scan'):
            scan_date = datetime.fromisoformat(stats['last_scan']['scan_date'])
            console.print(f"[bold]Last scan:[/bold] {scan_date.strftime('%Y-%m-%d %H:%M')}")
            console.print(f"[bold]Jobs found in last scan:[/bold] {stats['last_scan']['jobs_found']}")

        # Application status breakdown
        if stats.get('by_status'):
            console.print("\n[bold]Application Status:[/bold]")
            for status, count in stats['by_status'].items():
                console.print(f"  {status}: {count}")

        # Top companies
        if stats.get('top_companies'):
            console.print("\n[bold]Top Hiring Companies:[/bold]")
            for company_data in stats['top_companies'][:5]:
                console.print(f"  {company_data['company']}: {company_data['count']} jobs")

        # Top matches
        top_jobs = db.get_jobs(min_score=80)[:10]
        if top_jobs:
            console.print("\n[bold]Highest Match Jobs:[/bold]\n")

            table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
            table.add_column("Score", style="cyan", width=6)
            table.add_column("Title", style="white", width=40)
            table.add_column("Company", style="green", width=20)

            for job in top_jobs:
                score = f"{job['match_score']:.0f}"
                table.add_row(score, job['title'][:40], job['company'][:20])

            console.print(table)


@cli.command()
@click.option("--days", default=config.DATA_RETENTION_DAYS, help="Remove jobs older than N days")
def clean(days):
    """Remove old jobs from database."""
    console.print(f"\n[bold blue]Cleaning jobs older than {days} days...[/bold blue]\n")

    with Database() as db:
        deleted = db.clean_old_jobs(days)

    console.print(f"[green]Deleted {deleted} old jobs.[/green]")


@cli.command()
@click.option("--output", default="jobs.csv", help="Output CSV file path")
@click.option("--min-score", type=float, help="Minimum match score")
def export(output, min_score):
    """Export jobs to CSV."""
    import csv

    console.print(f"\n[bold blue]Exporting jobs to {output}...[/bold blue]\n")

    with Database() as db:
        jobs = db.get_jobs(min_score=min_score)

    if not jobs:
        console.print("[yellow]No jobs to export.[/yellow]")
        return

    # Write CSV
    with open(output, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['title', 'company', 'location', 'match_score', 'url', 'posted_date', 'app_status']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for job in jobs:
            writer.writerow({
                'title': job['title'],
                'company': job['company'],
                'location': job['location'],
                'match_score': job['match_score'],
                'url': job['url'],
                'posted_date': job.get('posted_date', ''),
                'app_status': job.get('app_status', '')
            })

    console.print(f"[green]Exported {len(jobs)} jobs to {output}[/green]")


if __name__ == "__main__":
    cli()
