# Tools

Tools for evaluating agent configurations.

## Workspace Access

### read_workspace
Read all files from an agent workspace.

**When to use:** Starting any review, loading agent configuration
**Parameters:**
- path: Workspace directory path

**Returns:** Contents of IDENTITY.md, SOUL.md, AGENTS.md, TOOLS.md, NOTES.md

### read_file
Read a specific file.

**When to use:** Focused review, checking specific concerns
**Parameters:**
- path: Full file path

## Knowledge Base Access

### read_knowledge
Read from the knowledge base.

**When to use:** Loading evaluation criteria
**Key paths:**
- `../knowledge/foundations/ai-agents-course.md` - Core concepts
- `../knowledge/patterns/context-engineering.md` - Context principles
- `../knowledge/patterns/reflection.md` - Self-improvement patterns
- `../knowledge/patterns/multi-agent.md` - Coordination patterns
- `../knowledge/patterns/guardrails.md` - Safety patterns
- `../knowledge/patterns/memory.md` - Persistence patterns
- `../knowledge/tools/README.md` - Tool design principles
- `../knowledge/evals/README.md` - Evaluation methods

### search_knowledge
Search knowledge base for specific topics.

**When to use:** Finding relevant principles for specific issues
**Parameters:**
- query: What to search for

## Evaluation Tools

### score_file
Score a file against criteria.

**When to use:** Systematic evaluation
**Parameters:**
- file: Content to evaluate
- criteria: What to check against

**Returns:** Score (1-10) with reasoning

### compare_files
Compare two versions of a file.

**When to use:** A/B comparison, before/after evaluation
**Parameters:**
- file_a: First version
- file_b: Second version
- criteria: Comparison dimensions

## Reporting

### generate_report
Create structured review report.

**When to use:** Compiling final review
**Parameters:**
- findings: All evaluation results
- format: summary, detailed, or checklist

### write_file
Save review results.

**When to use:** Persisting review for reference
**Parameters:**
- path: Where to save
- content: Report content

## Evaluation Criteria Reference

### IDENTITY.md Checklist
- [ ] Clear name and role
- [ ] Specific expertise listed
- [ ] Approach is step-by-step
- [ ] Honest "What I'm Not" section
- [ ] Mission aligns with expertise

### SOUL.md Checklist
- [ ] Values are actionable, not platitudes
- [ ] Each value guides real decisions
- [ ] Values are specific to this agent type
- [ ] No contradictions between values

### AGENTS.md Checklist
- [ ] Each mode has clear trigger
- [ ] Each mode has defined approach
- [ ] Each mode has expected output
- [ ] Modes don't overlap confusingly
- [ ] Mode selection guidance included

### TOOLS.md Checklist
- [ ] Tools are atomic (one action each)
- [ ] Descriptions are specific
- [ ] Parameters are typed/constrained
- [ ] Usage guidelines included
- [ ] Dangerous tools have warnings

### NOTES.md Checklist
- [ ] Purpose is documented
- [ ] Customization tips included
- [ ] Limitations are listed
- [ ] Integration points noted
