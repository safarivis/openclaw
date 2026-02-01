#!/usr/bin/env python3
"""
Yahoo Finance News Scraper
Fetches recent news for a given stock ticker.

Usage:
    python yahoo_news.py TICKER [--limit 10]

Examples:
    python yahoo_news.py GOLF
    python yahoo_news.py AAPL --limit 20
"""

import argparse
import json
import sys
from datetime import datetime

try:
    import yfinance as yf
except ImportError:
    print("Error: yfinance not installed. Run: pip install yfinance")
    sys.exit(1)


def get_stock_news(ticker: str, limit: int = 10) -> list:
    """
    Fetch recent news for a stock ticker.

    Args:
        ticker: Stock ticker symbol
        limit: Maximum number of news items

    Returns:
        List of news dictionaries
    """
    stock = yf.Ticker(ticker)

    try:
        news = stock.news
    except Exception as e:
        print(f"Error fetching news: {e}", file=sys.stderr)
        return []

    if not news:
        return []

    results = []
    for item in news[:limit]:
        # Extract relevant fields
        news_item = {
            "title": item.get("title", "No title"),
            "publisher": item.get("publisher", "Unknown"),
            "link": item.get("link", ""),
            "published": "",
            "type": item.get("type", "article"),
            "thumbnail": ""
        }

        # Parse timestamp
        pub_time = item.get("providerPublishTime")
        if pub_time:
            try:
                dt = datetime.fromtimestamp(pub_time)
                news_item["published"] = dt.strftime("%Y-%m-%d %H:%M")
            except:
                pass

        # Get thumbnail
        thumbnail = item.get("thumbnail", {})
        if isinstance(thumbnail, dict):
            resolutions = thumbnail.get("resolutions", [])
            if resolutions:
                news_item["thumbnail"] = resolutions[0].get("url", "")

        results.append(news_item)

    return results


def get_stock_calendar(ticker: str) -> dict:
    """
    Get upcoming events (earnings, dividends, etc.)

    Args:
        ticker: Stock ticker symbol

    Returns:
        Dictionary with calendar events
    """
    stock = yf.Ticker(ticker)

    calendar = {
        "earnings_date": None,
        "dividend_date": None,
        "ex_dividend_date": None
    }

    try:
        info = stock.info

        # Earnings date
        earnings = info.get("earningsTimestamp")
        if earnings:
            try:
                calendar["earnings_date"] = datetime.fromtimestamp(earnings).strftime("%Y-%m-%d")
            except:
                pass

        # Dividend date
        div_date = info.get("dividendDate")
        if div_date:
            try:
                calendar["dividend_date"] = datetime.fromtimestamp(div_date).strftime("%Y-%m-%d")
            except:
                pass

        # Ex-dividend date
        ex_div = info.get("exDividendDate")
        if ex_div:
            try:
                calendar["ex_dividend_date"] = datetime.fromtimestamp(ex_div).strftime("%Y-%m-%d")
            except:
                pass

    except Exception as e:
        print(f"Error fetching calendar: {e}", file=sys.stderr)

    return calendar


def categorize_news(news: list) -> dict:
    """
    Categorize news by type/sentiment.

    Args:
        news: List of news items

    Returns:
        Dictionary with categorized news
    """
    categories = {
        "earnings": [],
        "analyst": [],
        "product": [],
        "market": [],
        "other": []
    }

    keywords = {
        "earnings": ["earnings", "quarter", "revenue", "profit", "eps", "guidance", "beat", "miss"],
        "analyst": ["analyst", "upgrade", "downgrade", "rating", "price target", "buy", "sell", "hold"],
        "product": ["launch", "product", "release", "announce", "new", "innovation"],
        "market": ["market", "stock", "shares", "trading", "investor", "rally", "drop", "surge"]
    }

    for item in news:
        title_lower = item.get("title", "").lower()
        categorized = False

        for category, kws in keywords.items():
            if any(kw in title_lower for kw in kws):
                categories[category].append(item)
                categorized = True
                break

        if not categorized:
            categories["other"].append(item)

    return categories


def format_news_markdown(ticker: str, news: list, calendar: dict = None) -> str:
    """Format news as markdown."""
    lines = []
    lines.append(f"# News: {ticker}")
    lines.append(f"\n**Generated:** {datetime.now().isoformat()}")
    lines.append("")

    # Calendar events
    if calendar:
        lines.append("## Upcoming Events")
        lines.append("| Event | Date |")
        lines.append("|-------|------|")
        if calendar.get("earnings_date"):
            lines.append(f"| Earnings | {calendar['earnings_date']} |")
        if calendar.get("ex_dividend_date"):
            lines.append(f"| Ex-Dividend | {calendar['ex_dividend_date']} |")
        if calendar.get("dividend_date"):
            lines.append(f"| Dividend Payment | {calendar['dividend_date']} |")
        lines.append("")

    # News items
    if not news:
        lines.append("## Recent News")
        lines.append("No recent news found.")
        return "\n".join(lines)

    # Categorize
    categorized = categorize_news(news)

    for category, items in categorized.items():
        if not items:
            continue

        category_title = category.title()
        lines.append(f"## {category_title} News")
        lines.append("")

        for item in items:
            title = item.get("title", "No title")
            publisher = item.get("publisher", "Unknown")
            published = item.get("published", "")
            link = item.get("link", "")

            lines.append(f"### {title}")
            lines.append(f"*{publisher} - {published}*")
            if link:
                lines.append(f"[Read more]({link})")
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fetch Yahoo Finance news")
    parser.add_argument("ticker", help="Stock ticker symbol")
    parser.add_argument("--limit", type=int, default=10,
                        help="Maximum number of news items (default: 10)")
    parser.add_argument("--calendar", action="store_true",
                        help="Include calendar events")
    parser.add_argument("--output", choices=["json", "markdown"], default="markdown",
                        help="Output format")

    args = parser.parse_args()

    ticker = args.ticker.upper()

    print(f"Fetching news for {ticker}...", file=sys.stderr)
    news = get_stock_news(ticker, args.limit)

    calendar = None
    if args.calendar:
        print(f"Fetching calendar...", file=sys.stderr)
        calendar = get_stock_calendar(ticker)

    if args.output == "json":
        output = {
            "ticker": ticker,
            "news": news,
            "calendar": calendar
        }
        print(json.dumps(output, indent=2))
    else:
        print(format_news_markdown(ticker, news, calendar))


if __name__ == "__main__":
    main()
