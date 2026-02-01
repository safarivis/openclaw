#!/usr/bin/env python3
"""
Stock Comparison Tool
Compares two or more stocks side by side.

Usage:
    python compare_stocks.py TICKER1 TICKER2 [TICKER3 ...]

Examples:
    python compare_stocks.py GOLF MODG
    python compare_stocks.py AAPL MSFT GOOGL
"""

import argparse
import sys

try:
    import yfinance as yf
except ImportError:
    print("Error: yfinance not installed. Run: pip install yfinance")
    sys.exit(1)


def fetch_comparison_data(ticker: str) -> dict:
    """Fetch key comparison metrics for a ticker."""
    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "ticker": ticker,
        "name": info.get("shortName", info.get("longName", ticker)),
        "price": info.get("currentPrice") or info.get("regularMarketPrice", "N/A"),
        "market_cap": info.get("marketCap"),
        "enterprise_value": info.get("enterpriseValue"),
        "revenue": info.get("totalRevenue"),
        "revenue_growth": info.get("revenueGrowth"),
        "gross_margin": info.get("grossMargins"),
        "operating_margin": info.get("operatingMargins"),
        "profit_margin": info.get("profitMargins"),
        "ebitda": info.get("ebitda"),
        "net_income": info.get("netIncomeToCommon"),
        "fcf": info.get("freeCashflow"),
        "pe_trailing": info.get("trailingPE"),
        "pe_forward": info.get("forwardPE"),
        "ev_ebitda": info.get("enterpriseToEbitda"),
        "ev_revenue": info.get("enterpriseToRevenue"),
        "pb": info.get("priceToBook"),
        "dividend_yield": info.get("dividendYield"),
        "payout_ratio": info.get("payoutRatio"),
        "debt_equity": info.get("debtToEquity"),
        "current_ratio": info.get("currentRatio"),
        "roe": info.get("returnOnEquity"),
        "roa": info.get("returnOnAssets"),
        "52_week_high": info.get("fiftyTwoWeekHigh"),
        "52_week_low": info.get("fiftyTwoWeekLow"),
        "beta": info.get("beta"),
        "shares_outstanding": info.get("sharesOutstanding")
    }


def format_value(val, format_type="number"):
    """Format a value for display."""
    if val is None or val == "N/A":
        return "N/A"

    try:
        val = float(val)
        if format_type == "number":
            if abs(val) >= 1e12:
                return f"${val/1e12:.1f}T"
            elif abs(val) >= 1e9:
                return f"${val/1e9:.1f}B"
            elif abs(val) >= 1e6:
                return f"${val/1e6:.1f}M"
            else:
                return f"${val:,.0f}"
        elif format_type == "percent":
            return f"{val*100:.1f}%"
        elif format_type == "ratio":
            return f"{val:.1f}x"
        elif format_type == "price":
            return f"${val:.2f}"
        else:
            return f"{val:.2f}"
    except:
        return str(val)


def find_winner(values: list, higher_is_better: bool = True) -> int:
    """Find the index of the winning value."""
    valid_values = []
    for i, v in enumerate(values):
        try:
            if v is not None and v != "N/A":
                valid_values.append((i, float(v)))
        except:
            pass

    if not valid_values:
        return -1

    if higher_is_better:
        winner = max(valid_values, key=lambda x: x[1])
    else:
        winner = min(valid_values, key=lambda x: x[1])

    return winner[0]


