# Evaluation Guide

You can't improve what you don't measure.

## Why Evals Matter

Without evals:
- You think changes help, but they don't
- Regressions slip through
- "It works on my examples" isn't evidence
- Hard to compare approaches

With evals:
- Objective measure of quality
- Catch regressions immediately
- Compare approaches fairly
- Track improvement over time

## Eval Types

### Component-Level Evals
Test individual pieces in isolation.

| Component | What to Test |
|-----------|-------------|
| Tool selection | Does agent pick the right tool? |
| Parameter extraction | Are parameters correct? |
| Format compliance | Does output match schema? |
| Single step | Is each reasoning step valid? |

**Example:**
```yaml
test: tool_selection
input: "What's the weather in Paris?"
expected_tool: get_weather
expected_params:
  city: "Paris"
```

### End-to-End Evals
Test the full pipeline.

| Aspect | What to Measure |
|--------|----------------|
| Task completion | Did agent finish the task? |
| Output correctness | Is the final answer right? |
| Efficiency | How many steps/tokens? |
| User satisfaction | Would user be happy? |

**Example:**
```yaml
test: full_task
input: "Find me a flight from NYC to LA next Monday under $300"
expected:
  contains: ["flight", "NYC", "LA", "Monday"]
  price_under: 300
  status: completed
```

## Eval Methods

### Exact Match
Output must equal expected exactly.

```python
def exact_match(output, expected):
    return output == expected
```

**Use for:** Structured outputs, specific answers

### Contains
Output must include key elements.

```python
def contains_all(output, required):
    return all(r in output for r in required)
```

**Use for:** Free-form responses, partial matching

### Regex Match
Output matches pattern.

```python
def regex_match(output, pattern):
    return re.match(pattern, output) is not None
```

**Use for:** Formatted outputs (dates, IDs, etc.)

### LLM-as-Judge
Another LLM evaluates the output.

```python
def llm_judge(output, criteria):
    prompt = f"""
    Rate this output 1-5 on: {criteria}
    Output: {output}
    Score:
    """
    return llm.generate(prompt)
```

**Use for:** Quality assessment, subjective criteria

### Human Evaluation
Human raters judge output quality.

**Use for:** Final validation, complex quality, gold standard

## Building Eval Sets

### Start Small
Begin with 10-20 diverse examples.

### Include Edge Cases
- Empty inputs
- Very long inputs
- Ambiguous requests
- Invalid requests
- Boundary conditions

### Add Real Examples
Capture actual user interactions.

```python
# Log real inputs and have humans label expected outputs
def log_for_eval(input, output, human_rating):
    eval_set.append({
        "input": input,
        "output": output,
        "human_rating": human_rating
    })
```

### Balance Categories
If you have 100 evals:
- 50 common cases (happy path)
- 30 edge cases
- 20 failure cases (should reject/error)

### Version Your Evals
Eval sets evolve. Track changes.

```
evals/
├── v1/
│   └── test_cases.yaml
├── v2/
│   ├── test_cases.yaml
│   └── CHANGELOG.md
```

## Running Evals

### The Eval Loop

```python
def run_evals(agent, eval_set):
    results = []
    for test in eval_set:
        output = agent.run(test.input)
        score = evaluate(output, test.expected)
        results.append({
            "input": test.input,
            "output": output,
            "expected": test.expected,
            "score": score,
            "passed": score >= test.threshold
        })
    return results
```

### Metrics to Track

```python
def summarize_results(results):
    return {
        "total": len(results),
        "passed": sum(r["passed"] for r in results),
        "pass_rate": sum(r["passed"]) / len(results),
        "avg_score": mean(r["score"] for r in results),
        "by_category": group_by_category(results)
    }
```

### Regression Detection

```python
def check_regressions(current, previous):
    regressions = []
    for test in current:
        prev = find_previous(test, previous)
        if prev and test.score < prev.score:
            regressions.append({
                "test": test.name,
                "was": prev.score,
                "now": test.score
            })
    return regressions
```

## Eval at Scale

You can't manually check everything. Sample intelligently.

### Stratified Sampling
Sample from each category proportionally.

```python
def stratified_sample(results, n):
    samples = []
    for category in categories:
        category_results = [r for r in results if r.category == category]
        k = n * len(category_results) / len(results)
        samples.extend(random.sample(category_results, k))
    return samples
```

### Focus on Failures
Review failures more than successes.

```python
def prioritized_review(results):
    failures = [r for r in results if not r.passed]
    low_confidence = [r for r in results if r.confidence < 0.7]
    return failures + low_confidence
```

### Automated Triage
Use LLM to categorize failures.

```python
def categorize_failure(test):
    prompt = f"""
    This test failed:
    Input: {test.input}
    Expected: {test.expected}
    Got: {test.output}

    Categorize the failure:
    - wrong_tool: Agent used wrong tool
    - wrong_params: Right tool, wrong parameters
    - wrong_reasoning: Bad logic in response
    - format_error: Correct content, wrong format
    - hallucination: Made up information
    - other: Doesn't fit categories

    Category:
    """
    return llm.generate(prompt)
```

## Common Mistakes

### Testing on Training Data
Eval set overlaps with examples in prompt.

**Fix:** Hold out eval examples. Never use them for few-shot.

### Overfitting to Evals
Optimize for eval score, not real quality.

**Fix:** Regularly add new cases. Test on real user inputs.

### Inconsistent Conditions
Different runs have different results.

**Fix:** Control randomness. Same seed, same temperature.

### Ignoring Edge Cases
Only test happy path.

**Fix:** Deliberately add weird inputs.

### No Baseline
Can't tell if changes actually help.

**Fix:** Always compare against baseline. Track metrics over time.

## Eval Checklist

- [ ] Eval set has 10+ diverse examples
- [ ] Edge cases and failures are included
- [ ] Eval method matches output type (exact, contains, LLM judge)
- [ ] Baseline metrics established
- [ ] Regression detection in place
- [ ] Eval runs are reproducible
- [ ] Real user examples are added over time
- [ ] Results are tracked and versioned
