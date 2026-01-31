# Tools

<!-- CUSTOMIZE: Add or remove tools based on your agent's capabilities -->

## Core Tools

### read_file
Read source code files.

**When to use:** Understanding existing code, finding related code
**Parameters:**
- path: File to read

### write_file
Create or overwrite files.

**When to use:** Creating new files, replacing entire file content
**Parameters:**
- path: File location
- content: File content

### edit_file
Make targeted changes to existing files.

**When to use:** Modifying specific parts of existing code
**Parameters:**
- path: File location
- old_text: Text to replace
- new_text: Replacement text

### run_command
Execute shell commands.

**When to use:** Running tests, builds, linters, package managers
**Parameters:**
- command: Command to run

**Tips:**
- Run tests after changes
- Check linter output
- Use for git operations

### search_code
Search codebase for patterns.

**When to use:** Finding usage, related code, definitions
**Parameters:**
- pattern: Search pattern (regex supported)
- path: Directory to search

## Optional Tools

### run_tests
Execute test suite.

**When to use:** Verifying changes don't break existing code
**Parameters:**
- path: Test file or directory
- filter: Specific tests to run

### lint
Check code style and potential issues.

**When to use:** Before committing, catching common issues
**Parameters:**
- path: File or directory to lint

### format
Auto-format code.

**When to use:** Ensuring consistent style
**Parameters:**
- path: File or directory to format

### search_docs
Search language/framework documentation.

**When to use:** Looking up APIs, best practices
**Parameters:**
- query: What to search for

## Tool Usage Guidelines

1. **Read before writing** - Understand context first
2. **Run tests after changes** - Verify nothing broke
3. **Search before implementing** - Code may already exist
4. **Use existing patterns** - Match project conventions
