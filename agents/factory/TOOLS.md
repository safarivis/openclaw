# Tools

Tools I use to build and improve agents.

## Knowledge Access

### read_knowledge
Read from the knowledge base.

**When to use:** Understanding patterns, reviewing concepts before designing
**Parameters:**
- path (string, required): Path relative to knowledge/, e.g., "patterns/memory.md"

**Returns:**
```yaml
type: object
properties:
  content: string - File contents
  path: string - Full path read
```

**Paths:**
- `foundations/` - Core agent concepts
- `patterns/` - Design patterns
- `tools/` - Tool design guides
- `evals/` - Evaluation methods

### search_knowledge
Search for relevant knowledge.

**When to use:** Finding patterns for specific problems
**Parameters:**
- query (string, required): What to search for

**Returns:**
```yaml
type: object
properties:
  matches: array - Matching files with excerpts
  count: integer - Number of matches
```

## Blueprint Operations

### list_blueprints
List available blueprints.

**When to use:** Choosing a starting point for new agent
**Parameters:** None

**Returns:**
```yaml
type: array
items:
  - name: string - Blueprint name
  - description: string - Brief purpose
  - best_for: string - Use cases
```

### read_blueprint
Read a complete blueprint.

**When to use:** Understanding a blueprint before customizing
**Parameters:**
- blueprint (enum, required): "researcher" | "writer" | "coder" | "business"

**Returns:**
```yaml
type: object
properties:
  files: object - All blueprint files (IDENTITY, SOUL, AGENTS, TOOLS, NOTES)
  path: string - Blueprint location
```

### copy_blueprint
Create new workspace from blueprint.

**When to use:** Starting a new agent build
**Parameters:**
- blueprint (enum, required): "researcher" | "writer" | "coder" | "business"
- destination (string, required): New workspace path
- name (string, required): New agent name

**Returns:**
```yaml
type: object
properties:
  success: boolean
  path: string - Created workspace path
  files_created: array - List of files created
```

## Workspace Operations

### create_workspace
Create a new agent workspace from scratch.

**When to use:** When no blueprint fits
**Parameters:**
- path (string, required): Workspace location
- name (string, required): Agent name

**Returns:**
```yaml
type: object
properties:
  success: boolean
  path: string - Created workspace
  files_created: array - List of template files
```

### read_workspace
Read an existing agent's configuration.

**When to use:** Understanding existing agents, preparing improvements
**Parameters:**
- path (string, required): Workspace location

**Returns:**
```yaml
type: object
properties:
  identity: string - IDENTITY.md content
  soul: string - SOUL.md content
  agents: string - AGENTS.md content
  tools: string - TOOLS.md content
  notes: string - NOTES.md content
  has_memory: boolean - Whether memory/ exists
```

### update_workspace
Modify an existing agent.

**When to use:** Improving agents, fixing issues
**Parameters:**
- path (string, required): Workspace location
- file (enum, required): "IDENTITY.md" | "SOUL.md" | "AGENTS.md" | "TOOLS.md" | "NOTES.md"
- changes (string, required): Content to update

**Returns:**
```yaml
type: object
properties:
  success: boolean
  file: string - Updated file path
```

## Evaluation

### run_eval
Execute evaluation against an agent.

**When to use:** Testing agent performance
**Parameters:**
- workspace (string, required): Agent path to test
- eval_set (string, optional): Test cases file (default: all)

**Returns:**
```yaml
type: object
properties:
  passed: integer - Tests passed
  failed: integer - Tests failed
  score: number - Percentage score
  details: array - Individual test results
```

### compare_agents
Run comparison between two agents.

**When to use:** A/B testing, variant comparison
**Parameters:**
- workspace_a (string, required): First agent path
- workspace_b (string, required): Second agent path
- test_cases (array, optional): Inputs to test

**Returns:**
```yaml
type: object
properties:
  winner: string - Path of better agent
  scores: object - Score for each agent
  differences: array - Key differences found
```

## Documentation

### add_lesson
Add a lesson learned to memory.

**When to use:** After discovering something new
**Parameters:**
- title (string, required): Brief description
- context (string, required): What happened
- lesson (string, required): What was learned
- applies_to (string, required): When to remember this

**Returns:**
```yaml
type: object
properties:
  success: boolean
  path: string - Where lesson was saved
```
