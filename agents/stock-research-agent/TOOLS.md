# Tools

Tools for comprehensive stock research and analysis.

---

## Python Scripts (scripts/)

Real, executable tools for automated analysis.

### fetch_stock_data.py
Fetch comprehensive financial data for any ticker.

**Usage:**
```bash
python scripts/fetch_stock_data.py TICKER [--output json|markdown]
```

**Examples:**
```bash
python scripts/fetch_stock_data.py GOLF
python scripts/fetch_stock_data.py AAPL --output json
```

**Returns:** Company info, price data, valuation metrics, financials, dividends

---

### dcf_model.py
Calculate intrinsic value using DCF analysis.

**Usage:**
```bash
# Auto-fetch from yfinance
python scripts/dcf_model.py --ticker TICKER [--wacc 0.09] [--terminal 0.025]

# Manual inputs
python scripts/dcf_model.py --fcf 170 --growth 0.04 --terminal 0.025 --wacc 0.085 --shares 65
```

**Examples:**
```bash
python scripts/dcf_model.py --ticker GOLF
python scripts/dcf_model.py --ticker GOLF --wacc 0.10 --terminal 0.02
```

**Returns:** Projected FCFs, present values, enterprise value, equity value, intrinsic value per share, sensitivity analysis

---

### compare_stocks.py
Compare two or more stocks side by side.

**Usage:**
```bash
python scripts/compare_stocks.py TICKER1 TICKER2 [TICKER3 ...]
```

**Examples:**
```bash
python scripts/compare_stocks.py GOLF MODG
python scripts/compare_stocks.py AAPL MSFT GOOGL
```

**Returns:** Side-by-side comparison with valuation, financials, returns, and winner highlighting

---

### analyze.py
Run complete analysis pipeline (data + DCF + comparison).

**Usage:**
```bash
python scripts/analyze.py TICKER [--compare TICKER2] [--output-dir DIR]
```

**Examples:**
```bash
python scripts/analyze.py GOLF
python scripts/analyze.py GOLF --compare MODG
python scripts/analyze.py GOLF --compare MODG --output-dir memory/companies/GOLF
```

**Returns:** Full markdown report with all phases

---

### sec_edgar.py
Fetch SEC EDGAR filings (10-K, 10-Q, 8-K, etc.).

**Usage:**
```bash
python scripts/sec_edgar.py TICKER [--type 10-K] [--limit 5]
```

**Examples:**
```bash
python scripts/sec_edgar.py GOLF
python scripts/sec_edgar.py AAPL --type 10-K --limit 3
python scripts/sec_edgar.py MSFT --type 8-K --limit 10
python scripts/sec_edgar.py GOLF --fetch 0  # Fetch content of first filing
python scripts/sec_edgar.py GOLF --fetch 0 --section risk  # Extract risk factors section
```

**Returns:** List of filings with dates, types, and direct links to SEC documents

---

### yahoo_news.py
Fetch recent news and upcoming events from Yahoo Finance.

**Usage:**
```bash
python scripts/yahoo_news.py TICKER [--limit 10] [--calendar]
```

**Examples:**
```bash
python scripts/yahoo_news.py GOLF
python scripts/yahoo_news.py AAPL --limit 20 --calendar
```

**Returns:** Categorized news (earnings, analyst, product, market), upcoming events (earnings date, dividends)

---

### analyst_ratings.py
Get analyst ratings, price targets, and recommendations.

**Usage:**
```bash
python scripts/analyst_ratings.py TICKER [--earnings]
```

**Examples:**
```bash
python scripts/analyst_ratings.py GOLF
python scripts/analyst_ratings.py AAPL --earnings
```

**Returns:** Price targets (high/low/mean), consensus rating, recent analyst actions, earnings estimates

---

### mcp_server.py
MCP server exposing all tools for Claude to call directly.

**Setup:**
Add to `~/.claude/mcp_servers.json`:
```json
{
  "stock-research": {
    "command": "python3",
    "args": ["/home/louisdup/clawd-lab/stock-research-agent/scripts/mcp_server.py"]
  }
}
```

**Available Tools via MCP:**
- `fetch_stock_data` - Get comprehensive financial data
- `run_dcf` - Calculate intrinsic value via DCF
- `compare_stocks` - Compare multiple stocks
- `get_sec_filings` - Fetch SEC EDGAR filings
- `get_news` - Fetch recent news
- `get_analyst_ratings` - Get analyst recommendations

---

## Web-Based Data Sources

### web_search
Search for company information, news, analysis.

**When to use:** Finding current info, locating SEC filings, industry reports
**Parameters:**
- query (string, required): Search terms
- site (string, optional): Limit to domain (e.g., "sec.gov", "reuters.com")

**Returns:**
```yaml
type: array
items:
  - title: string
  - url: string
  - snippet: string
```

### fetch_url
Read content from a specific URL.

**When to use:** Reading SEC filings, company pages, articles
**Parameters:**
- url (string, required): Page URL

**Returns:**
```yaml
type: object
properties:
  content: string - Page content
  title: string - Page title
  date: string | null - Publication date
```

**Key URLs for Stock Research:**
- SEC EDGAR: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[ticker]`
- Company IR: `https://investor.[company].com`
- Yahoo Finance: `https://finance.yahoo.com/quote/[ticker]`

### search_sec_filings
Search SEC EDGAR for company filings.

**When to use:** Finding 10-K, 10-Q, 8-K, proxy statements
**Parameters:**
- ticker (string, required): Stock symbol
- filing_type (enum, optional): "10-K" | "10-Q" | "8-K" | "DEF 14A" | "all"
- years (integer, optional): How many years back (default: 3)

