# Problem Log

> Say **"log this as a problem"** at any point and Claude adds it here instantly.
>
> Each entry has: what the problem is, why it happened, whether it is solvable or an infrastructure limit, and a verdict on whether it is worth spending time on.

**Back to:** [[Home]]

---

## Status labels

| Label | Meaning |
|---|---|
| ✅ Solvable | A real fix exists — worth spending time on |
| ⚠️ Partial | Can be improved but not fully fixed — accept the limit |
| 🏗️ Infrastructure | The way the tools are built — not your code's fault, not worth fighting |
| ⏭️ Skip | Don't spend more time here — move on |

---

## Problem 001 — No real-time error hints in the terminal REPL before hitting Enter

**Date:** 2026-06-04
**Triggered by:** Typing `Print(height)` in the REPL, hitting Enter, then seeing the NameError — wished it had flagged it before Enter.

**What the problem feels like:**
In VS Code `.py` files, there are red squiggles under mistakes as you type. In the terminal REPL (`python` or `ptpython`), nothing warns you until you hit Enter and Python crashes.

**Why this happens — the infrastructure explanation:**

```
.py file in VS Code
    └── Pylance (Language Server) watches every keystroke
    └── Analyses the whole file in real time
    └── Draws red squiggles before you run anything        ✅ WORKS

Terminal REPL (python / ptpython)
    └── Just a text box connected to a Python process
    └── No Language Server attached
    └── Python only reads your line AFTER you press Enter   ❌ NO HINTS

ptpython REPL
    └── Adds syntax colour highlighting as you type
    └── Shows function signatures (print, input, etc.)
    └── Still cannot catch NameError before Enter           ⚠️ PARTIAL
```

**Root cause in one sentence:**
The REPL is a live interpreter — it evaluates your code the moment you submit it, so there is nothing to analyse until you hit Enter. Pylance works by reading a saved file continuously, which is a fundamentally different model.

**Verdict:** 🏗️ Infrastructure — this is how REPLs work by design across every language.

**Is any fix possible?**

| Option | What it gives | Effort |
|---|---|---|
| Use `.py` file + Pylance | Full real-time red squiggles before running | Zero — already set up |
| ptpython | Syntax colour (catches `Print` visually) + signatures | Zero — already installed |
| Jupyter Notebook | Cell-by-cell execution + inline output, Pylance inside cells | Low — `pip install jupyter` |
| Fix the REPL itself | Not possible without replacing it entirely | Not worth it |

**Recommended workflow change (30-second fix):**
- Quick one-liners and experiments → REPL is fine, accept the limit
- Anything more than 2 lines → write in a `.py` file, Pylance catches errors as you type, run with `python filename.py`

**Time worth spending on this:** 0 more minutes. The `.py` file workflow already solves it.

---

## Problem 002 — (next logged problem goes here)

---

## Drift Alert Rules
*Claude flags these automatically when a problem is being over-investigated.*

A problem is worth logging, diagnosing once, and moving on if:
- It is an infrastructure limit (the tools just work that way)
- The workaround takes under 30 seconds
- Fixing it would not teach Python — it would teach tool configuration

Claude will say: **"Drift alert — [problem type]. [One-line verdict]. Back to Python."**
