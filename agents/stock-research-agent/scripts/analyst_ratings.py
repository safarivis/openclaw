#!/usr/bin/env python3
"""
Analyst Ratings Aggregator
Fetches analyst ratings, price targets, and recommendations.

Usage:
    python analyst_ratings.py TICKER

Examples:
    python analyst_ratings.py GOLF
    python analyst_ratings.py AAPL
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Optional

try:
    import yfinance as yf
except ImportError:
    print("Error: yfinance not installed. Run: pip install yfinance")
    sys.exit(1)

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False


def get_analyst_recommendations(ticker: str) -> dict:
    """
    Get analyst recommendations and price targets.

    Args:
        ticker: Stock ticker symbol

    Returns:
        Dictionary with analyst data
    """
    stock = yf.Ticker(ticker)
    info = stock.info

    result = {
        "ticker": ticker,
        "current_price": info.get("currentPrice") or info.get("regularMarketPrice"),
        "target_high": info.get("targetHighPrice"),
        "target_low": info.get("targetLowPrice"),
        "target_mean": info.get("targetMeanPrice"),
        "target_median": info.get("targetMedianPrice"),
        "recommendation": info.get("recommendationKey"),
        "recommendation_mean": info.get("recommendationMean"),
        "num_analysts": info.get("numberOfAnalystOpinions"),
        "upside_potential": None,
        "recent_ratings": [],
        "rating_trend": {}
    }

    # Calculate upside potential
    if result["current_price"] and result["target_mean"]:
        try:
            upside = (result["target_mean"] - result["current_price"]) / result["current_price"]
            result["upside_potential"] = upside
        except:
            pass

    # Get recent analyst ratings
    try:
        recommendations = stock.recommendations
        if recommendations is not None and not recommendations.empty:
            # Get last 10 ratings
            recent = recommendations.tail(10)
            for idx, row in recent.iterrows():
                rating = {
                    "date": str(idx.date()) if hasattr(idx, 'date') else str(idx),
                    "firm": row.get("Firm", "Unknown"),
                    "to_grade": row.get("To Grade", ""),
                    "from_grade": row.get("From Grade", ""),
                    "action": row.get("Action", "")
                }
                result["recent_ratings"].append(rating)

            result["recent_ratings"].reverse()  # Most recent first
    except Exception as e:
        print(f"Error fetching recommendations: {e}", file=sys.stderr)

    # Get rating trend
    try:
        trend = stock.recommendations_summary
        if trend is not None and not trend.empty:
            # Convert to dict
            for col in trend.columns:
                if col != "period":
                    values = trend[col].tolist()
                    if values:
                        result["rating_trend"][col] = values[0] if len(values) == 1 else values
    except Exception as e:
        print(f"Error fetching trend: {e}", file=sys.stderr)

    return result


def get_earnings_estimates(ticker: str) -> dict:
    """
    Get earnings estimates and history.

    Args:
        ticker: Stock ticker symbol

    Returns:
        Dictionary with earnings data
    """
    stock = yf.Ticker(ticker)
    info = stock.info

    result = {
        "current_eps": info.get("trailingEps"),
        "forward_eps": info.get("forwardEps"),
        "peg_ratio": info.get("pegRatio"),
        "earnings_growth": info.get("earningsGrowth"),
        "earnings_quarterly_growth": info.get("earningsQuarterlyGrowth"),
        "estimates": [],
        "history": []
    }

    # Get earnings estimates
    try:
        earnings = stock.earnings_dates
        if earnings is not None and not earnings.empty:
            for idx, row in earnings.head(4).iterrows():
                est = {
                    "date": str(idx.date()) if hasattr(idx, 'date') else str(idx),
                    "eps_estimate": row.get("EPS Estimate"),
                    "eps_actual": row.get("Reported EPS"),
                    "surprise": row.get("Surprise(%)"),
                }
                result["estimates"].append(est)
    except Exception as e:
        print(f"Error fetching earnings: {e}", file=sys.stderr)

    return result


def interpret_recommendation(mean_score: float) -> str:
    """
    Interpret the recommendation mean score.

    Score scale: 1 = Strong Buy, 2 = Buy, 3 = Hold, 4 = Sell, 5 = Strong Sell
    """
    if mean_score is None:
        return "No Rating"
    if mean_score <= 1.5:
        return "Strong Buy"
    elif mean_score <= 2.5:
        return "Buy"
    elif mean_score <= 3.5:
        return "Hold"
    elif mean_score <= 4.5:
        return "Sell"
    else:
        return "Strong Sell"


def format_ratings_markdown(data: dict, earnings: dict = None) -> str:
    """Format analyst ratings as markdown."""
    lines = []
    lines.append(f"# Analyst Ratings: {data['ticker']}")
    lines.append(f"\n**Generated:** {datetime.now().isoformat()}")
    lines.append("")

    # Price targets
    lines.append("## Price Targets")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")

    current = data.get("current_price")
    if current:
        lines.append(f"| Current Price | ${current:.2f} |")

    target_mean = data.get("target_mean")
    if target_mean:
        lines.append(f"| Mean Target | ${target_mean:.2f} |")

    target_median = data.get("target_median")
    if target_median:
        lines.append(f"| Median Target | ${target_median:.2f} |")

    target_high = data.get("target_high")
    if target_high:
        lines.append(f"| High Target | ${target_high:.2f} |")

    target_low = data.get("target_low")
    if target_low:
        lines.append(f"| Low Target | ${target_low:.2f} |")

    upside = data.get("upside_potential")
    if upside is not None:
        pct = f"{upside*100:+.1f}%"
        lines.append(f"| **Upside Potential** | **{pct}** |")

    lines.append("")

    # Consensus
    lines.append("## Consensus Rating")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")

    rec = data.get("recommendation", "N/A")
    lines.append(f"| Recommendation | {rec.upper() if rec else 'N/A'} |")

    rec_mean = data.get("recommendation_mean")
    if rec_mean:
        interp = interpret_recommendation(rec_mean)
        lines.append(f"| Mean Score | {rec_mean:.2f} ({interp}) |")

    num = data.get("num_analysts")
    if num:
        lines.append(f"| # of Analysts | {num} |")

    lines.append("")

    # Rating trend
    trend = data.get("rating_trend", {})
    if trend:
        lines.append("## Rating Distribution")
        lines.append("| Rating | Count |")
        lines.append("|--------|-------|")
        for rating, count in trend.items():
            if isinstance(count, (int, float)) and count > 0:
                lines.append(f"| {rating} | {int(count)} |")
        lines.append("")

    # Recent ratings
    recent = data.get("recent_ratings", [])
    if recent:
        lines.append("## Recent Analyst Actions")
        lines.append("| Date | Firm | Action | Rating |")
        lines.append("|------|------|--------|--------|")
        for r in recent[:10]:
            date = r.get("date", "")
            firm = r.get("firm", "Unknown")[:20]
            action = r.get("action", "")
            to_grade = r.get("to_grade", "")
            lines.append(f"| {date} | {firm} | {action} | {to_grade} |")
        lines.append("")

    # Earnings
    if earnings:
        lines.append("## Earnings")
        lines.append("| Metric | Value |")
        lines.append("|--------|-------|")

        if earnings.get("current_eps"):
            lines.append(f"| TTM EPS | ${earnings['current_eps']:.2f} |")
        if earnings.get("forward_eps"):
            lines.append(f"| Forward EPS | ${earnings['forward_eps']:.2f} |")
        if earnings.get("earnings_growth"):
            lines.append(f"| Earnings Growth | {earnings['earnings_growth']*100:.1f}% |")
        lines.append("")

        # Earnings history
        ests = earnings.get("estimates", [])
        if ests:
            lines.append("### Recent Quarters")
            lines.append("| Date | Estimate | Actual | Surprise |")
            lines.append("|------|----------|--------|----------|")
            for e in ests:
                date = e.get("date", "")
                est = e.get("eps_estimate")
                actual = e.get("eps_actual")
                surprise = e.get("surprise")

                est_str = f"${est:.2f}" if est else "N/A"
                actual_str = f"${actual:.2f}" if actual else "N/A"
                surprise_str = f"{surprise:.1f}%" if surprise else "N/A"

                lines.append(f"| {date} | {est_str} | {actual_str} | {surprise_str} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fetch analyst ratings")
    parser.add_argument("ticker", help="Stock ticker symbol")
    parser.add_argument("--earnings", action="store_true",
                        help="Include earnings estimates")
    parser.add_argument("--output", choices=["json", "markdown"], default="markdown",
                        help="Output format")

    args = parser.parse_args()

    ticker = args.ticker.upper()

    print(f"Fetching analyst ratings for {ticker}...", file=sys.stderr)
    data = get_analyst_recommendations(ticker)

    earnings = None
    if args.earnings:
        print(f"Fetching earnings data...", file=sys.stderr)
        earnings = get_earnings_estimates(ticker)

    if args.output == "json":
        output = {
            "ratings": data,
            "earnings": earnings
        }
        print(json.dumps(output, indent=2, default=str))
    else:
        print(format_ratings_markdown(data, earnings))


if __name__ == "__main__":
    main()
