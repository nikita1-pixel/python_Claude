---
session_number: 5
date: 2026-06-09
phase: 6
topic: OOP from zero — classes, objects, __init__, methods
duration_min:
---

# Session 5 — Phase 6: OOP basics

**Goal of today:** Understand what a class and an object are, write your own class with `__init__` and methods, and create objects from it — the last foundation before Phase 8 tooling.
**Files built:** `oop_practice.py`

---

## Live Log
> RULE: paste the FULL explanation verbatim — never summarise.

### Concept 1: What is a class / object (why OOP exists)
> Why it exists: when you have many "things" that share the same shape (data + behaviour), making each by hand is repetitive and error-prone. A class is a reusable blueprint; objects are the things stamped from it.

(teaching in progress)

---

### Concepts covered (built `oops/bankacc.py`)
- Class vs object (blueprint vs instance), `__init__` (auto setup), `self` (this object)
- Methods = functions in a class acting on self; state persists between calls
- Inheritance: `class SavingAccount(BankAccount)` inherits deposit/withdraw for free
- `super().__init__(...)` runs parent setup, no duplication
- Built BankAccount (deposit/withdraw + funds check) + SavingAccount (add_interest)

### Bugs debugged (3 types — great range)
- Structural: deposit/withdraw indented INSIDE __init__ → not methods (AttributeError)
- Value: rate passed as 10 instead of 0.10 → 1000% interest. Lesson: % = decimal 0–1.
- Logic: `if amount < balance: print("Insufficient")` backwards + no else → always withdrew, went negative. Fixed: `if amount <= balance: ...withdraw... else: print insufficient`.

## Checkpoint — Phase 6 OOP
| # | Question | Answer | ✓/✗ |
|---|---|---|---|
| 1 | class vs object | After patch: class=blueprint, object=instance that holds data & does things | ✓ (patched) |
| 2 | __init__ / self | Needed teaching: __init__ = auto setup on creation; self = this object | patched |
| 3 | why s.deposit works | Got it after patch: **inheritance** | ✓ (patched) |
| 4 | super().__init__ | Roughly right: calls parent setup, avoids duplication | ✓ |
| 5 | spot-the-bug (missing self) | Correctly spotted `def meow():` needs self; clarified call stays `c.meow()` | ✓ |

**Score:** Code skills strong; vocab shaky at first, fully patched via re-check (class/object + inheritance nailed). **Phase 6: PRACTISED.**

---

## What I can now do unaided
- Write a class with `__init__`, `self`, attributes and methods
- Create multiple objects, each with own state that persists across method calls
- Build a child class that inherits from a parent and adds/overrides behavior
- Use `super().__init__()` to reuse parent setup
- Debug structural (indentation), value, and logic bugs in OOP code

## Stuck on / open questions
- Reinforce the *vocabulary* (explain-back) — code is solid but verbal definitions were shaky; re-ask "class vs object", "what is self/__init__", "why inheritance" next session as warm-up.

## Next session starts with
Warm-up re-ask of OOP vocab (30 sec), then either: (a) reach OOP MASTERED by refactoring part of the expense tracker into classes (real use), or (b) start Phase 8 (venv, pip, requirements.txt, git, VS Code debugger, tests).

