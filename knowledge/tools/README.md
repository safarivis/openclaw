# Tool Design Guide

Tools are how agents act on the world. Design them for LLMs, not humans.

## Tool Anatomy

```yaml
name: search_customers
description: |
  Search the customer database by name, email, or customer ID.
  Returns up to 10 matching customers with their contact info.
  Use this when you need to find a specific customer or lookup customer details.
parameters:
  query:
    type: string
    description: The search term (name, email, or ID)
    required: true
  field:
    type: enum
    values: [name, email, id]
    description: Which field to search in
    default: name
returns:
  type: array
  items:
    - id: Customer ID
    - name: Full name
    - email: Email address
    - status: active/inactive
```

## Design Principles

### 1. Clear Names
The name should describe what the tool does.

| Bad | Good | Why |
|-----|------|-----|
| `sc` | `search_customers` | Abbreviations confuse |
| `query_db_v2` | `get_customer_orders` | Be specific |
| `do_thing` | `send_email` | Actions over generic names |

### 2. Specific Descriptions
Describe: what it does, when to use it, what it returns.

**Bad:**
```
description: Search customers
```

**Good:**
```
description: |
  Search the customer database by name, email, or customer ID.
  Returns up to 10 matching customers with their contact info.
  Use this when you need to find a specific customer or lookup customer details.
  Returns empty array if no matches found.
```

### 3. Typed Parameters
Constrain inputs to reduce errors.

| Type | Use When |
|------|----------|
| enum | Limited valid options |
| boolean | Yes/no decisions |
| integer | Counts, IDs, limits |
| string | Free-form text |
| array | Multiple items |

**Prefer enums over strings:**
```yaml
# Bad - agent might send "E-mail" or "EMAIL"
field:
  type: string

# Good - agent can only send valid values
field:
  type: enum
  values: [name, email, id]
```

### 4. Atomic Operations
One tool = one action. Don't combine multiple operations.

**Bad:**
```
search_and_update_customer(query, new_email)
```

**Good:**
```
search_customers(query)
update_customer(id, new_email)
```

### 5. Idempotent When Possible
Same input = same output = same side effects.

```yaml
# Idempotent - safe to retry
set_customer_status(id, status="active")

# Not idempotent - different each time
increment_counter(id)
```

### 6. Minimal Required Parameters
Only require what's truly necessary.

```yaml
# Bad - too many required fields
create_task:
  required: [title, description, due_date, priority, assignee, tags, project]

# Good - smart defaults
create_task:
  required: [title]
  optional:
    description: ""
    due_date: null
    priority: "medium"
```

## Common Mistakes

### Too Many Tools
Agent gets decision paralysis. Can't remember what each does.

**Fix:** Consolidate related tools. Aim for 5-15 tools max.

### Vague Descriptions
Agent uses wrong tool or passes wrong parameters.

**Fix:** Be extremely specific. Include examples in description.

### Complex Parameters
Agent makes formatting errors.

**Fix:** Simplify. Use primitives over nested objects.

### No Error Information
Agent can't recover from failures.

**Fix:** Return structured errors with actionable messages.

```yaml
# Bad
error: "Failed"

# Good
error:
  code: "customer_not_found"
  message: "No customer with ID 123 exists"
  suggestion: "Try searching by email instead"
```

### Dangerous Defaults
Silent side effects.

**Fix:** Require confirmation for destructive operations.

## Tool Categories

### Read Tools (Safe)
Retrieve information. No side effects.

```
search_customers, get_order_details, list_products
```

Design tips:
- Support filtering and pagination
- Return structured data
- Include relevant metadata

### Write Tools (Careful)
Modify data. Reversible side effects.

```
create_customer, update_order, add_product
```

Design tips:
- Return the modified object
- Include before/after state if helpful
- Support dry-run mode for testing

### Action Tools (Dangerous)
Execute operations. Potentially irreversible.

```
send_email, deploy_code, delete_customer
```

Design tips:
- Require explicit confirmation
- Include preview/draft mode
- Log all actions
- Support undo when possible

## Tool Response Design

### Success Response
```yaml
status: success
result:
  id: 123
  name: "John Doe"
  email: "john@example.com"
```

### Error Response
```yaml
status: error
error:
  code: "validation_failed"
  message: "Email format is invalid"
  field: "email"
  suggestion: "Use format: user@domain.com"
```

### Partial Success
```yaml
status: partial
results:
  - id: 1, status: success
  - id: 2, status: error, message: "Not found"
  - id: 3, status: success
summary:
  total: 3
  succeeded: 2
  failed: 1
```

## Testing Tools

### Unit Tests
Test tool implementation in isolation.

```python
def test_search_customers():
    result = search_customers("john")
    assert len(result) > 0
    assert "name" in result[0]
```

### Integration Tests
Test tool in agent context.

```python
def test_agent_uses_search():
    response = agent.run("Find customer John Smith")
    assert "search_customers" in response.tool_calls
    assert "John Smith" in str(response)
```

### Edge Case Tests
- Empty results
- Invalid parameters
- Permission denied
- Rate limits
- Timeout

## Implementation Checklist

- [ ] Name clearly describes the action
- [ ] Description explains what, when, and returns
- [ ] Parameters are typed and constrained
- [ ] Required vs optional is clear
- [ ] Errors are structured and actionable
- [ ] Dangerous operations require confirmation
- [ ] Tool is testable in isolation
- [ ] Response format is consistent
