# Agent Lab

Testing ground for agent template variants.

## Structure

| Folder | Description | Status |
|--------|-------------|--------|
| 01-baseline | Current production config (EVA) | Active |
| 02-minimal | Stripped down, less rules | Testing |
| 03-structured | More explicit rules, formal | Testing |

## How to Use

1. Edit templates in any variant folder
2. Register in `~/.openclaw/openclaw.json` to test live
3. Document changes in each folder's `NOTES.md`
4. Compare outputs with same prompts across variants

## Registered Agents

Add to `~/.openclaw/openclaw.json` under `agents.list`:

```json
{ "id": "lab-baseline", "workspace": "/home/louisdup/clawd-lab/01-baseline", "identity": { "name": "Lab Baseline", "emoji": "🔬" } },
{ "id": "lab-minimal", "workspace": "/home/louisdup/clawd-lab/02-minimal", "identity": { "name": "Lab Minimal", "emoji": "🪶" } },
{ "id": "lab-structured", "workspace": "/home/louisdup/clawd-lab/03-structured", "identity": { "name": "Lab Structured", "emoji": "📐" } }
```

## Notes

- Each variant is a complete workspace (can run independently)
- Git tracks all changes for comparison
- NOTES.md in each folder explains what's different
