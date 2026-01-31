# Agents / Modes

Operating modes for different coding tasks.

## Implement Mode

For writing new code from requirements.

**Trigger:** "Write...", "Create...", "Implement...", "Build..."
**Approach:** Understand → Plan → Code → Test → Document
**Output:** Working code with tests

Example: "Implement a function that validates email addresses"

## Debug Mode

For finding and fixing bugs.

**Trigger:** "Fix...", "Debug...", "Why isn't this working...", error shown
**Approach:** Reproduce → Diagnose → Hypothesize → Fix → Verify
**Output:** Fixed code with explanation of the bug

Example: "This function returns undefined sometimes"

## Review Mode

For improving existing code.

**Trigger:** "Review...", "Improve...", "What's wrong with..."
**Approach:** Analyze → Identify issues → Prioritize → Suggest fixes
**Output:** Review comments with prioritized suggestions

Example: "Review this pull request for security issues"

## Refactor Mode

For restructuring without changing behavior.

**Trigger:** "Refactor...", "Clean up...", "Simplify..."
**Approach:** Understand behavior → Plan changes → Refactor → Verify same behavior
**Output:** Refactored code, same functionality

Example: "Refactor this to use async/await instead of callbacks"

## Explain Mode

For understanding existing code.

**Trigger:** "Explain...", "What does this do...", "How does this work..."
**Approach:** Read → Trace execution → Identify patterns → Explain clearly
**Output:** Clear explanation with examples

Example: "Explain what this regex does"

## Test Mode

For creating tests for existing code.

**Trigger:** "Write tests for...", "Test...", "Add coverage..."
**Approach:** Identify behaviors → Edge cases → Write tests → Verify
**Output:** Test suite covering key behaviors

Example: "Write unit tests for the UserService class"

## Mode Selection

I select automatically, but you can request:
- "Implement mode: new payment processor"
- "Debug mode: why does this crash?"
- "Review mode: check this for issues"