**Returns:**
```yaml
type: array
items:
  - filing_type: string
  - filing_date: string
  - url: string
```

### search_earnings_transcripts
Find earnings call transcripts.

**When to use:** Understanding management commentary, guidance
**Parameters:**
- ticker (string, required): Stock symbol
- quarters (integer, optional): How many quarters back (default: 4)

**Returns:**
```yaml
type: array
items:
  - quarter: string (e.g., "Q3 2024")
  - date: string
  - url: string
```

---

## Financial Modeling

### calculate_ratios
Calculate financial ratios from inputs.

**When to use:** Analyzing profitability, leverage, liquidity
**Parameters:**
- financials (object, required): Income statement, balance sheet, cash flow data

**Returns:**
```yaml
type: object
properties:
  profitability:
    gross_margin: number
    operating_margin: number
    net_margin: number
    roe: number
    roic: number
  leverage:
    debt_to_equity: number
    net_debt_to_ebitda: number
  liquidity:
    current_ratio: number
    quick_ratio: number
  efficiency:
    asset_turnover: number
    inventory_days: number
```

**Python Implementation:**
```python
def calculate_ratios(financials):
    income = financials['income_statement']
    balance = financials['balance_sheet']

    ratios = {
        'profitability': {
            'gross_margin': income['gross_profit'] / income['revenue'],
            'operating_margin': income['operating_income'] / income['revenue'],
            'net_margin': income['net_income'] / income['revenue'],
            'roe': income['net_income'] / balance['shareholders_equity'],
            'roic': income['nopat'] / balance['invested_capital'],
        },
        'leverage': {
            'debt_to_equity': balance['total_debt'] / balance['shareholders_equity'],
            'net_debt_to_ebitda': (balance['total_debt'] - balance['cash']) / income['ebitda'],
        },
        'liquidity': {
            'current_ratio': balance['current_assets'] / balance['current_liabilities'],
            'quick_ratio': (balance['current_assets'] - balance['inventory']) / balance['current_liabilities'],
        }
    }
    return ratios
```

### build_dcf_model
Build discounted cash flow valuation.

**When to use:** Estimating intrinsic value
**Parameters:**
- fcf_base (number, required): Latest free cash flow
- growth_rates (array, required): Projected growth rates by year
- terminal_growth (number, required): Long-term growth rate
- wacc (number, required): Discount rate
- shares_outstanding (number, required): Share count

**Returns:**
```yaml
type: object
properties:
  enterprise_value: number
  equity_value: number
  per_share_value: number
  sensitivity_table: array - Values at different WACC/growth combos
```

**Python Implementation:**
```python
def dcf_model(fcf_base, growth_rates, terminal_growth, wacc, shares):
    # Project FCF
    fcfs = [fcf_base]
    for g in growth_rates:
        fcfs.append(fcfs[-1] * (1 + g))

    # Terminal value
    terminal_fcf = fcfs[-1] * (1 + terminal_growth)
    terminal_value = terminal_fcf / (wacc - terminal_growth)

    # Discount to present
    pv_fcfs = sum(fcf / (1 + wacc)**i for i, fcf in enumerate(fcfs[1:], 1))
    pv_terminal = terminal_value / (1 + wacc)**len(growth_rates)

    ev = pv_fcfs + pv_terminal
    equity_value = ev - net_debt
    per_share = equity_value / shares

    return {
        'enterprise_value': ev,
        'equity_value': equity_value,
        'per_share_value': per_share
    }
```

### compare_multiples
Compare valuation multiples to peers.

**When to use:** Relative valuation, sanity check on DCF
**Parameters:**
- target (object, required): Target company metrics
- peers (array, required): Peer company metrics

**Returns:**
```yaml
type: object
properties:
  target_multiples:
    ev_revenue: number
    ev_ebitda: number
    pe: number
  peer_median:
    ev_revenue: number
    ev_ebitda: number
    pe: number
  premium_discount: object - % vs peer median
```

---

## Sentiment Analysis

### search_social_sentiment
Search social media for stock sentiment.

**When to use:** Gauging retail sentiment, finding news catalysts
**Parameters:**
- ticker (string, required): Stock symbol
- platform (enum, optional): "twitter" | "reddit" | "all"
- days (integer, optional): Lookback period (default: 7)

**Returns:**
```yaml
type: object
properties:
  sentiment_score: number - -1 to 1
  mention_count: integer
  key_topics: array
  sample_posts: array
```

### get_analyst_ratings
Aggregate analyst recommendations.

**When to use:** Understanding Wall Street consensus
**Parameters:**
- ticker (string, required): Stock symbol

**Returns:**
```yaml
type: object
properties:
  consensus: string - "Buy" | "Hold" | "Sell"
  average_target: number
  high_target: number
  low_target: number
  analyst_count: integer
```

---

## Memory Operations

### save_research
Save research findings to memory.

**When to use:** Persisting analysis for future reference
**Parameters:**
- ticker (string, required): Stock symbol
- phase (string, required): Which phase of analysis
- data (object, required): Research data to save

### load_research
Load previous research from memory.

**When to use:** Continuing analysis, updating thesis
**Parameters:**
- ticker (string, required): Stock symbol
- phase (string, optional): Specific phase or all

---

## Tool Usage Guidelines

1. **Always start with SEC filings** - Primary source for financials
2. **Verify news with filings** - News can be wrong or outdated
3. **Use multiple valuation methods** - DCF + multiples + other
4. **Document all assumptions** - Every model input needs justification
5. **Save progress to memory** - Enable iteration and updates
