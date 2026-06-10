---
name: feedback-drift-alert
description: Flag when Nikita is over-investigating an infrastructure problem and redirect back to learning
metadata:
  type: feedback
---

When Nikita spends more than 2 exchanges on a problem that is a known infrastructure limit (REPL behaviour, OS differences, editor setup, tool configuration), say:

"Drift alert — [problem type]. [One-line verdict]. Back to Python."

Then redirect immediately to the next learning concept.

**Why:** Nikita explicitly asked to be warned when drifting into infrastructure rabbit holes. These problems feel solvable but are often just "how the tool works" — investigating them burns learning time without teaching Python.

**How to apply:**
- Infrastructure problems: REPL limits, terminal vs editor differences, pip/venv behaviour, OS quirks
- Solvable in 30 seconds or less → give the fix, move on, no extended discussion
- Not solvable → one clear explanation, log to Problem Log.md, move on
- Never spend more than 1 response on a tool/setup problem unless Nikita explicitly asks to go deeper
