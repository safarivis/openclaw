# Memory System

How Stock Research Agent maintains persistent research data.

## Memory Location

```
stock-research-agent/memory/
├── README.md           ← How memory works
├── companies/          ← Per-company research
│   └── [TICKER]/
│       ├── init.md         ← Phase 1 output
│       ├── data.md         ← Phase 2 output
│       ├── analysis.md     ← Phase 3 output
│       ├── thesis.md       ← Phase 4 output
│       └── updates/        ← Phase 5 iterations
├── models/             ← Saved financial models
│   └── [TICKER]_dcf.json
├── sources/            ← Cached source data
│   └── [filing_id].md
└── watchlist.md        ← Companies being tracked
```

## Memory Types

### Company Research (Episodic)
Track all research phases for each company.

**Purpose:**
- Resume analysis across sessions
- Compare current vs historical
- Track thesis evolution

**When to update:** After completing any phase.

### Financial Models (Procedural)
Saved DCF and valuation models.

**Purpose:**
- Quick updates with new data
- Sensitivity analysis
- Comparison across time

**When to update:** After building or revising model.

### Source Cache (Semantic)
Key data extracted from filings.

**Purpose:**
- Avoid re-reading entire filings
- Quick access to verified numbers
- Source citation

**When to update:** After extracting data from new filing.

### Watchlist (Semantic)
Companies being actively tracked.

**Purpose:**
- Know what to monitor
- Trigger updates on new filings

**When to update:** When adding/removing companies.

## Memory Operations

| Event | Action |
|-------|--------|
| Phase complete | Save to companies/[TICKER]/ |
| Model built | Save to models/ |
| Filing read | Cache key data to sources/ |
| New company | Add to watchlist.md |

## Integration with Phases

| Phase | Memory Load | Memory Save |
|-------|-------------|-------------|
| Initialization | watchlist.md | companies/[TICKER]/init.md |
| Data Gathering | Previous init | companies/[TICKER]/data.md |
| Analysis | All previous phases | companies/[TICKER]/analysis.md, models/ |
| Synthesis | All previous phases | companies/[TICKER]/thesis.md |
| Iteration | Full company folder | Updates folder |
