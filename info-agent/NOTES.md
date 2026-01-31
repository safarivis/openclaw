# Info Agent Notes

## Origin

Created from the `researcher` blueprint, specialized for knowledge ingestion and curation.

## Purpose

Extract knowledge from external content (YouTube, articles) and help decide what's worth adding to the knowledge base or teaching to specific agents.

## Key Principle

**Always ask before implementing.** Info Agent advises and recommends - humans decide and approve.

## Workflow

```
Content (YouTube, article)
         ↓
    [Ingest Mode]
    Get transcript, extract concepts
         ↓
    [Compare Mode]
    Check against existing knowledge
         ↓
    [Advise Mode]
    Recommend what to add, where, why
         ↓
    Human Approval ← REQUIRED
         ↓
    Save to knowledge base or agent memory
```

## Use Cases

### Add to Global Knowledge Base
```
User: "Ingest this AI agents video, see if it improves our knowledge"
Info Agent:
1. Gets transcript
2. Extracts concepts
3. Compares to knowledge/
4. Reports: "3 new patterns worth adding, 5 redundant"
5. Asks: "Add these 3 patterns to knowledge/patterns/?"
User: "Yes"
Info Agent: Saves to knowledge/patterns/
```

### Teach Specific Agent
```
User: "Teach Brand Agent everything from Chris Do"
Info Agent:
1. Ingests Chris Do content
2. Extracts brand-relevant principles
3. Creates brand-agent/memory/mentors/chris-do.md
4. Asks: "Add this mentor file to Brand Agent?"
User: "Yes"
Info Agent: Saves mentor file
```

### Check Before Adding
```
User: "Is this video worth adding?"
Info Agent:
1. Ingests and extracts
2. Compares
3. Reports: "90% redundant with existing knowledge. Skip."
```

## File Locations

### Global Knowledge
```
knowledge/
├── foundations/    ← Core concepts
├── patterns/       ← Design patterns
├── tools/          ← Tool design
└── evals/          ← Evaluation methods
```

### Agent-Specific Knowledge
```
[agent]/memory/
├── mentors/
│   ├── chris-do.md
│   ├── simon-sinek.md
│   └── ...
└── [other memory files]
```

## YouTube Transcript Access

### Option 1: youtube-transcript-api (Python)
```python
from youtube_transcript_api import YouTubeTranscriptApi
transcript = YouTubeTranscriptApi.get_transcript(video_id)
```

### Option 2: Manual via yt-dlp
```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download [URL]
```

### Option 3: Web service
Use a transcript extraction service/API.

## Quality Filters

Before recommending addition, content must pass:

1. **Actionable** - Can be applied, not just theoretical
2. **Non-redundant** - Not already in knowledge base
3. **Relevant** - Applies to agent building or specific agent domain
4. **Credible** - From reputable source
5. **Clear** - Can be summarized concisely

## Integration Points

- **Agent Builder** - Uses knowledge base Info Agent curates
- **Agent Reviewer** - Reviews agents built with curated knowledge
- **All Agents** - Can have mentor knowledge added to their memory

## Limitations

- **Transcript quality** - Auto-generated transcripts may have errors
- **Context loss** - Visual content doesn't transfer
- **Subjectivity** - Value assessment requires judgment
- **Approval required** - Can't self-improve without human

## Changelog

- Initial creation from researcher blueprint
- Specialized for knowledge ingestion
- Added mentor file support for agent-specific learning
- Implemented ask-before-acting principle
