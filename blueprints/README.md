# Agent Blueprints

Reusable templates for common agent types. Start here instead of from scratch.

## Available Blueprints

| Blueprint | Use For | Directory |
|-----------|---------|-----------|
| Researcher | Web search, RAG, fact-finding | `researcher/` |
| Writer | Content, scripts, copy | `writer/` |
| Coder | Code generation, debugging | `coder/` |
| Business | Sales, support, operations | `business/` |

## How to Use Blueprints

### 0. Capture Intent First (WHY.md)
**Before building**, fill out the WHY.md template:
```bash
cp blueprints/WHY.md my-new-agent/WHY.md
# Fill in: Problem, Users, Constraints, Success Criteria
# Get approval before proceeding
```

This prevents drift by documenting the "why" before the "how."

### 1. Choose a Blueprint
Pick the closest match to your agent's primary function.

### 2. Copy the Directory
```bash
cp -r blueprints/researcher/ my-new-agent/
```

### 3. Customize
Edit each file to match your specific needs:

| File | What to Customize |
|------|-------------------|
| WHY.md | Problem, users, constraints (fill FIRST) |
| IDENTITY.md | Name, emoji, specific role |
| SOUL.md | Values and principles for your domain |
| AGENTS.md | Specific modes and behaviors |
| TOOLS.md | Add/remove tools for your use case |
| KNOWLEDGE.md | Domain knowledge, concepts, references |
| NOTES.md | Document what you changed and why |

### 4. Register
Add to `~/.openclaw/openclaw.json`:
```json
{
  "id": "my-agent",
  "workspace": "/path/to/my-new-agent",
  "identity": { "name": "My Agent", "emoji": "🤖" }
}
```

### 5. Test
Run the agent and iterate based on results.

## Blueprint Structure

Each agent should have:

```
agent-name/
├── WHY.md         ← Intent doc (copy from blueprints/WHY.md)
├── IDENTITY.md    ← Who the agent is
├── SOUL.md        ← Core values and principles
├── AGENTS.md      ← Operating modes and behaviors
├── TOOLS.md       ← Available tools and usage
├── KNOWLEDGE.md   ← Domain knowledge (copy from blueprints/KNOWLEDGE.md)
└── NOTES.md       ← When to use, limitations, customization tips
```

**Templates at root:** Copy `blueprints/WHY.md` and `blueprints/KNOWLEDGE.md` when starting.

## Creating New Blueprints

When you build an agent that others could reuse:

1. Copy your working agent to `blueprints/new-type/`
2. Generalize specific details (names, domains, etc.)
3. Add placeholder comments: `<!-- CUSTOMIZE: your specific X here -->`
4. Write NOTES.md explaining the blueprint
5. Test by creating a new agent from it

## Combining Blueprints

Some agents need multiple capabilities. Approaches:

### Merge Files
Take sections from multiple blueprints into one agent.

### Multi-Agent
Use separate agents from different blueprints, coordinated by a manager.

### Layering
Start with one blueprint, add tools/modes from others.

## Blueprint vs. From Scratch

**Use blueprints when:**
- Building a common agent type
- Want proven patterns
- Need to move fast

**Build from scratch when:**
- Novel agent type
- Highly specialized domain
- Learning how agents work
