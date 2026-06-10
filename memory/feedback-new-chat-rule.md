---
name: feedback-new-chat-rule
description: When conversation gets too long, prompt Nikita to start a new chat with a ready-made context paste
metadata:
  type: feedback
---

When the conversation grows long (approaching context limits or clearly getting slow/laggy), proactively say:
"Chat's getting long — start a new one. Paste this into your first message:"
Then output the full context handoff block from `memory/handoff-template.md`.

**Session length control point:** After ~20 exchanges OR when setup/tooling takes over from actual Python learning, wrap the session. Rule: if we have spent more than 3 consecutive exchanges on tooling/setup instead of Python code, wrap and redirect.

**Wrap-up sequence (do all 4):**
1. Update study-state.md resume point
2. Add session summary to session log
3. Output the next-chat paste block
4. One-line confirmation: "Session #N done. [what was covered]. Next: [topic]."

**Why:** Nikita wants zero context loss across chats and sessions — the session logs + study-state are the memory, not the chat window.

**How to apply:** Watch for signs of length — many exchanges, repeated scrolling references, or if auto-compression kicks in. Don't wait for the user to notice. Prompt first.
