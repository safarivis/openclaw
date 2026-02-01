# Stock Research Agent Memory

Persistent storage for equity research.

## Structure

```
memory/
├── companies/      ← Per-company research
├── models/         ← Saved financial models
├── sources/        ← Cached filing data
└── watchlist.md    ← Companies being tracked
```

## Usage

- Each company gets its own folder under `companies/`
- Models are saved as JSON for easy updating
- Sources are cached to avoid re-reading filings
