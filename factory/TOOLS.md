# Tools

Tools I use to build and improve agents.

## Knowledge Access

### read_knowledge
Read from the knowledge base.

**When to use:** Understanding patterns, reviewing concepts before designing
**Paths:**
- `../knowledge/foundations/` - Core agent concepts
- `../knowledge/patterns/` - Design patterns
- `../knowledge/tools/` - Tool design guides
- `../knowledge/evals/` - Evaluation methods

**Example:**
```
read_knowledge("patterns/context-engineering.md")
```

### search_knowledge
Search for relevant knowledge.

**When to use:** Finding patterns for specific problems
**Parameters:**
- query: What to search for

**Example:**
```
search_knowledge("how to handle rate limiting")
```

## Blueprint Operations

### list_blueprints
List available blueprints.

**When to use:** Choosing a starting point for new agent
**Returns:** Blueprint names with brief descriptions

### read_blueprint
Read a complete blueprint.

**When to use:** Understanding a blueprint before customizing
**Parameters:**
- blueprint: researcher, writer, coder, business

**Example:**
```
read_blueprint("researcher")
```

### copy_blueprint
Create new workspace from blueprint.

**When to use:** Starting a new agent build
**Parameters:**
- blueprint: Source blueprint
- destination: New workspace path
- name: New agent name

**Example:**
```
copy_blueprint("researcher", "../05-competitor-intel", "Competitor Intel Agent")
```

## Workspace Operations

### create_workspace
Create a new agent workspace from scratch.

**When to use:** When no blueprint fits
**Parameters:**
- path: Workspace location
- name: Agent name

### read_workspace
Read an existing agent's configuration.

**When to use:** Understanding existing agents, preparing improvements
**Parameters:**
- path: Workspace location

### update_workspace
Modify an existing agent.

**When to use:** Improving agents, fixing issues
**Parameters:**
- path: Workspace location
- file: Which file to update
- changes: What to change

## Evaluation

### run_eval
Execute evaluation against an agent.

**When to use:** Testing agent performance
**Parameters:**
- workspace: Agent to test
- eval_set: Test cases to run

### compare_agents
Run comparison between two agents.

**When to use:** A/B testing, variant comparison
**Parameters:**
- workspace_a: First agent
- workspace_b: Second agent
- test_cases: Inputs to test

## Documentation

### add_lesson
Add a lesson learned to the knowledge base.

**When to use:** After discovering something new that could help future agent building
**Parameters:**
- title: Brief description
- context: What happened
- lesson: What was learned
- applies_to: When to remember this

**Example:**
```
add_lesson(
  "Check tool count",
  "Built agent with 20 tools, it got confused",
  "Keep tools under 15, consolidate related functions",
  "Agent design, tool selection"
)
```
