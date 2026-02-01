#!/usr/bin/env python3
"""
Stock Data Fetcher
Fetches financial data for a given ticker using yfinance.

Usage:
    python fetch_stock_data.py TICKER [--output json|markdown]

Examples:
    python fetch_stock_data.py GOLF
    python fetch_stock_data.py AAPL --output json
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


def fetch_stock_data(ticker: str) -> dict:
    """Fetch comprehensive stock data for a ticker."""
    stock = yf.Ticker(ticker)

    data = {
        "ticker": ticker,
        "fetched_at": datetime.now().isoformat(),
        "info": {},
        "financials": {},
        "valuation": {},
        "dividends": {},
        "price": {},
        "errors": []
    }

    try:
        info = stock.info

        # Company Info
        data["info"] = {
            "name": info.get("longName", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
            "country": info.get("country", "N/A"),
            "employees": info.get("fullTimeEmployees", "N/A"),
            "website": info.get("website", "N/A"),
            "description": info.get("longBusinessSummary", "N/A")[:500] + "..." if info.get("longBusinessSummary") else "N/A"
        }

        # Price Data
        data["price"] = {
            "current": info.get("currentPrice") or info.get("regularMarketPrice", "N/A"),
            "previous_close": info.get("previousClose", "N/A"),
            "open": info.get("open") or info.get("regularMarketOpen", "N/A"),
            "day_high": info.get("dayHigh") or info.get("regularMarketDayHigh", "N/A"),
            "day_low": info.get("dayLow") or info.get("regularMarketDayLow", "N/A"),
            "52_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
            "52_week_low": info.get("fiftyTwoWeekLow", "N/A"),
            "50_day_avg": info.get("fiftyDayAverage", "N/A"),
            "200_day_avg": info.get("twoHundredDayAverage", "N/A"),
            "volume": info.get("volume") or info.get("regularMarketVolume", "N/A"),
            "avg_volume": info.get("averageVolume", "N/A")
        }

        # Valuation Metrics
        data["valuation"] = {
            "market_cap": info.get("marketCap", "N/A"),
            "enterprise_value": info.get("enterpriseValue", "N/A"),
            "pe_trailing": info.get("trailingPE", "N/A"),
            "pe_forward": info.get("forwardPE", "N/A"),
            "peg_ratio": info.get("pegRatio", "N/A"),
            "price_to_book": info.get("priceToBook", "N/A"),
            "price_to_sales": info.get("priceToSalesTrailing12Months", "N/A"),
            "ev_to_revenue": info.get("enterpriseToRevenue", "N/A"),
            "ev_to_ebitda": info.get("enterpriseToEbitda", "N/A")
        }

        # Financial Metrics
        data["financials"] = {
            "revenue": info.get("totalRevenue", "N/A"),
            "revenue_growth": info.get("revenueGrowth", "N/A"),
            "gross_profit": info.get("grossProfits", "N/A"),
            "gross_margin": info.get("grossMargins", "N/A"),
            "operating_margin": info.get("operatingMargins", "N/A"),
            "profit_margin": info.get("profitMargins", "N/A"),
            "ebitda": info.get("ebitda", "N/A"),
            "net_income": info.get("netIncomeToCommon", "N/A"),
            "eps_trailing": info.get("trailingEps", "N/A"),
            "eps_forward": info.get("forwardEps", "N/A"),
            "free_cash_flow": info.get("freeCashflow", "N/A"),
            "operating_cash_flow": info.get("operatingCashflow", "N/A"),
            "total_cash": info.get("totalCash", "N/A"),
            "total_debt": info.get("totalDebt", "N/A"),
            "debt_to_equity": info.get("debtToEquity", "N/A"),
            "current_ratio": info.get("currentRatio", "N/A"),
            "quick_ratio": info.get("quickRatio", "N/A"),
            "roe": info.get("returnOnEquity", "N/A"),
            "roa": info.get("returnOnAssets", "N/A"),
            "book_value": info.get("bookValue", "N/A"),
            "shares_outstanding": info.get("sharesOutstanding", "N/A")
        }

        # Dividend Info
        data["dividends"] = {
            "dividend_rate": info.get("dividendRate", "N/A"),
            "dividend_yield": info.get("dividendYield", "N/A"),
            "payout_ratio": info.get("payoutRatio", "N/A"),
            "ex_dividend_date": info.get("exDividendDate", "N/A"),
            "five_year_avg_yield": info.get("fiveYearAvgDividendYield", "N/A")
        }

    except Exception as e:
        data["errors"].append(f"Error fetching info: {str(e)}")

    # Get historical financials
    try:
        income_stmt = stock.income_stmt
        if income_stmt is not None and not income_stmt.empty:
            latest_year = income_stmt.columns[0]
            data["income_statement"] = {
                "period": str(latest_year),
                "total_revenue": _safe_get(income_stmt, "Total Revenue", latest_year),
                "gross_profit": _safe_get(income_stmt, "Gross Profit", latest_year),
                "operating_income": _safe_get(income_stmt, "Operating Income", latest_year),
                "net_income": _safe_get(income_stmt, "Net Income", latest_year),
                "ebitda": _safe_get(income_stmt, "EBITDA", latest_year)
            }
    except Exception as e:
        data["errors"].append(f"Error fetching income statement: {str(e)}")

    try:
        balance = stock.balance_sheet
        if balance is not None and not balance.empty:
            latest = balance.columns[0]
            data["balance_sheet"] = {
                "period": str(latest),
                "total_assets": _safe_get(balance, "Total Assets", latest),
                "total_liabilities": _safe_get(balance, "Total Liabilities Net Minority Interest", latest),
                "total_equity": _safe_get(balance, "Total Equity Gross Minority Interest", latest),
                "cash": _safe_get(balance, "Cash And Cash Equivalents", latest),
                "total_debt": _safe_get(balance, "Total Debt", latest)
            }
    except Exception as e:
        data["errors"].append(f"Error fetching balance sheet: {str(e)}")

    try:
        cashflow = stock.cashflow
        if cashflow is not None and not cashflow.empty:
            latest = cashflow.columns[0]
            data["cash_flow"] = {
                "period": str(latest),
                "operating_cf": _safe_get(cashflow, "Operating Cash Flow", latest),
                "investing_cf": _safe_get(cashflow, "Investing Cash Flow", latest),
                "financing_cf": _safe_get(cashflow, "Financing Cash Flow", latest),
                "free_cash_flow": _safe_get(cashflow, "Free Cash Flow", latest),
                "capex": _safe_get(cashflow, "Capital Expenditure", latest)
            }
    except Exception as e:
        data["errors"].append(f"Error fetching cash flow: {str(e)}")

    return data


def _safe_get(df, row_name, col):
    """Safely get a value from a DataFrame."""
    try:
        if row_name in df.index:
            val = df.loc[row_name, col]
            if val is not None and str(val) != 'nan':
                return float(val)
    except:
        pass
    return "N/A"


def format_number(val):
    """Format large numbers for display."""
    if val == "N/A" or val is None:
        return "N/A"
    try:
        val = float(val)
        if abs(val) >= 1e12:
            return f"${val/1e12:.2f}T"
        elif abs(val) >= 1e9:
            return f"${val/1e9:.2f}B"
        elif abs(val) >= 1e6:
            return f"${val/1e6:.2f}M"
        elif abs(val) >= 1e3:
            return f"${val/1e3:.2f}K"
        else:
            return f"${val:.2f}"
    except:
        return str(val)


def format_percent(val):
    """Format as percentage."""
    if val == "N/A" or val is None:
        return "N/A"
    try:
        v = float(val)
        # yfinance sometimes returns values > 1 that should be decimals
        # e.g. dividend yield of 0.98 should be 0.98%, not 98%
        if v > 1:
            return f"{v:.2f}%"  # Already a percentage
        return f"{v*100:.2f}%"
    except:
        return str(val)


def format_ratio(val):
    """Format as ratio."""
    if val == "N/A" or val is None:
        return "N/A"
    try:
        return f"{float(val):.2f}x"
    except:
        return str(val)


def to_markdown(data: dict) -> str:
    """Convert data to markdown report."""
    md = []
    md.append(f"# {data['info'].get('name', data['ticker'])} ({data['ticker']})")
    md.append(f"\n**Fetched:** {data['fetched_at']}")
    md.append(f"\n**Sector:** {data['info'].get('sector', 'N/A')} | **Industry:** {data['info'].get('industry', 'N/A')}")

    # Price
    md.append("\n## Price")
    md.append(f"| Metric | Value |")
    md.append(f"|--------|-------|")
    md.append(f"| Current Price | ${data['price'].get('current', 'N/A')} |")
    md.append(f"| 52-Week High | ${data['price'].get('52_week_high', 'N/A')} |")
    md.append(f"| 52-Week Low | ${data['price'].get('52_week_low', 'N/A')} |")
    md.append(f"| 50-Day Avg | ${data['price'].get('50_day_avg', 'N/A')} |")

    # Valuation
    md.append("\n## Valuation")
    md.append(f"| Metric | Value |")
    md.append(f"|--------|-------|")
    md.append(f"| Market Cap | {format_number(data['valuation'].get('market_cap'))} |")
    md.append(f"| Enterprise Value | {format_number(data['valuation'].get('enterprise_value'))} |")
    md.append(f"| P/E (TTM) | {format_ratio(data['valuation'].get('pe_trailing'))} |")
    md.append(f"| P/E (Forward) | {format_ratio(data['valuation'].get('pe_forward'))} |")
    md.append(f"| EV/EBITDA | {format_ratio(data['valuation'].get('ev_to_ebitda'))} |")
    md.append(f"| EV/Revenue | {format_ratio(data['valuation'].get('ev_to_revenue'))} |")
    md.append(f"| P/B | {format_ratio(data['valuation'].get('price_to_book'))} |")
    md.append(f"| PEG | {format_ratio(data['valuation'].get('peg_ratio'))} |")

    # Financials
    md.append("\n## Financials")
    md.append(f"| Metric | Value |")
    md.append(f"|--------|-------|")
    md.append(f"| Revenue | {format_number(data['financials'].get('revenue'))} |")
    md.append(f"| Revenue Growth | {format_percent(data['financials'].get('revenue_growth'))} |")
    md.append(f"| Gross Margin | {format_percent(data['financials'].get('gross_margin'))} |")
    md.append(f"| Operating Margin | {format_percent(data['financials'].get('operating_margin'))} |")
    md.append(f"| Profit Margin | {format_percent(data['financials'].get('profit_margin'))} |")
    md.append(f"| EBITDA | {format_number(data['financials'].get('ebitda'))} |")
    md.append(f"| Net Income | {format_number(data['financials'].get('net_income'))} |")
    md.append(f"| EPS (TTM) | ${data['financials'].get('eps_trailing', 'N/A')} |")
    md.append(f"| Free Cash Flow | {format_number(data['financials'].get('free_cash_flow'))} |")

    # Balance Sheet
    md.append("\n## Balance Sheet")
    md.append(f"| Metric | Value |")
    md.append(f"|--------|-------|")
    md.append(f"| Total Cash | {format_number(data['financials'].get('total_cash'))} |")
    md.append(f"| Total Debt | {format_number(data['financials'].get('total_debt'))} |")
    md.append(f"| Debt/Equity | {format_ratio(data['financials'].get('debt_to_equity'))} |")
    md.append(f"| Current Ratio | {format_ratio(data['financials'].get('current_ratio'))} |")
    md.append(f"| ROE | {format_percent(data['financials'].get('roe'))} |")
    md.append(f"| ROA | {format_percent(data['financials'].get('roa'))} |")

    # Dividends
    if data['dividends'].get('dividend_yield') and data['dividends'].get('dividend_yield') != "N/A":
        md.append("\n## Dividends")
        md.append(f"| Metric | Value |")
        md.append(f"|--------|-------|")
        md.append(f"| Dividend Rate | ${data['dividends'].get('dividend_rate', 'N/A')} |")
        md.append(f"| Dividend Yield | {format_percent(data['dividends'].get('dividend_yield'))} |")
        md.append(f"| Payout Ratio | {format_percent(data['dividends'].get('payout_ratio'))} |")

    # Errors
    if data.get('errors'):
        md.append("\n## Warnings")
        for err in data['errors']:
            md.append(f"- {err}")

    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser(description="Fetch stock data")
    parser.add_argument("ticker", help="Stock ticker symbol")
    parser.add_argument("--output", choices=["json", "markdown"], default="markdown",
                        help="Output format (default: markdown)")

    args = parser.parse_args()

    data = fetch_stock_data(args.ticker.upper())

    if args.output == "json":
        print(json.dumps(data, indent=2, default=str))
    else:
        print(to_markdown(data))


if __name__ == "__main__":
    main()
