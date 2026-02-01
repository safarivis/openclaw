#!/usr/bin/env python3
"""
DCF Valuation Model
Calculates intrinsic value using Discounted Cash Flow analysis.

Usage:
    python dcf_model.py --fcf BASE_FCF --growth RATE --terminal RATE --wacc RATE --shares SHARES
    python dcf_model.py --ticker TICKER  # Auto-fetch data from yfinance

Examples:
    python dcf_model.py --fcf 170 --growth 0.04 --terminal 0.025 --wacc 0.085 --shares 65
    python dcf_model.py --ticker GOLF
    python dcf_model.py --ticker GOLF --wacc 0.09 --terminal 0.02
"""

import argparse
import json
import sys
from dataclasses import dataclass
from typing import List, Optional

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False


@dataclass
class DCFInputs:
    """DCF Model Inputs"""
    ticker: str
    base_fcf: float  # Base Free Cash Flow (in millions)
    growth_rates: List[float]  # Growth rates for projection years
    terminal_growth: float  # Terminal/perpetual growth rate
    wacc: float  # Weighted Average Cost of Capital
    shares_outstanding: float  # Shares outstanding (in millions)
    net_debt: float = 0  # Net debt (total debt - cash) in millions


@dataclass
class DCFResult:
    """DCF Model Results"""
    inputs: DCFInputs
    projected_fcfs: List[float]
    pv_fcfs: List[float]
    terminal_value: float
    pv_terminal: float
    enterprise_value: float
    equity_value: float
    intrinsic_value_per_share: float


def calculate_dcf(inputs: DCFInputs) -> DCFResult:
    """
    Calculate DCF valuation.

    Args:
        inputs: DCFInputs with all required parameters

    Returns:
        DCFResult with calculated values
    """
    projected_fcfs = []
    pv_fcfs = []

    # Project FCFs for each year
    current_fcf = inputs.base_fcf
    for i, growth_rate in enumerate(inputs.growth_rates):
        year = i + 1
        current_fcf = current_fcf * (1 + growth_rate)
        projected_fcfs.append(current_fcf)

        # Discount to present value
        discount_factor = (1 + inputs.wacc) ** year
        pv = current_fcf / discount_factor
        pv_fcfs.append(pv)

    # Terminal Value (Gordon Growth Model)
    final_year = len(inputs.growth_rates)
    terminal_fcf = projected_fcfs[-1] * (1 + inputs.terminal_growth)
    terminal_value = terminal_fcf / (inputs.wacc - inputs.terminal_growth)

    # Discount terminal value to present
    terminal_discount_factor = (1 + inputs.wacc) ** final_year
    pv_terminal = terminal_value / terminal_discount_factor

    # Enterprise Value = PV of FCFs + PV of Terminal Value
    enterprise_value = sum(pv_fcfs) + pv_terminal

    # Equity Value = Enterprise Value - Net Debt
    equity_value = enterprise_value - inputs.net_debt

    # Intrinsic Value per Share
    intrinsic_value = equity_value / inputs.shares_outstanding

    return DCFResult(
        inputs=inputs,
        projected_fcfs=projected_fcfs,
        pv_fcfs=pv_fcfs,
        terminal_value=terminal_value,
        pv_terminal=pv_terminal,
        enterprise_value=enterprise_value,
        equity_value=equity_value,
        intrinsic_value_per_share=intrinsic_value
    )


def sensitivity_analysis(inputs: DCFInputs,
                         wacc_range: List[float] = None,
                         terminal_range: List[float] = None) -> dict:
    """
    Run sensitivity analysis on WACC and terminal growth.

    Returns matrix of intrinsic values.
    """
    if wacc_range is None:
        wacc_range = [inputs.wacc - 0.01, inputs.wacc, inputs.wacc + 0.01]
    if terminal_range is None:
        terminal_range = [inputs.terminal_growth - 0.005, inputs.terminal_growth, inputs.terminal_growth + 0.005]

    matrix = {}
    for wacc in wacc_range:
        matrix[f"{wacc:.1%}"] = {}
        for tg in terminal_range:
            modified_inputs = DCFInputs(
                ticker=inputs.ticker,
                base_fcf=inputs.base_fcf,
                growth_rates=inputs.growth_rates,
                terminal_growth=tg,
                wacc=wacc,
                shares_outstanding=inputs.shares_outstanding,
                net_debt=inputs.net_debt
            )
            result = calculate_dcf(modified_inputs)
            matrix[f"{wacc:.1%}"][f"{tg:.1%}"] = round(result.intrinsic_value_per_share, 2)

    return matrix


