#!/usr/bin/env python3
"""
Stock Analysis Runner
Full analysis pipeline for a given ticker.

Usage:
    python analyze.py TICKER [--compare TICKER2] [--output-dir DIR]

Examples:
    python analyze.py GOLF
    python analyze.py GOLF --compare MODG
    python analyze.py AAPL --output-dir ./reports
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

# Import our modules
from fetch_stock_data import fetch_stock_data, to_markdown as data_to_markdown
from dcf_model import fetch_inputs_from_ticker, calculate_dcf, format_result as dcf_to_markdown
from compare_stocks import generate_comparison

try:
    import yfinance as yf
except ImportError:
    print("Error: yfinance not installed. Run: pip install yfinance")
    sys.exit(1)


def run_full_analysis(ticker: str, compare_ticker: str = None, output_dir: str = None) -> str:
    """Run complete analysis pipeline."""
    ticker = ticker.upper()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    sections = []
    sections.append(f"# Full Analysis: {ticker}")
    sections.append(f"\n**Generated:** {timestamp}")
    sections.append("\n---\n")

    # Phase 1: Basic Data
    print(f"[1/4] Fetching data for {ticker}...", file=sys.stderr)
    try:
        data = fetch_stock_data(ticker)
        sections.append("## Company Overview & Financials\n")
        sections.append(data_to_markdown(data))
        sections.append("\n---\n")
    except Exception as e:
        sections.append(f"## Error Fetching Data\n\n{e}\n")

    # Phase 2: DCF Valuation
    print(f"[2/4] Running DCF model...", file=sys.stderr)
    try:
        # Get current price
        stock = yf.Ticker(ticker)
        current_price = stock.info.get('currentPrice') or stock.info.get('regularMarketPrice')

        # Run DCF
        inputs = fetch_inputs_from_ticker(ticker)
        result = calculate_dcf(inputs)
        sections.append(dcf_to_markdown(result, current_price))
        sections.append("\n---\n")
    except Exception as e:
        sections.append(f"## DCF Model Error\n\n{e}\n\n---\n")

    # Phase 3: Comparison (if requested)
    if compare_ticker:
        print(f"[3/4] Comparing {ticker} vs {compare_ticker}...", file=sys.stderr)
        try:
            comparison = generate_comparison([ticker, compare_ticker.upper()])
            sections.append(comparison)
            sections.append("\n---\n")
        except Exception as e:
            sections.append(f"## Comparison Error\n\n{e}\n\n---\n")
    else:
        print(f"[3/4] Skipping comparison (no --compare specified)...", file=sys.stderr)

    # Phase 4: Summary
    print(f"[4/4] Generating summary...", file=sys.stderr)
    sections.append(generate_summary(ticker, data, result if 'result' in dir() else None, current_price if 'current_price' in dir() else None))

    report = "\n".join(sections)

    # Save to file if output_dir specified
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        filename = output_path / f"{ticker}_analysis_{datetime.now().strftime('%Y%m%d')}.md"
        with open(filename, 'w') as f:
            f.write(report)
        print(f"\nReport saved to: {filename}", file=sys.stderr)

    return report


def generate_summary(ticker: str, data: dict, dcf_result, current_price: float) -> str:
    """Generate investment summary."""
    lines = []
    lines.append("## Investment Summary")
    lines.append("")

    # Key metrics table
    lines.append("### Key Metrics")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")

    if data:
        val = data.get('valuation', {})
        fin = data.get('financials', {})

        def fmt_num(v):
            if v is None or v == "N/A":
                return "N/A"
            try:
                v = float(v)
                if abs(v) >= 1e9:
                    return f"${v/1e9:.1f}B"
                elif abs(v) >= 1e6:
                    return f"${v/1e6:.1f}M"
                return f"${v:,.0f}"
            except:
                return str(v)

        def fmt_pct(v):
            if v is None or v == "N/A":
                return "N/A"
            try:
                return f"{float(v)*100:.1f}%"
            except:
                return str(v)

        def fmt_ratio(v):
            if v is None or v == "N/A":
                return "N/A"
            try:
                return f"{float(v):.1f}x"
            except:
                return str(v)

        lines.append(f"| Market Cap | {fmt_num(val.get('market_cap'))} |")
        lines.append(f"| P/E | {fmt_ratio(val.get('pe_trailing'))} |")
        lines.append(f"| EV/EBITDA | {fmt_ratio(val.get('ev_to_ebitda'))} |")
        lines.append(f"| Revenue | {fmt_num(fin.get('revenue'))} |")
        lines.append(f"| Profit Margin | {fmt_pct(fin.get('profit_margin'))} |")
        lines.append(f"| ROE | {fmt_pct(fin.get('roe'))} |")

    # DCF conclusion
    if dcf_result and current_price:
        lines.append("")
        lines.append("### Valuation Assessment")
        lines.append("")

        iv = dcf_result.intrinsic_value_per_share
        upside = (iv - current_price) / current_price

        if upside > 0.20:
            verdict = "🟢 **UNDERVALUED** - Significant margin of safety"
        elif upside > 0:
            verdict = "🟡 **SLIGHTLY UNDERVALUED** - Limited upside"
        elif upside > -0.20:
            verdict = "🟡 **FAIRLY VALUED to SLIGHTLY OVERVALUED**"
        else:
            verdict = "🔴 **OVERVALUED** - Price exceeds intrinsic value"

        lines.append(f"| Current Price | ${current_price:.2f} |")
        lines.append(f"| DCF Intrinsic Value | ${iv:.2f} |")
        lines.append(f"| Upside/Downside | {upside:.1%} |")
        lines.append(f"| **Verdict** | {verdict} |")

    # Action recommendation
    lines.append("")
    lines.append("### Recommendation")
    lines.append("")

    if dcf_result and current_price:
        upside = (dcf_result.intrinsic_value_per_share - current_price) / current_price
        if upside > 0.20:
            lines.append("**BUY** - Stock trading below intrinsic value with margin of safety.")
        elif upside > 0:
            lines.append("**HOLD** - Fair value, wait for better entry or position size appropriately.")
        elif upside > -0.20:
            lines.append("**HOLD/TRIM** - Slightly overvalued, don't add at current levels.")
        else:
            lines.append("**AVOID/SELL** - Significantly overvalued, better opportunities elsewhere.")
    else:
        lines.append("*Unable to generate recommendation - insufficient data*")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Run full stock analysis")
    parser.add_argument("ticker", help="Stock ticker to analyze")
    parser.add_argument("--compare", help="Second ticker to compare against")
    parser.add_argument("--output-dir", help="Directory to save report")

    args = parser.parse_args()

    report = run_full_analysis(args.ticker, args.compare, args.output_dir)
    print(report)


if __name__ == "__main__":
    main()
