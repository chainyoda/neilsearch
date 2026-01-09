#!/usr/bin/env python3
"""Verify that all modules can be imported and basic functionality works."""
import sys

def verify_imports():
    """Test all module imports."""
    print("Verifying module imports...")
    errors = []

    try:
        import config
        print("✓ config")
    except Exception as e:
        errors.append(f"✗ config: {e}")

    try:
        import database
        print("✓ database")
    except Exception as e:
        errors.append(f"✗ database: {e}")

    try:
        import resume_parser
        print("✓ resume_parser")
    except Exception as e:
        errors.append(f"✗ resume_parser: {e}")

    try:
        import matcher
        print("✓ matcher")
    except Exception as e:
        errors.append(f"✗ matcher: {e}")

    try:
        import scrapers
        print("✓ scrapers")
    except Exception as e:
        errors.append(f"✗ scrapers: {e}")

    try:
        import dashboard
        print("✓ dashboard")
    except Exception as e:
        errors.append(f"✗ dashboard: {e}")

    try:
        import neilsearch
        print("✓ neilsearch")
    except Exception as e:
        errors.append(f"✗ neilsearch: {e}")

    return errors

def verify_dependencies():
    """Test critical dependencies."""
    print("\nVerifying dependencies...")
    errors = []

    try:
        import PyPDF2
        print("✓ PyPDF2")
    except Exception as e:
        errors.append(f"✗ PyPDF2: {e}")

    try:
        import pdfplumber
        print("✓ pdfplumber")
    except Exception as e:
        errors.append(f"✗ pdfplumber: {e}")

    try:
        import docx
        print("✓ python-docx")
    except Exception as e:
        errors.append(f"✗ python-docx: {e}")

    try:
        from playwright.sync_api import sync_playwright
        print("✓ playwright")
    except Exception as e:
        errors.append(f"✗ playwright: {e}")

    try:
        from bs4 import BeautifulSoup
        print("✓ beautifulsoup4")
    except Exception as e:
        errors.append(f"✗ beautifulsoup4: {e}")

    try:
        import click
        print("✓ click")
    except Exception as e:
        errors.append(f"✗ click: {e}")

    try:
        from rich.console import Console
        print("✓ rich")
    except Exception as e:
        errors.append(f"✗ rich: {e}")

    try:
        from jinja2 import Template
        print("✓ jinja2")
    except Exception as e:
        errors.append(f"✗ jinja2: {e}")

    return errors

def verify_database():
    """Test database initialization."""
    print("\nVerifying database functionality...")
    try:
        from database import Database
        with Database() as db:
            db.init_db()
        print("✓ Database initialization successful")
        return []
    except Exception as e:
        return [f"✗ Database: {e}"]

def main():
    print("=" * 50)
    print("NeilSearch Setup Verification")
    print("=" * 50)
    print()

    all_errors = []

    # Verify imports
    errors = verify_imports()
    all_errors.extend(errors)

    # Verify dependencies
    errors = verify_dependencies()
    all_errors.extend(errors)

    # Verify database
    errors = verify_database()
    all_errors.extend(errors)

    # Print results
    print("\n" + "=" * 50)
    if all_errors:
        print("VERIFICATION FAILED")
        print("=" * 50)
        print("\nErrors found:")
        for error in all_errors:
            print(f"  {error}")
        print("\nPlease run setup:")
        print("  ./setup.sh")
        print("\nOr install missing dependencies:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    else:
        print("VERIFICATION SUCCESSFUL")
        print("=" * 50)
        print("\nAll modules loaded successfully!")
        print("\nNext steps:")
        print("1. python neilsearch.py profile --resume /path/to/resume.pdf")
        print("2. python neilsearch.py scan")
        print("3. python neilsearch.py dashboard")
        print()

if __name__ == "__main__":
    main()