def generate_comparison(tickers: list) -> str:
    """Generate a comparison report."""
    # Fetch data for all tickers
    data = []
    for ticker in tickers:
        try:
            d = fetch_comparison_data(ticker.upper())
            data.append(d)
        except Exception as e:
            print(f"Warning: Could not fetch data for {ticker}: {e}", file=sys.stderr)

    if len(data) < 2:
        return "Error: Need at least 2 valid tickers to compare"

    lines = []
    lines.append(f"# Stock Comparison: {' vs '.join([d['ticker'] for d in data])}")
    lines.append("")

    # Header with names
    header = "| Metric |"
    separator = "|--------|"
    for d in data:
        header += f" **{d['ticker']}** |"
        separator += "--------|"
    lines.append(header)
    lines.append(separator)

    # Company names
    row = "| Company |"
    for d in data:
        name = d['name'][:20] + "..." if len(str(d['name'])) > 20 else d['name']
        row += f" {name} |"
    lines.append(row)

    # Define metrics to compare
    metrics = [
        ("**PRICE**", None, None, None),
        ("Current Price", "price", "price", True),
        ("52-Week High", "52_week_high", "price", None),
        ("52-Week Low", "52_week_low", "price", None),
        ("**VALUATION**", None, None, None),
        ("Market Cap", "market_cap", "number", True),
        ("Enterprise Value", "enterprise_value", "number", None),
        ("P/E (TTM)", "pe_trailing", "ratio", False),
        ("P/E (Forward)", "pe_forward", "ratio", False),
        ("EV/EBITDA", "ev_ebitda", "ratio", False),
        ("EV/Revenue", "ev_revenue", "ratio", False),
        ("P/B", "pb", "ratio", False),
        ("**FINANCIALS**", None, None, None),
        ("Revenue", "revenue", "number", True),
        ("Revenue Growth", "revenue_growth", "percent", True),
        ("Gross Margin", "gross_margin", "percent", True),
        ("Operating Margin", "operating_margin", "percent", True),
        ("Profit Margin", "profit_margin", "percent", True),
        ("EBITDA", "ebitda", "number", True),
        ("Net Income", "net_income", "number", True),
        ("Free Cash Flow", "fcf", "number", True),
        ("**RETURNS**", None, None, None),
        ("ROE", "roe", "percent", True),
        ("ROA", "roa", "percent", True),
        ("**BALANCE SHEET**", None, None, None),
        ("Debt/Equity", "debt_equity", "ratio", False),
        ("Current Ratio", "current_ratio", "ratio", True),
        ("**DIVIDENDS**", None, None, None),
        ("Dividend Yield", "dividend_yield", "percent", True),
        ("Payout Ratio", "payout_ratio", "percent", False),
        ("**RISK**", None, None, None),
        ("Beta", "beta", "default", None),
    ]

    for label, key, fmt, higher_is_better in metrics:
        if key is None:
            # Section header
            row = f"| {label} |" + " |" * len(data)
            lines.append(row)
            continue

        values = [d.get(key) for d in data]
        winner_idx = find_winner(values, higher_is_better) if higher_is_better is not None else -1

        row = f"| {label} |"
        for i, val in enumerate(values):
            formatted = format_value(val, fmt)
            if i == winner_idx and higher_is_better is not None:
                formatted = f"**{formatted}** ✓"
            row += f" {formatted} |"
        lines.append(row)

    # Summary
    lines.append("")
    lines.append("## Summary")
    lines.append("")

    # Count wins
    wins = {d['ticker']: 0 for d in data}
    for label, key, fmt, higher_is_better in metrics:
        if key is None or higher_is_better is None:
            continue
        values = [d.get(key) for d in data]
        winner_idx = find_winner(values, higher_is_better)
        if winner_idx >= 0:
            wins[data[winner_idx]['ticker']] += 1

    lines.append("| Ticker | Wins |")
    lines.append("|--------|------|")
    for ticker, win_count in sorted(wins.items(), key=lambda x: x[1], reverse=True):
        lines.append(f"| {ticker} | {win_count} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Compare stocks side by side")
    parser.add_argument("tickers", nargs="+", help="Stock tickers to compare")

    args = parser.parse_args()

    if len(args.tickers) < 2:
        print("Error: Need at least 2 tickers to compare")
        sys.exit(1)

    print(generate_comparison(args.tickers))


if __name__ == "__main__":
    main()
