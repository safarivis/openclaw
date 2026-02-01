# Agents / Modes

Operating modes for stock research tasks.

## Phase 1: Initialization Mode

Verify company basics before deep research.

**Trigger:** New company analysis, "analyze [ticker]"

**Context Load:**
- `memory/companies/` - Check if previously analyzed
- `memory/templates/` - Load analysis framework

**Approach:**
1. Verify ticker, exchange, company name
2. Confirm current market cap, share price
3. Identify latest SEC filings available
4. Note fiscal year end, reporting schedule
5. Identify business segments from 10-K

**Output:**
```
Company: [Name]
Ticker: [Symbol] on [Exchange]
Market Cap: $[X]B as of [date]
Share Price: $[X] as of [date]
Latest 10-K: [date]
Latest 10-Q: [date]
Business Segments: [list]
```

**Done when:**
- All basics verified from primary sources
- Latest filings identified
- Ready for data gathering

---

## Phase 2: Data Gathering Mode

Systematic collection from multiple sources.

**Trigger:** "gather data", after initialization

**Context Load:**
- Initialization output
- `memory/sources/` - Reuse cached data if fresh

**Approach:**
1. **Financials:** Pull 3-5 years from 10-Ks
   - Revenue by segment
   - Gross/operating/net margins
   - Balance sheet (assets, liabilities, equity)
   - Cash flow (operating, investing, financing)
2. **Competitive:** Research top 3-5 competitors
   - Market share estimates
   - Revenue/margin comparison
3. **Industry:** Find market size, growth rates
4. **Management:** Recent earnings calls, strategy
5. **Sentiment:** Analyst ratings, social media

**Output:** Structured data tables with sources

**Done when:**
- 3+ years of financials extracted
- Competitor data gathered
- Industry context established
- All data has source citations

---

## Phase 3: Analysis Mode

First-principles breakdown and financial modeling.

**Trigger:** "analyze", after data gathering

**Context Load:**
- All gathered data
- `memory/models/` - Previous models if updating

**Approach:**
1. **Deconstruct Business:**
   - Revenue drivers (volume × price)
   - Cost structure (fixed vs variable)
   - Capital intensity
   - Working capital needs
2. **Calculate Ratios:**
   - Profitability: Gross margin, EBIT margin, ROE, ROIC
   - Leverage: Debt/Equity, Net Debt/EBITDA
   - Liquidity: Current ratio, Quick ratio
   - Efficiency: Asset turnover, Inventory days
3. **Build Valuation Model:**
   - DCF with explicit assumptions
   - Trading comparables
   - Sensitivity analysis
4. **Identify Moats/Risks:**
   - Competitive advantages
   - Key risk factors

**Output:**
- Ratio analysis table
- DCF model with assumptions
- Valuation summary
- Risk matrix

**Done when:**
- All ratios calculated with sources
- DCF model complete with sensitivities
- Risks quantified where possible

---

## Phase 4: Synthesis Mode

Combine findings into balanced conclusions.

**Trigger:** "synthesize", after analysis

**Context Load:**
- All analysis output
- `memory/thesis/` - Previous thesis if updating

**Approach:**
1. Summarize key findings
2. Build bull case with evidence
3. Build bear case with evidence
4. Identify key uncertainties
5. State what would change thesis
6. Compare to current valuation

**Output:**
```
## Investment Thesis

### Summary
[1-2 paragraph overview]

### Bull Case
- [Point 1 with evidence]
- [Point 2 with evidence]

### Bear Case
- [Point 1 with evidence]
- [Point 2 with evidence]

### Key Uncertainties
- [Uncertainty 1]
- [Uncertainty 2]

### Valuation
- Current: $X (Y.Zx EV/EBITDA)
- Fair Value Range: $A - $B
- Implied upside/downside: X% to Y%

### What Would Change My View
- Bull → Bear: [triggers]
- Bear → Bull: [triggers]
```

**Done when:**
- Both cases presented fairly
- Valuation range established
- Uncertainties acknowledged
- Thesis is actionable

---

## Phase 5: Iteration Mode

Refine analysis based on new information.

**Trigger:** New filings, earnings, "update analysis"

**Context Load:**
- Previous analysis from memory
- New data sources

**Approach:**
1. Identify what's changed
2. Update relevant data
3. Re-run affected models
4. Revise thesis if warranted
5. Document changes

**Output:** Updated analysis with change log

**Done when:**
- New data incorporated
- Models updated
- Thesis revised if needed
- Changes documented

---

## Mode Selection

Modes run sequentially for new analysis:
`Initialization → Data Gathering → Analysis → Synthesis`

For updates: `Iteration` mode only.

Specify explicitly:
- "Phase 1: Initialize analysis of CALY"
- "Phase 2: Gather all financial data"
- "Phase 3: Run full analysis"
- "Phase 4: Synthesize and conclude"
- "Update: New Q3 earnings released"
