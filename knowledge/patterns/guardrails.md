# Guardrails Pattern

Protect against agent mistakes and misuse through systematic checks.

## The 80/20 Rule

Focus guardrails on high-impact actions:
1. **Irreversible** - Delete, send, publish, deploy
2. **Sensitive** - Money, PII, credentials
3. **External** - Affects other users or systems

Don't over-guardrail low-risk actions (reading files, formatting text).

## Types of Guardrails

### Input Guardrails
Check what goes INTO the agent.

| Check | Purpose | Example |
|-------|---------|---------|
| Format validation | Ensure parseable input | JSON schema validation |
| Length limits | Prevent context overflow | Max 10K chars per message |
| Content filtering | Block harmful prompts | Prompt injection detection |
| Authorization | Verify permissions | Check user can access resource |
| Rate limiting | Prevent abuse | Max 100 requests/minute |

### Output Guardrails
Check what comes OUT of the agent.

| Check | Purpose | Example |
|-------|---------|---------|
| Format validation | Ensure correct structure | Output matches expected schema |
| Content filtering | Block harmful output | PII detection, toxicity check |
| Confidence threshold | Catch uncertain answers | Only act if confidence > 0.8 |
| Fact verification | Catch hallucinations | Cross-check with sources |
| Human approval | High-stakes gating | "Confirm before sending" |

### Process Guardrails
Check how the agent BEHAVES.

| Check | Purpose | Example |
|-------|---------|---------|
| Max iterations | Prevent infinite loops | Stop after 10 tool calls |
| Timeout | Prevent hanging | Kill after 5 minutes |
| Cost cap | Prevent runaway spending | Stop at $10 per request |
| Action allowlist | Restrict capabilities | Can only call these 5 tools |
| Rollback | Enable recovery | Log all actions for undo |

## Implementation Strategies

### Pre-Check (Fail Fast)
Validate before action. Cheapest and safest.

```python
def execute_action(action):
    if not validate_input(action):
        return Error("Invalid input")
    if not user_has_permission(action):
        return Error("Unauthorized")
    return do_action(action)
```

### Post-Check (Verify Output)
Validate after generation, before delivery.

```python
def generate_response(prompt):
    response = llm.generate(prompt)
    if contains_pii(response):
        response = redact_pii(response)
    if not matches_schema(response):
        response = fix_format(response)
    return response
```

### Confirmation Loop
Require approval for high-stakes actions.

```python
def delete_file(path):
    if is_high_risk(path):
        if not get_user_confirmation(f"Delete {path}?"):
            return Cancelled()
    return do_delete(path)
```

### Monitoring (Async Check)
Log everything, review later, alert on anomalies.

```python
def execute_action(action):
    result = do_action(action)
    log_action(action, result)  # Async logging
    if is_anomalous(action):
        alert_security_team(action)
    return result
```

## Common Guardrails to Implement

### Prompt Injection Detection
Detect attempts to override instructions.

```python
INJECTION_PATTERNS = [
    "ignore previous instructions",
    "disregard the above",
    "new instructions:",
    "system prompt:"
]

def check_injection(input):
    return any(p in input.lower() for p in INJECTION_PATTERNS)
```

### Output Schema Validation
Ensure structured output is valid.

```python
def validate_json_output(output, schema):
    try:
        data = json.loads(output)
        jsonschema.validate(data, schema)
        return True
    except:
        return False
```

### Action Allowlist
Restrict what the agent can do.

```python
ALLOWED_ACTIONS = ["search", "read_file", "summarize"]

def execute_tool(tool_name, params):
    if tool_name not in ALLOWED_ACTIONS:
        return Error(f"Tool {tool_name} not allowed")
    return tools[tool_name].run(params)
```

### Iteration Limit
Prevent infinite loops.

```python
MAX_ITERATIONS = 10

def agent_loop(task):
    for i in range(MAX_ITERATIONS):
        action = agent.decide()
        if action.is_done:
            return action.result
        execute(action)
    return Error("Max iterations exceeded")
```

### Sensitive Data Detection
Catch PII, secrets, credentials.

```python
import re

def contains_sensitive_data(text):
    patterns = {
        'email': r'\b[\w.-]+@[\w.-]+\.\w+\b',
        'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
        'api_key': r'\b(sk_|pk_|api_)[a-zA-Z0-9]{20,}\b',
    }
    return any(re.search(p, text) for p in patterns.values())
```

## Graceful Degradation

When guardrails trigger, fail gracefully:

1. **Inform the user** - Explain what was blocked and why
2. **Suggest alternatives** - Offer allowed actions
3. **Log the event** - Record for analysis
4. **Don't expose internals** - Don't reveal security measures

```python
def handle_guardrail_failure(guardrail, action):
    log_security_event(guardrail, action)

    return UserMessage(
        "I can't do that action. Here's what I can help with instead: ..."
    )
```

## Testing Guardrails

### Red Team Testing
Try to break your guardrails.

- Prompt injection attempts
- Edge cases and boundary values
- Malformed inputs
- Privilege escalation

### Fuzzing
Generate random inputs to find failures.

### Regression Testing
Ensure fixes don't break guardrails.

## Common Mistakes

### Too Strict
Blocks legitimate use cases.

**Fix:** Start permissive, tighten based on observed issues.

### Too Loose
Misses actual attacks.

**Fix:** Red team testing. Learn from incidents.

### Security Theater
Checks that look good but don't help.

**Fix:** Each guardrail should block a specific, real threat.

### User Friction
Too many confirmations kill usability.

**Fix:** Reserve confirmation for truly high-stakes actions.
