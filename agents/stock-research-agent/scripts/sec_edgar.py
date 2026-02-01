#!/usr/bin/env python3
"""
SEC EDGAR Filing Fetcher
Fetches SEC filings (10-K, 10-Q, 8-K, etc.) for a given company.

Usage:
    python sec_edgar.py TICKER [--type 10-K] [--limit 5]

Examples:
    python sec_edgar.py GOLF
    python sec_edgar.py AAPL --type 10-K --limit 3
    python sec_edgar.py MSFT --type 8-K --limit 10
"""

import argparse
import json
import re
import sys
from datetime import datetime
from typing import Optional

try:
    import requests
except ImportError:
    print("Error: requests not installed. Run: pip install requests")
    sys.exit(1)


# SEC requires a user agent
HEADERS = {
    "User-Agent": "StockResearchAgent/1.0 (research@example.com)",
    "Accept-Encoding": "gzip, deflate"
}

SEC_BASE = "https://www.sec.gov"
EDGAR_SEARCH = "https://efts.sec.gov/LATEST/search-index"
COMPANY_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"


def get_cik_from_ticker(ticker: str) -> Optional[str]:
    """Convert ticker to CIK (Central Index Key)."""
    try:
        response = requests.get(COMPANY_TICKERS_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()

        ticker_upper = ticker.upper()
        for entry in data.values():
            if entry.get("ticker", "").upper() == ticker_upper:
                # CIK needs to be zero-padded to 10 digits
                cik = str(entry.get("cik_str", ""))
                return cik.zfill(10)

        return None
    except Exception as e:
        print(f"Error fetching CIK: {e}", file=sys.stderr)
        return None


def get_company_filings(cik: str, filing_type: str = None, limit: int = 10) -> list:
    """
    Fetch recent filings for a company from SEC EDGAR.

    Args:
        cik: Company CIK (10-digit zero-padded)
        filing_type: Filter by filing type (10-K, 10-Q, 8-K, etc.)
        limit: Maximum number of filings to return

    Returns:
        List of filing dictionaries
    """
    # Use SEC's company submissions API
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"

    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error fetching filings: {e}", file=sys.stderr)
        return []

    filings = []
    recent = data.get("filings", {}).get("recent", {})

    if not recent:
        return []

    # Extract filing data
    forms = recent.get("form", [])
    filing_dates = recent.get("filingDate", [])
    accession_numbers = recent.get("accessionNumber", [])
    primary_docs = recent.get("primaryDocument", [])
    descriptions = recent.get("primaryDocDescription", [])

    for i in range(min(len(forms), 100)):  # Check up to 100 filings
        form = forms[i] if i < len(forms) else ""
        filing_date = filing_dates[i] if i < len(filing_dates) else ""
        accession = accession_numbers[i] if i < len(accession_numbers) else ""
        primary_doc = primary_docs[i] if i < len(primary_docs) else ""
        description = descriptions[i] if i < len(descriptions) else ""

        # Filter by type if specified
        if filing_type and form.upper() != filing_type.upper():
            # Also match partial (e.g., "10-K" matches "10-K/A")
            if not form.upper().startswith(filing_type.upper()):
                continue

        # Build filing URL
        accession_clean = accession.replace("-", "")
        filing_url = f"{SEC_BASE}/Archives/edgar/data/{cik.lstrip('0')}/{accession_clean}/{primary_doc}"
        index_url = f"{SEC_BASE}/Archives/edgar/data/{cik.lstrip('0')}/{accession_clean}/"

        filings.append({
            "form": form,
            "filing_date": filing_date,
            "accession_number": accession,
            "description": description,
            "document_url": filing_url,
            "index_url": index_url
        })

        if len(filings) >= limit:
            break

    return filings


def get_filing_content(url: str, max_chars: int = 50000) -> str:
    """
    Fetch the content of a filing.

    Args:
        url: URL to the filing document
        max_chars: Maximum characters to return

    Returns:
        Filing text content (truncated if too long)
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()

        content = response.text

        # If HTML, try to extract text
        if "<html" in content.lower() or "<body" in content.lower():
            # Simple HTML text extraction
            content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
            content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
            content = re.sub(r'<[^>]+>', ' ', content)
            content = re.sub(r'\s+', ' ', content)
            content = content.strip()

        if len(content) > max_chars:
            content = content[:max_chars] + f"\n\n[... truncated at {max_chars} characters ...]"

        return content

    except Exception as e:
        return f"Error fetching filing content: {e}"


def search_filing_for_section(content: str, section: str) -> str:
    """
    Search filing content for a specific section.

    Common sections:
    - "Item 1" or "Business" - Business description
    - "Item 1A" or "Risk Factors" - Risk factors
    - "Item 7" or "MD&A" - Management discussion
    - "Item 8" - Financial statements

    Args:
        content: Filing text content
        section: Section to search for

    Returns:
        Extracted section text or message if not found
    """
    # Common section patterns
    patterns = {
        "business": r"(?:Item\s*1[.\s]*[-–—]?\s*)?Business\s*\n",
        "risk": r"(?:Item\s*1A[.\s]*[-–—]?\s*)?Risk\s*Factors",
        "mda": r"(?:Item\s*7[.\s]*[-–—]?\s*)?Management[''`]?s?\s*Discussion",
        "financials": r"(?:Item\s*8[.\s]*[-–—]?\s*)?Financial\s*Statements",
    }

    section_lower = section.lower()
    pattern = patterns.get(section_lower)

    if not pattern:
        # Try to find the literal section
        pattern = re.escape(section)

    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        start = match.start()
        # Extract up to 10000 chars from section start
        return content[start:start + 10000]

    return f"Section '{section}' not found in filing."


def format_filings_markdown(ticker: str, filings: list, company_name: str = None) -> str:
    """Format filings list as markdown."""
    lines = []
    name = company_name or ticker
    lines.append(f"# SEC Filings: {name} ({ticker})")
    lines.append(f"\n**Generated:** {datetime.now().isoformat()}")
    lines.append(f"\n**Source:** SEC EDGAR")
    lines.append("")

    if not filings:
        lines.append("No filings found.")
        return "\n".join(lines)

    lines.append("| Date | Form | Description | Link |")
    lines.append("|------|------|-------------|------|")

    for f in filings:
        date = f.get("filing_date", "N/A")
        form = f.get("form", "N/A")
        desc = f.get("description", "")[:50]
        url = f.get("document_url", "")
        lines.append(f"| {date} | {form} | {desc} | [View]({url}) |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fetch SEC EDGAR filings")
    parser.add_argument("ticker", help="Stock ticker symbol")
    parser.add_argument("--type", dest="filing_type", default=None,
                        help="Filing type filter (10-K, 10-Q, 8-K, etc.)")
    parser.add_argument("--limit", type=int, default=10,
                        help="Maximum number of filings (default: 10)")
    parser.add_argument("--fetch", metavar="INDEX",
                        help="Fetch content of filing at index (0-based)")
    parser.add_argument("--section", default=None,
                        help="Extract specific section (business, risk, mda, financials)")
    parser.add_argument("--output", choices=["json", "markdown"], default="markdown",
                        help="Output format")

    args = parser.parse_args()

    # Get CIK
    print(f"Looking up CIK for {args.ticker}...", file=sys.stderr)
    cik = get_cik_from_ticker(args.ticker)

    if not cik:
        print(f"Error: Could not find CIK for ticker {args.ticker}", file=sys.stderr)
        sys.exit(1)

    print(f"Found CIK: {cik}", file=sys.stderr)

    # Get filings
    print(f"Fetching filings...", file=sys.stderr)
    filings = get_company_filings(cik, args.filing_type, args.limit)

    if args.fetch is not None:
        # Fetch specific filing content
        idx = int(args.fetch)
        if idx < 0 or idx >= len(filings):
            print(f"Error: Index {idx} out of range (0-{len(filings)-1})", file=sys.stderr)
            sys.exit(1)

        url = filings[idx].get("document_url")
        print(f"Fetching content from: {url}", file=sys.stderr)
        content = get_filing_content(url)

        if args.section:
            content = search_filing_for_section(content, args.section)

        print(content)
    else:
        # List filings
        if args.output == "json":
            print(json.dumps(filings, indent=2))
        else:
            print(format_filings_markdown(args.ticker, filings))


if __name__ == "__main__":
    main()
