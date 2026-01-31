# Brand Agent Memory

Persistent storage for brand decisions, guidelines, and lessons learned.

## Structure

```
memory/
├── README.md           ← This file
├── brand-strategy.md   ← Core positioning and pillars
├── voice-guide.md      ← Voice attributes and examples
├── decisions.md        ← Log of brand decisions with rationale
├── competitors.md      ← Competitive landscape analysis
└── lessons.md          ← What we've learned from successes/failures
```

## How Memory Works

### Automatic Persistence
After completing key tasks, save relevant outputs:

| Mode | What to Save | Where |
|------|--------------|-------|
| Strategy | Positioning, pillars, audience | `brand-strategy.md` |
| Voice | Voice attributes, do/don't examples | `voice-guide.md` |
| Competitor | Competitive analysis, positioning map | `competitors.md` |
| Review/Audit | Key decisions, changes made | `decisions.md` |
| Any | Insights from failures/successes | `lessons.md` |

### Before Starting Tasks
Load relevant context:
1. Always read `brand-strategy.md` (core positioning)
2. Read `voice-guide.md` for content tasks
3. Check `decisions.md` for past context
4. Review `lessons.md` to avoid repeating mistakes

### Memory Principles

1. **Write-through** - Save important outputs immediately
2. **Lessons learned** - Extract insights from failures
3. **Semantic** - Store facts and decisions, not full conversations
4. **Searchable** - Use clear headers for easy retrieval

## File Formats

### brand-strategy.md
```markdown
# Brand Strategy
Last updated: [date]

## Positioning Statement
[For X audience, we are Y that does Z, unlike competitors who W]

## Brand Pillars
1. [Pillar] - [Description]
2. [Pillar] - [Description]
3. [Pillar] - [Description]

## Target Audience
- Primary: [description]
- Secondary: [description]

## Competitive Position
[How we're different]
```

### voice-guide.md
```markdown
# Voice Guide
Last updated: [date]

## Voice Attributes
| Attribute | Description | Do | Don't |
|-----------|-------------|----|----- |
| [e.g., Confident] | [what it means] | [example] | [example] |

## Tone Variations
- Formal contexts: [guidance]
- Casual contexts: [guidance]
- Crisis contexts: [guidance]
```

### decisions.md
```markdown
# Brand Decisions Log

## [Date] - [Decision Title]
**Context:** [Why this came up]
**Decision:** [What we decided]
**Rationale:** [Why we chose this]
**Alternatives considered:** [What else we thought about]
**Impact:** [What this affects]
```

### lessons.md
```markdown
# Lessons Learned

## [Date] - [Lesson Title]
**Context:** [What happened]
**Outcome:** [Result - success or failure]
**Lesson:** [What we learned]
**Apply when:** [Future situations where this matters]
```