def fetch_inputs_from_ticker(ticker: str,
                              wacc: float = 0.09,
                              terminal_growth: float = 0.025,
                              projection_years: int = 5,
                              growth_rate: float = None) -> DCFInputs:
    """
    Fetch DCF inputs from yfinance for a given ticker.
    """
    if not YFINANCE_AVAILABLE:
        raise ImportError("yfinance not installed. Run: pip install yfinance")

    stock = yf.Ticker(ticker)
    info = stock.info

    # Get FCF
    fcf = info.get('freeCashflow')
    if fcf is None:
        # Try to get from cash flow statement
        cf = stock.cashflow
        if cf is not None and not cf.empty and 'Free Cash Flow' in cf.index:
            fcf = float(cf.loc['Free Cash Flow'].iloc[0])

    if fcf is None:
        raise ValueError(f"Could not find Free Cash Flow for {ticker}")

    # Convert to millions
    fcf_millions = fcf / 1e6

    # Get shares outstanding
    shares = info.get('sharesOutstanding', 0) / 1e6  # Convert to millions

    # Get net debt
    total_debt = info.get('totalDebt', 0) or 0
    total_cash = info.get('totalCash', 0) or 0
    net_debt = (total_debt - total_cash) / 1e6  # Convert to millions

    # Estimate growth rate if not provided
    if growth_rate is None:
        revenue_growth = info.get('revenueGrowth')
        if revenue_growth:
            growth_rate = min(revenue_growth, 0.15)  # Cap at 15%
        else:
            growth_rate = 0.05  # Default 5%

    # Create growth rates (declining to terminal)
    growth_rates = []
    for i in range(projection_years):
        # Linear decline from growth_rate to terminal_growth
        decline_factor = i / projection_years
        year_growth = growth_rate * (1 - decline_factor) + terminal_growth * decline_factor
        growth_rates.append(year_growth)

    return DCFInputs(
        ticker=ticker,
        base_fcf=fcf_millions,
        growth_rates=growth_rates,
        terminal_growth=terminal_growth,
        wacc=wacc,
        shares_outstanding=shares,
        net_debt=net_debt
    )


