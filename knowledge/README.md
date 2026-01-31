# Knowledge Base

Accumulated wisdom for building effective AI agents.

## Structure

| Directory | Contents |
|-----------|----------|
| `foundations/` | Core concepts every agent builder must understand |
| `patterns/` | Design patterns for common agent behaviors |
| `tools/` | How to design effective tools for agents |
| `evals/` | How to evaluate agent performance |

## How to Use

**When building a new agent:**
1. Start with `foundations/ai-agents-course.md` for core concepts
2. Choose relevant patterns from `patterns/`
3. Design tools using guides in `tools/`
4. Plan evaluation using `evals/`

**When debugging an agent:**
1. Check if the problem matches a known pattern
2. Review tool design against principles
3. Set up targeted evals to measure improvement

## Key Principles

1. **Context is everything** - What the agent knows determines what it can do
2. **Tools are interfaces** - Design for the LLM, not for humans
3. **Decompose aggressively** - Break tasks into LLM-sized pieces
4. **Evaluate continuously** - You can't improve what you don't measure
5. **Start simple** - Add complexity only when needed

## Sources

- AI Agents course (distilled in foundations/)
- OpenClaw patterns and documentation
- Lessons learned from testing variants
