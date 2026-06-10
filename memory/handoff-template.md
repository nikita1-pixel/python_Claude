---
name: handoff-template
description: Paste this at the start of any new chat to restore full learning context instantly
metadata:
  type: reference
---

# New Chat Context Handoff

When Nikita starts a new chat (because old one got too long), she pastes the block below.
Claude reads it and continues exactly where the old chat left off — no cold start.

---

## The paste block (copy everything between the lines)

---
I'm Nikita. I'm doing Python zero-to-job-ready learning with Claude Code.
My repo is at: C:\Users\nirma\OneDrive\Desktop\python\python_Claude

Please read these files to restore full context before responding:
1. memory/study-state.md         ← resume point + phase status
2. obsidian/Weak Points Tracker.md  ← what to drill before new content
3. obsidian/Session Logs/ ← pick the most recent file for last session detail

Then greet me with the resume line from study-state.md and ask if I want to continue, drill weak points, or jump somewhere.

Do NOT summarise what you read back to me — just use it and resume.
---

---

## What each file gives Claude

| File | What it restores |
|---|---|
| `memory/study-state.md` | Exact resume point, phase statuses, session count, open questions |
| `obsidian/Weak Points Tracker.md` | Every concept Nikita tripped on — drill these first |
| `obsidian/Session Logs/[latest].md` | Full verbatim last session — what was coded, what errored, what was explained |
| `CLAUDE.md` | Full mentor rules — auto-loaded by Claude Code in the repo directory |

---

## When Claude Code is used (terminal in the repo folder)

Claude Code auto-loads CLAUDE.md on every session — so in the terminal, context is always warm.
The paste block above is only needed for claude.ai web chats or a different machine.
