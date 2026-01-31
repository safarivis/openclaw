# Memory System

How Agent Reviewer maintains persistent knowledge.

## Memory Location

```
agent-reviewer/memory/
├── README.md      ← How memory works
├── reviews.md     ← All reviews conducted
└── patterns.md    ← Common issue patterns
```

## Memory Types

### Reviews (Episodic)
Track every review conducted.

**Purpose:**
- Reference past reviews
- Track improvement over time
- Compare agents

**When to update:** After completing any review.

### Patterns (Semantic)
Common issues that recur across agents.

**Purpose:**
- Quickly spot known issues
- Standardize fixes
- Improve review efficiency

**When to update:** When same issue appears 3+ times.

## Memory Operations

| Event | Action |
|-------|--------|
| Review completed | Add to reviews.md |
| Issue recurs | Update patterns.md frequency |
| New pattern found | Add to patterns.md |
