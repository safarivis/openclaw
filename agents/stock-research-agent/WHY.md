# Why This Agent Exists

## Problem Statement

Stock research is time-consuming and scattered across multiple sources. Manually gathering financials, analyst ratings, SEC filings, and news takes hours. Without systematic methodology, analysis quality varies and key data gets missed.

## Target Users

- Individual investors researching stocks
- Anyone asking "analyze [TICKER] for me"
- Portfolio managers needing quick briefs

**Current workflow without this agent:**
1. Visit Yahoo Finance, SEC EDGAR, news sites separately
2. Manually compile data into notes
3. Run DCF in spreadsheet
4. Miss important context
5. Takes 2-4 hours per stock

## Success Criteria

| Criteria | Target | How to Measure |
|----------|--------|----------------|
| Time savings | < 5 min for full analysis | Compare to manual |
| Data completeness | All major sources covered | Checklist verification |
| Accuracy | Financials match source data | Spot check against Yahoo |

## Constraints

- Never give specific buy/sell advice (not a financial advisor)
- Always cite data sources
- Acknowledge DCF limitations for certain company types
- Don't store sensitive API keys in code

## Key Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| 5-phase methodology | Initialize→Gather→Analyze→Synthesize→Iterate | Systematic, complete |
| yfinance for data | Free, reliable, comprehensive | No API key needed |
| DCF + comparables | Multiple valuation methods | More robust |
| MCP integration | Tools callable by Claude | Seamless workflow |

## Out of Scope

- Real-time trading signals
- Portfolio management
- Options/derivatives analysis
- Crypto assets

---

**Status:** Approved
**Date:** 2026-02-01
