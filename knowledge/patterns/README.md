# Agent Design Patterns

Reusable patterns for common agent behaviors. Reference these when designing new agents.

## Pattern Index

| Pattern | Use Case | File |
|---------|----------|------|
| Context Engineering | Managing what the agent knows | `context-engineering.md` |
| Reflection | Self-critique and revision | `reflection.md` |
| Multi-Agent | Coordinating multiple agents | `multi-agent.md` |
| Guardrails | Safety and quality gates | `guardrails.md` |
| Memory | Persistence across sessions | `memory.md` |

## Choosing Patterns

**Start simple.** Only add patterns when you have a specific problem they solve.

| Problem | Pattern to Try |
|---------|----------------|
| Agent makes uninformed decisions | Context Engineering |
| Output quality is inconsistent | Reflection |
| Task is too complex for one agent | Multi-Agent |
| Agent takes dangerous actions | Guardrails |
| Agent forgets past interactions | Memory |