def format_result(result: DCFResult, current_price: float = None) -> str:
    """Format DCF result as markdown."""
    lines = []
    lines.append(f"# DCF Valuation: {result.inputs.ticker}")
    lines.append("")

    # Inputs
    lines.append("## Inputs")
    lines.append(f"| Parameter | Value |")
    lines.append(f"|-----------|-------|")
    lines.append(f"| Base FCF | ${result.inputs.base_fcf:.1f}M |")
    lines.append(f"| Growth Rates | {', '.join([f'{g:.1%}' for g in result.inputs.growth_rates])} |")
    lines.append(f"| Terminal Growth | {result.inputs.terminal_growth:.1%} |")
    lines.append(f"| WACC | {result.inputs.wacc:.1%} |")
    lines.append(f"| Shares Outstanding | {result.inputs.shares_outstanding:.1f}M |")
    lines.append(f"| Net Debt | ${result.inputs.net_debt:.1f}M |")
    lines.append("")

    # Projections
    lines.append("## FCF Projections")
    lines.append(f"| Year | FCF | PV of FCF |")
    lines.append(f"|------|-----|-----------|")
    for i, (fcf, pv) in enumerate(zip(result.projected_fcfs, result.pv_fcfs)):
        lines.append(f"| {i+1} | ${fcf:.1f}M | ${pv:.1f}M |")
    lines.append("")

    # Valuation
    lines.append("## Valuation")
    lines.append(f"| Component | Value |")
    lines.append(f"|-----------|-------|")
    lines.append(f"| PV of FCFs | ${sum(result.pv_fcfs):.1f}M |")
    lines.append(f"| Terminal Value | ${result.terminal_value:.1f}M |")
    lines.append(f"| PV of Terminal | ${result.pv_terminal:.1f}M |")
    lines.append(f"| **Enterprise Value** | **${result.enterprise_value:.1f}M** |")
    lines.append(f"| Less: Net Debt | ${result.inputs.net_debt:.1f}M |")
    lines.append(f"| **Equity Value** | **${result.equity_value:.1f}M** |")
    lines.append(f"| **Intrinsic Value/Share** | **${result.intrinsic_value_per_share:.2f}** |")
    lines.append("")

    # Comparison to current price
    if current_price:
        upside = (result.intrinsic_value_per_share - current_price) / current_price
        status = "UNDERVALUED" if upside > 0.1 else "OVERVALUED" if upside < -0.1 else "FAIRLY VALUED"
        lines.append("## vs Current Price")
        lines.append(f"| Metric | Value |")
        lines.append(f"|--------|-------|")
        lines.append(f"| Current Price | ${current_price:.2f} |")
        lines.append(f"| Intrinsic Value | ${result.intrinsic_value_per_share:.2f} |")
        lines.append(f"| Upside/Downside | {upside:.1%} |")
        lines.append(f"| **Status** | **{status}** |")
        lines.append("")

    # Sensitivity
    lines.append("## Sensitivity Analysis")
    sens = sensitivity_analysis(result.inputs)

    # Header
    terminal_rates = list(list(sens.values())[0].keys())
    lines.append(f"| WACC \\ Terminal | {' | '.join(terminal_rates)} |")
    lines.append(f"|-----------------|{'|'.join(['-------'] * len(terminal_rates))}|")

    for wacc_label, terminal_values in sens.items():
        values = [f"${v:.0f}" for v in terminal_values.values()]
        lines.append(f"| {wacc_label} | {' | '.join(values)} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="DCF Valuation Model")

    # Option 1: Manual inputs
    parser.add_argument("--fcf", type=float, help="Base Free Cash Flow (in millions)")
    parser.add_argument("--growth", type=float, help="Annual growth rate (e.g., 0.05 for 5%)")
    parser.add_argument("--years", type=int, default=5, help="Projection years (default: 5)")

    # Option 2: Ticker-based (auto-fetch)
    parser.add_argument("--ticker", type=str, help="Stock ticker to fetch data from yfinance")

    # Common parameters
    parser.add_argument("--terminal", type=float, default=0.025, help="Terminal growth rate (default: 2.5%)")
    parser.add_argument("--wacc", type=float, default=0.09, help="WACC (default: 9%)")
    parser.add_argument("--shares", type=float, help="Shares outstanding (in millions)")
    parser.add_argument("--debt", type=float, default=0, help="Net debt (in millions)")
    parser.add_argument("--output", choices=["json", "markdown"], default="markdown")

    args = parser.parse_args()

    # Build inputs
    if args.ticker:
        # Fetch from yfinance
        inputs = fetch_inputs_from_ticker(
            args.ticker,
            wacc=args.wacc,
            terminal_growth=args.terminal,
            projection_years=args.years,
            growth_rate=args.growth
        )

        # Get current price for comparison
        stock = yf.Ticker(args.ticker)
        current_price = stock.info.get('currentPrice') or stock.info.get('regularMarketPrice')
    else:
        # Manual inputs
        if not all([args.fcf, args.growth, args.shares]):
            parser.error("Either --ticker OR (--fcf, --growth, --shares) required")

        growth_rates = [args.growth] * args.years
        inputs = DCFInputs(
            ticker="MANUAL",
            base_fcf=args.fcf,
            growth_rates=growth_rates,
            terminal_growth=args.terminal,
            wacc=args.wacc,
            shares_outstanding=args.shares,
            net_debt=args.debt
        )
        current_price = None

    # Calculate DCF
    result = calculate_dcf(inputs)

    # Output
    if args.output == "json":
        output = {
            "inputs": {
                "ticker": inputs.ticker,
                "base_fcf": inputs.base_fcf,
                "growth_rates": inputs.growth_rates,
                "terminal_growth": inputs.terminal_growth,
                "wacc": inputs.wacc,
                "shares_outstanding": inputs.shares_outstanding,
                "net_debt": inputs.net_debt
            },
            "results": {
                "projected_fcfs": result.projected_fcfs,
                "pv_fcfs": result.pv_fcfs,
                "terminal_value": result.terminal_value,
                "pv_terminal": result.pv_terminal,
                "enterprise_value": result.enterprise_value,
                "equity_value": result.equity_value,
                "intrinsic_value_per_share": result.intrinsic_value_per_share
            },
            "current_price": current_price,
            "sensitivity": sensitivity_analysis(inputs)
        }
        print(json.dumps(output, indent=2))
    else:
        print(format_result(result, current_price))


if __name__ == "__main__":
    main()
