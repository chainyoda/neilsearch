#!/bin/bash

echo "========================================="
echo "NeilSearch Setup"
echo "========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo ""
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install Playwright browsers
echo ""
echo "Installing Playwright browsers..."
playwright install chromium

# Download spaCy model
echo ""
echo "Downloading spaCy language model..."
python -m spacy download en_core_web_sm

echo ""
echo "========================================="
echo "Setup Complete!"
echo "========================================="
echo ""
echo "To get started:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Create your profile:"
echo "   python neilsearch.py profile --resume /path/to/resume.pdf"
echo ""
echo "3. Scan for jobs:"
echo "   python neilsearch.py scan"
echo ""
echo "4. View dashboard:"
echo "   python neilsearch.py dashboard"
echo ""
