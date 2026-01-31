# Agent Reviewer Notes

## Origin

Created from the `researcher` blueprint, specialized for agent quality assurance.

## Purpose

Quality gate in the Agent Factory workflow:
```
Agent Builder creates → Agent Reviewer validates → Iterate if needed → Deploy
```

## Key Customizations from Researcher Blueprint

| Original | Customized |
|----------|------------|
| Web search focus | Workspace analysis focus |
| External sources | Knowledge base as source |
| General research modes | Review-specific modes |
| Citation tracking | Principle referencing |

## Review Scoring System

### Overall Score (1-10)

| Score | Meaning |
|-------|---------|
| 9-10 | Excellent - Ready for production |
| 7-8 | Good - Minor improvements suggested |
| 5-6 | Acceptable - Notable issues to address |
| 3-4 | Needs Work - Significant problems |
| 1-2 | Not Ready - Major rework required |

### Per-File Scoring

Each file scored 1-10 on:
- **Completeness** - All expected sections present
- **Clarity** - Easy to understand
- **Specificity** - Concrete, not vague
- **Alignment** - Follows knowledge base principles
- **Usefulness** - Actually helps the agent work

## Standard Review Process

1. **Load workspace** - Read all .md files
2. **Load criteria** - Relevant knowledge base sections
3. **Per-file review** - Score and comment each file
4. **Cross-file check** - Consistency across files
5. **Overall assessment** - Weighted score and summary
6. **Prioritized recommendations** - Top 3 improvements

## Common Issues I Flag

### IDENTITY.md
- Missing "What I'm Not" section
- Vague expertise claims
- No clear mission statement
- Approach that doesn't match expertise

### SOUL.md
- Generic values (could apply to any agent)
- Platitudes without actionable guidance
- Values that contradict each other
- Missing domain-specific principles

### AGENTS.md
- Modes without clear triggers
- Overlapping modes (confusing selection)
- Missing output specifications
- No examples provided

### TOOLS.md
- Tools that do multiple things
- Vague descriptions
- Missing parameter documentation
- No usage guidelines

### NOTES.md
- No explanation of origin/purpose
- Missing customization guidance
- No limitations documented

## Integration with Agent Builder

When Agent Builder creates a new agent:
1. Agent Builder outputs workspace
2. Agent Reviewer runs Full Review
3. If score < 7, iterate with specific fixes
4. If score >= 7, ready for registration

## Limitations

- **Subjective judgment** - Scores involve interpretation
- **Can't test runtime** - Reviews config, not behavior
- **Knowledge base dependent** - Quality limited by our principles
- **No automated fixes** - Identifies issues, human implements

## Future Improvements

- [ ] Automated fix suggestions
- [ ] Runtime behavior testing
- [ ] Historical tracking (improvement over time)
- [ ] Integration with Agent Builder for auto-review

## Changelog

- Initial creation from researcher blueprint
- Added evaluation criteria checklists
- Defined scoring system
