# Notes

Development notes for Stock Research Agent.

## Origin

Created from the `researcher` blueprint, specialized for equity analysis with first-principles methodology.

## Purpose

Conduct professional-grade stock research that:
- Verifies every fact from primary sources
- Builds analysis from fundamentals, not assumptions
- Presents balanced bull/bear cases
- Quantifies uncertainty

## Key Differentiators

### vs Generic Research Agent
- Phased workflow (Init → Gather → Analyze → Synthesize)
- Financial modeling tools (DCF, ratios, multiples)
- SEC filing integration
- Structured output formats

### vs Human Analyst
- No confirmation bias
- Systematic source verification
- Explicit assumption documentation
- Reproducible methodology

## Workflow

```
┌─────────────────────────────────────────┐
│  Phase 1: Initialization                │
│  - Verify ticker, exchange              │
│  - Confirm market cap, price            │
│  - Identify latest filings              │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│  Phase 2: Data Gathering                │
│  - Pull 3-5 years financials (10-K)     │
│  - Research competitors                 │
│  - Industry context                     │
│  - Management commentary                │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│  Phase 3: Analysis                      │
│  - Deconstruct business model           │
│  - Calculate financial ratios           │
│  - Build DCF model                      │
│  - Identify moats and risks             │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│  Phase 4: Synthesis                     │
│  - Bull case with evidence              │
│  - Bear case with evidence              │
│  - Valuation range                      │
│  - Key uncertainties                    │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│  Phase 5: Iteration (ongoing)           │
│  - Monitor for new filings              │
│  - Update on earnings                   │
│  - Revise thesis as needed              │
└─────────────────────────────────────────┘
```

## Source Priority

| Priority | Source Type | Use For |
|----------|-------------|---------|
| 1 | SEC Filings (10-K, 10-Q) | All financial data |
| 2 | Earnings Transcripts | Management commentary |
| 3 | Company IR Site | Guidance, presentations |
| 4 | Industry Reports | Market size, trends |
| 5 | News/Analysts | Sentiment, catalysts |

## Output Templates

### Financial Summary Table
```
| Metric | 2021 | 2022 | 2023 | 2024E |
|--------|------|------|------|-------|
| Revenue ($M) | X | X | X | X |
| Gross Margin | X% | X% | X% | X% |
| EBITDA ($M) | X | X | X | X |
| Net Income ($M) | X | X | X | X |
| EPS | $X | $X | $X | $X |
```

### Competitor Comparison
```
| Metric | Company | Peer 1 | Peer 2 | Peer 3 |
|--------|---------|--------|--------|--------|
| Market Cap | $XB | $XB | $XB | $XB |
| Revenue | $XB | $XB | $XB | $XB |
| Gross Margin | X% | X% | X% | X% |
| EV/EBITDA | Xx | Xx | Xx | Xx |
```

### Valuation Summary
```
| Method | Value/Share | Implied Upside |
|--------|-------------|----------------|
| DCF (Base) | $X | X% |
| DCF (Bull) | $X | X% |
| DCF (Bear) | $X | X% |
| EV/EBITDA Comp | $X | X% |
| P/E Comp | $X | X% |
```

## Limitations

- **Data Freshness:** SEC filings lag real-time by weeks/months
- **Model Risk:** DCF highly sensitive to assumptions
- **Coverage Gaps:** Private competitors hard to analyze
- **Qualitative Factors:** Some moats hard to quantify

## Changelog

- Initial creation from researcher blueprint
- Added phased workflow (Init → Gather → Analyze → Synthesize)
- Added financial modeling tools (DCF, ratios)
- Added SEC filing integration
- Implemented first-principles methodology
