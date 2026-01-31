# Reflection Pattern

Agents improve output quality by critiquing and revising their own work.

## Core Pattern

```
1. Generate initial output
2. Critique: "What's wrong with this?"
3. Revise based on critique
4. Repeat until satisfied (or max iterations)
```

## When to Use Reflection

### Good Use Cases
- **Writing tasks** - Drafts benefit from revision
- **Code generation** - Catch bugs before execution
- **Analysis** - Deepen insights through iteration
- **Complex reasoning** - Multi-step problems need checking

### Bad Use Cases
- **Simple tasks** - Adds latency with no improvement
- **Highly constrained outputs** - Format already correct
- **Domain expertise required** - LLM can't evaluate quality
- **Real-time needs** - Too slow for immediate response

## Reflection Techniques

### Self-Critique
Agent evaluates its own output.

```
Prompt: "Review your response. List 3 ways it could be improved."
```

**Pros:** Simple, no extra calls
**Cons:** Blind to own mistakes

### Rubric-Based
Evaluate against specific criteria.

```
Rate this code 1-5 on each criterion:
- Correctness: Does it work?
- Readability: Is it clear?
- Efficiency: Is it fast?
- Maintainability: Is it easy to change?
```

**Pros:** Consistent, targeted
**Cons:** Need to define good rubrics

### Persona-Based
Critique from a specific perspective.

```
"Review this as a senior engineer would. What would they change?"
"What would a security expert flag in this code?"
```

**Pros:** Catches domain-specific issues
**Cons:** LLM may not truly embody expertise

### Test-Driven
Generate tests, then check if output passes.

```
1. Generate code
2. Generate test cases
3. Run tests
4. Fix failures
5. Repeat
```

**Pros:** Objective quality measure
**Cons:** Only works for testable outputs

## Effective Critique Prompts

General:
- "Rate this output 1-10 and explain why not higher"
- "List 3 specific improvements"
- "Does this fully address the original request?"

For writing:
- "Is the argument logical and well-supported?"
- "Are there any unclear or confusing sections?"
- "What would make this more persuasive?"

For code:
- "What edge cases are not handled?"
- "Are there any potential bugs or security issues?"
- "How could this be simplified?"

## Controlling Iterations

### Fixed Count
Always do N iterations (usually 1-2).

```python
for i in range(2):
    output = generate(prompt)
    critique = generate(f"Critique: {output}")
    output = revise(output, critique)
```

### Quality Threshold
Stop when output meets criteria.

```python
while True:
    score = evaluate(output)
    if score >= 8:
        break
    output = revise(output, get_critique(output))
```

### Diminishing Returns
Stop when improvements are marginal.

```python
prev_score = 0
while True:
    score = evaluate(output)
    if score - prev_score < 0.5:  # Marginal improvement
        break
    prev_score = score
    output = revise(output)
```

## Common Mistakes

### Over-Reflection
Too many iterations make output worse (over-editing).

**Fix:** Cap iterations. 2-3 is usually enough.

### Vague Critiques
"This could be better" doesn't help.

**Fix:** Require specific, actionable feedback.

### Ignoring Critique
Agent generates critique but doesn't actually use it.

**Fix:** Explicitly include critique in revision prompt.

### Reflection Without Action
Agent agrees improvements needed but makes none.

**Fix:** Make revision mandatory. "Now rewrite incorporating these changes."

## Implementation Template

```
GENERATE:
{task_description}

CRITIQUE:
Review your output above. For each of these criteria, rate 1-5 and explain:
1. Completeness - Does it fully address the request?
2. Correctness - Is it accurate and error-free?
3. Clarity - Is it clear and well-organized?

If any score is below 4, list specific changes to improve it.

REVISE (if needed):
Incorporate the improvements you identified. Output the final version.
```
