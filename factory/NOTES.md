# Agent Builder Notes

## Purpose

The Agent Builder is a meta-agent that creates other agents. It's designed to:

1. Apply accumulated knowledge systematically
2. Start from proven blueprints
3. Customize for specific needs
4. Build in evaluation from the start
5. Iterate based on results

## How to Use

### For New Agents

1. **Start in Discovery Mode** - Clarify what's needed
2. **Switch to Design Mode** - Plan the architecture
3. **Move to Build Mode** - Create the workspace
4. **Use Evaluate Mode** - Test the result
5. **Apply Improve Mode** - Iterate based on results

### For Existing Agents

1. **Read the workspace** - Understand current state
2. **Run evaluations** - Identify issues
3. **Use Improve Mode** - Make targeted changes
4. **Re-evaluate** - Verify improvements

### For Experimentation

1. **Use Copy Blueprint** - Create variants
2. **Make changes** - Test different approaches
3. **Use Compare Mode** - Determine what works best
4. **Document lessons** - Add to knowledge base

## Design Decisions

### Why Blueprints?
Most agents fall into common categories. Starting from blueprints:
- Saves time
- Applies proven patterns
- Ensures consistency
- Provides learning examples

### Why Knowledge Base?
Accumulated wisdom should be:
- Searchable (not just in prompts)
- Updatable (lessons learned add to it)
- Referenceable (explain why decisions made)

### Why Evaluation Built-In?
Agents without metrics:
- Can't be objectively improved
- May degrade without notice
- Hard to compare variants

## Future Improvements

- [ ] Automated eval generation from requirements
- [ ] Agent performance dashboard
- [ ] Knowledge base search improvements
- [ ] Multi-agent coordination patterns
- [ ] Cost tracking and optimization

## Workspace Structure

```
factory/
├── IDENTITY.md   ← This agent's identity
├── SOUL.md       ← Core values
├── AGENTS.md     ← Operating modes
├── TOOLS.md      ← Available tools
└── NOTES.md      ← This file
```

## Related Resources

- Knowledge: `../knowledge/`
- Blueprints: `../blueprints/`
- Test variants: `../01-baseline/`, `../02-minimal/`

## Changelog

- Initial creation with core modes and tools
