# Knowledge Base

Agent Reviewer's evaluation criteria and patterns.

---

## Severity Levels

| Level | Definition | Action |
|-------|------------|--------|
| Critical | Blocks core functionality | Must fix |
| Major | Significant problems | Should fix |
| Minor | Small issues | Nice to fix |
| Polish | Suggestions | Optional |

## Review Categories

| Category | Checks |
|----------|--------|
| Identity | Who is this agent? Role, mission, boundaries |
| Capability | Can it do what it claims? Modes, tools |
| Safety | Are there guardrails? Limits, warnings |
| Clarity | Is it documented? Examples, notes |

## Pass Criteria

- Score >= 8.5/10
- Zero critical issues
- All required files present

## Common Issues

| Issue | Category | Severity |
|-------|----------|----------|
| Missing IDENTITY.md | Identity | Critical |
| No "Done when:" in modes | Capability | Major |
| Tools not typed | Capability | Major |
| No constraints in SOUL.md | Safety | Minor |

---

*See knowledge/evals/ for detailed evaluation methods.*
