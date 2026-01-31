# Coder Blueprint Notes

## When to Use This Blueprint

Use the Coder blueprint for agents that primarily:
- Write new code from requirements
- Fix bugs and debug issues
- Review and improve code quality
- Refactor and optimize
- Generate tests

## Common Customizations

### Language Specialization
Focus on specific languages:
```markdown
## Languages
Primary: TypeScript, JavaScript
Secondary: Python
Framework expertise: React, Node.js, FastAPI
```

### Code Style
Define conventions:
```markdown
## Code Style
- Use Prettier defaults
- Prefer functional over class-based
- Use named exports
- Error handling with Result types
```

### Project Context
Add project-specific knowledge:
```markdown
## Project Conventions
- All API routes in src/routes/
- Database models in src/models/
- Use Zod for validation
- Tests co-located with source files
```

### Security Focus
Emphasize security concerns:
```markdown
## Security Requirements
- Always validate user input
- Use parameterized queries
- Sanitize output for XSS
- Log security events
```

## Limitations

- **Testing blind spots** - May miss edge cases
- **Performance** - First solution may not be optimal
- **Security** - Should be reviewed for security-critical code
- **Architecture** - Complex design decisions need human input

## Tips for Better Results

1. **Share context** - Project structure, conventions, constraints
2. **Provide examples** - Show existing code patterns
3. **Be specific** - "Add retry logic" vs "Make this more robust"
4. **Review output** - Don't blindly trust generated code
5. **Run tests** - Verify changes work as intended

## Example Use Cases

- Feature implementation
- Bug fixing
- Code review assistance
- Test generation
- Documentation generation
- Refactoring

## What This Blueprint Isn't For

- Content writing (use Writer)
- Research tasks (use Researcher)
- Business operations (use Business)
- Architecture decisions (needs human judgment)

## Security Notes

The Coder agent should:
- Never hardcode secrets
- Validate all inputs
- Use parameterized queries
- Escape output appropriately
- Avoid eval() and similar

Review security-critical code carefully.
