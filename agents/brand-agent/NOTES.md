# Brand Agent Notes

## Origin

Created by Agent Builder from the `business` blueprint, customized for brand strategy and management.

## Purpose

Help businesses build, maintain, and protect strong brand identities that drive growth and customer loyalty.

## Key Customizations from Business Blueprint

| Original | Customized |
|----------|------------|
| General business ops | Brand-focused operations |
| Support/sales modes | Strategy/voice/review modes |
| CRM tools | Brand analysis tools |
| Customer interactions | Brand touchpoint management |
| No persistence | Full memory system |

## Best Use Cases

- **Startups** - Define brand from scratch
- **Rebrands** - Transition to new positioning
- **Consistency** - Ensure all touchpoints align
- **Campaigns** - Brand-aligned marketing guidance
- **Growth** - Scale brand without dilution

## How to Use

### For New Brands
1. Start in **Strategy Mode** to define positioning
2. Use **Voice Mode** to establish communication style
3. Brand decisions are automatically saved to memory

### For Existing Brands
1. Memory is loaded automatically from `memory/` directory
2. Run **Audit Mode** to assess current state
3. Use **Review Mode** for content checks
4. Apply **Campaign Mode** for new initiatives

### For Competitive Positioning
1. Use **Competitor Mode** for landscape analysis
2. Analysis is saved to `memory/competitors.md`
3. Refine positioning in **Strategy Mode**

## Memory System

The agent persists brand decisions across sessions in `./memory/`:

| File | Contents |
|------|----------|
| `brand-strategy.md` | Positioning, pillars, audience |
| `voice-guide.md` | Voice attributes, do/don't examples |
| `decisions.md` | Log of decisions with rationale |
| `competitors.md` | Competitive landscape analysis |
| `lessons.md` | Insights from successes/failures |

See `MEMORY.md` for full documentation.

## Limitations

- **Not a designer** - Provides direction, not final visuals
- **Not a copywriter** - Sets tone, doesn't write final copy
- **Not autonomous** - Major brand decisions need human approval
- **Not a researcher** - Interprets research, doesn't conduct primary research

## Integration Points

- Works well with **Writer Agent** for content execution
- Pairs with **Researcher Agent** for market intelligence
- Guides **Business Agent** on customer communication

## Evaluation Criteria

How to measure if Brand Agent is performing well:

### Per-Task Evaluation
| Mode | Success Criteria |
|------|-----------------|
| Strategy | Positioning is clear, differentiated, documented, and saved to memory |
| Voice | Guidelines are specific with do/don't examples, saved to memory |
| Review | Feedback is specific, actionable, with line references |
| Competitor | Analysis covers 3+ competitors with comparison matrix, saved to memory |
| Campaign | Brief aligns with brand, has clear messages and guardrails |
| Audit | All touchpoints assessed, prioritized action items provided |

### Quality Indicators
- **Specificity** - Recommendations cite specific guidelines, not vague advice
- **Consistency** - Advice aligns with documented brand strategy
- **Actionability** - Feedback includes concrete next steps
- **Completeness** - Each mode's "Done when" criteria are met
- **Memory Usage** - Loads context before tasks, saves outputs after

### Red Flags
- Generic advice that could apply to any brand
- Contradicting established brand guidelines
- Missing stopping criteria (endless refinement)
- Ignoring competitive context
- Not loading/saving memory appropriately

## Customization Tips

### For Specific Industries
Add industry context to IDENTITY.md:
```markdown
## Industry Focus
B2B SaaS for developers
- Technical audience expectations
- Trust and reliability emphasis
- Community-driven growth
```

### For Existing Brand Guidelines
Pre-populate memory files with existing brand documentation:
```bash
# Copy existing brand strategy
cp /path/to/brand-guide.md ./memory/brand-strategy.md

# Copy existing voice guide
cp /path/to/voice-and-tone.md ./memory/voice-guide.md
```

### For Team Use
Share the memory directory across team members to maintain consistency.

## File Structure

```
brand-agent/
├── IDENTITY.md     ← Who the agent is
├── SOUL.md         ← Core values
├── AGENTS.md       ← Operating modes
├── TOOLS.md        ← Available tools
├── MEMORY.md       ← Memory system docs
├── NOTES.md        ← This file
└── memory/         ← Persistent storage
    ├── README.md
    ├── brand-strategy.md
    ├── voice-guide.md
    ├── decisions.md
    ├── competitors.md
    └── lessons.md
```

## Changelog

- Initial creation from business blueprint
- Customized for brand strategy focus
- Added brand-specific modes and tools
- **v1.1**: Added "Done when" stopping conditions to all modes (per knowledge base)
- **v1.1**: Fixed TOOLS.md with typed parameters and return specs
- **v1.1**: Clarified available vs manual analysis tools
- **v1.1**: Added evaluation criteria
- **v1.1**: Made "Long-Term Thinking" value more actionable
- **v1.2**: Added full memory system with 5 persistent files
- **v1.2**: Created MEMORY.md documenting memory operations
- **v1.2**: Integrated memory load/save into all modes
- **v1.2**: Added memory section to IDENTITY.md
- **v1.2**: Updated TOOLS.md with memory operations
