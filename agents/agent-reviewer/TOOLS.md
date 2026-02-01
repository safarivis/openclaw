# Tools

Tools for evaluating agent configurations.

## Workspace Access

### read_workspace
Read all files from an agent workspace.

**When to use:** Starting any review, loading agent configuration
**Parameters:**
- path (string, required): Workspace directory path

**Returns:**
```yaml
type: object
properties:
  identity: string - IDENTITY.md content
  soul: string - SOUL.md content
  agents: string - AGENTS.md content
  tools: string - TOOLS.md content
  notes: string - NOTES.md content
  memory: string | null - MEMORY.md if exists
  has_memory_dir: boolean - Whether memory/ exists
```

### read_file
Read a specific file.

**When to use:** Focused review, checking specific concerns
**Parameters:**
- path (string, required): Full file path

**Returns:**
```yaml
type: object
properties:
  content: string - File contents
  exists: boolean - Whether file was found
```

## Knowledge Base Access

### read_knowledge
Read from the knowledge base.

**When to use:** Loading evaluation criteria
**Parameters:**
- path (string, required): Path relative to knowledge/

**Returns:**
```yaml
type: object
properties:
  content: string - File contents
  path: string - Full path read
```

**Key paths:**
- `foundations/ai-agents-course.md` - Core concepts
- `patterns/context-engineering.md` - Context principles
- `patterns/reflection.md` - Self-improvement patterns
- `patterns/multi-agent.md` - Coordination patterns
- `patterns/guardrails.md` - Safety patterns
- `patterns/memory.md` - Persistence patterns
- `tools/README.md` - Tool design principles
- `evals/README.md` - Evaluation methods

### search_knowledge
Search knowledge base for specific topics.

**When to use:** Finding relevant principles for specific issues
**Parameters:**
- query (string, required): What to search for

**Returns:**
```yaml
type: object
properties:
  matches: array - Files with matching content
  count: integer - Number of matches
```

## Evaluation Tools

### score_file
Score a file against criteria with categorized issues.

**When to use:** Systematic evaluation
**Parameters:**
- file (string, required): Content to evaluate
- criteria (string, required): What to check against

**Returns:**
```yaml
type: object
properties:
  score: number - Score 1-10
  reasoning: string - Why this score
  issues: array
    - severity: enum - "critical" | "major" | "minor" | "polish"
    - category: enum - "identity" | "capability" | "safety" | "clarity"
    - description: string - What's wrong
    - fix: string - How to fix it
    - line: number | null - Line reference if applicable
```

**Severity Guide:**
- **critical**: Blocks core functionality (0 tolerance)
- **major**: Significant problems (should fix before use)
- **minor**: Small issues (fix when convenient)
- **polish**: Suggestions (optional improvements)

### compare_files
Compare two versions of a file.

**When to use:** A/B comparison, before/after evaluation
**Parameters:**
- file_a (string, required): First version content
- file_b (string, required): Second version content
- criteria (string, optional): Comparison dimensions

**Returns:**
```yaml
type: object
properties:
  winner: string - "a" | "b" | "tie"
  score_a: number - Score for first file
  score_b: number - Score for second file
  differences: array - Key differences
```

## Reporting

### generate_report
Create structured review report with categorized issues.

**When to use:** Compiling final review
**Parameters:**
- findings (object, required): All evaluation results
- format (enum, optional): "summary" | "detailed" | "checklist" (default: "detailed")
- group_by (enum, optional): "severity" | "category" | "file" (default: "severity")

**Returns:**
```yaml
type: object
properties:
  report: string - Formatted report content
  format: string - Format used
  summary:
    overall_score: number
    critical_count: number
    major_count: number
    minor_count: number
    polish_count: number
    pass: boolean - True if score >= 8.5 AND critical_count == 0
```

**Report Template (severity grouping):**
```markdown
# Agent Review: [name]

**Score:** X/10 | **Status:** PASS/FAIL
**Critical:** N | **Major:** N | **Minor:** N | **Polish:** N

## Critical Issues (must fix)
- [category] description → fix

## Major Issues (should fix)
- [category] description → fix

## Minor Issues (nice to fix)
- [category] description → fix

## Polish (optional)
- [category] description → fix

## Top 3 Priority Fixes
1. ...
2. ...
3. ...
```

### write_file
Save review results.

**When to use:** Persisting review for reference
**Parameters:**
- path (string, required): Where to save
- content (string, required): Report content

**Returns:**
```yaml
type: object
properties:
  success: boolean
  path: string - Saved file path
```

## Evaluation Criteria Reference

### File → Category Mapping

| File | Primary Category | Secondary |
|------|-----------------|-----------|
| WHY.md | Identity | Clarity |
| IDENTITY.md | Identity | Clarity |
| SOUL.md | Safety | Identity |
| AGENTS.md | Capability | Clarity |
| TOOLS.md | Capability | Safety |
| MEMORY.md | Capability | Clarity |
| NOTES.md | Clarity | - |

### WHY.md Checklist (Identity/Clarity)
- [ ] Problem statement is concrete, not vague
- [ ] Target users clearly defined
- [ ] Success criteria are measurable
- [ ] Constraints explicitly listed
- [ ] Key decisions documented with rationale

### IDENTITY.md Checklist (Identity/Clarity)
- [ ] Clear name and role
- [ ] Specific expertise listed
- [ ] Approach is step-by-step
- [ ] Honest "What I'm Not" section
- [ ] Mission aligns with expertise

### SOUL.md Checklist (Safety/Identity)
- [ ] Values are actionable, not platitudes
- [ ] Each value guides real decisions
- [ ] Values are specific to this agent type
- [ ] No contradictions between values
- [ ] Includes constraints/limits (safety)

### AGENTS.md Checklist (Capability/Clarity)
- [ ] Each mode has clear trigger
- [ ] Each mode has defined approach
- [ ] Each mode has expected output
- [ ] Each mode has "Done when:" condition
- [ ] Modes don't overlap confusingly
- [ ] Mode selection guidance included

### TOOLS.md Checklist (Capability/Safety)
- [ ] Tools are atomic (one action each)
- [ ] Descriptions are specific
- [ ] Parameters are typed/constrained
- [ ] Usage guidelines included
- [ ] Dangerous tools have warnings (safety)
- [ ] Return types documented

### MEMORY.md Checklist (Capability/Clarity)
- [ ] Memory structure documented
- [ ] What to remember defined
- [ ] What NOT to remember defined
- [ ] Persistence strategy clear

### NOTES.md Checklist (Clarity)
- [ ] Purpose is documented
- [ ] Customization tips included
- [ ] Limitations are listed
- [ ] Integration points noted
- [ ] Changelog maintained
