# Memory

How I persist and recall brand information across sessions.

## Memory Location

All brand memory is stored in: `./memory/`

## Memory Files

| File | Purpose | Load When |
|------|---------|-----------|
| `brand-strategy.md` | Core positioning, pillars, audience | Always (before any task) |
| `voice-guide.md` | Voice attributes, tone, word choices | Content tasks (Review, Voice, Campaign) |
| `decisions.md` | Past decisions with rationale | When context needed, before major decisions |
| `competitors.md` | Competitive landscape analysis | Competitor Mode, Strategy updates |
| `lessons.md` | What we've learned | Before similar tasks, when stuck |

## Memory Operations

### Load (Before Task)
```
1. Always read brand-strategy.md first
2. Load mode-specific files (see table above)
3. Check decisions.md if task relates to past work
4. Review lessons.md for relevant insights
```

### Save (After Task)
```
1. Update relevant memory file with new information
2. Log significant decisions to decisions.md
3. Extract lessons from failures to lessons.md
4. Note the date of last update
```

## What to Remember

### Always Save
- Positioning statements and pillars (Strategy Mode)
- Voice attributes and guidelines (Voice Mode)
- Competitive analysis (Competitor Mode)
- Significant brand decisions with rationale

### Optionally Save
- Campaign-specific guidelines (if reusable)
- Audit findings (if patterns emerge)
- Review feedback (if reveals brand gap)

### Never Save
- Full conversation history (too verbose)
- Temporary working notes
- Personal user information

## Memory Hygiene

### Keep Current
- Update `Last updated:` dates when modifying
- Review and consolidate quarterly
- Archive outdated competitive analysis

### Avoid Conflicts
- Check existing content before overwriting
- Append to decisions.md, don't replace
- Flag contradictions for human review

### Handle Staleness
- Competitive analysis: refresh every 3-6 months
- Strategy: stable unless business changes
- Voice: stable unless rebrand
- Lessons: always relevant, accumulate over time

## Integration with Modes

### Strategy Mode
- **Load:** brand-strategy.md, competitors.md
- **Save:** Update brand-strategy.md with new positioning

### Voice Mode
- **Load:** brand-strategy.md, voice-guide.md
- **Save:** Update voice-guide.md with new guidelines

### Review Mode
- **Load:** brand-strategy.md, voice-guide.md
- **Save:** Log significant feedback patterns to lessons.md

### Competitor Mode
- **Load:** brand-strategy.md, competitors.md
- **Save:** Update competitors.md with new analysis

### Campaign Mode
- **Load:** brand-strategy.md, voice-guide.md, competitors.md
- **Save:** Log campaign decisions to decisions.md

### Audit Mode
- **Load:** All memory files
- **Save:** Log findings to decisions.md, patterns to lessons.md
