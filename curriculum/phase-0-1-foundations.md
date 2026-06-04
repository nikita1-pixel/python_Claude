# Phase 0 + 1 — Setup & Foundations (fast-recap session guide)

> Run as **one compressed session** (~90 min) ending in a checkpoint. If the checkpoint lands, advance to Phase 2 at normal pace. The checkpoint is non-negotiable — it's what stops the fast-recap from leaving holes.

This is the mentor's lesson plan for Session #1. Teach it live, log it verbatim into `sessions/`.

---

## Part A — Setup (Phase 0)

### Why first
You can't learn to code by reading. We get a real loop going: write a line → run it → see it happen. That feedback loop *is* the skill.

### Steps
1. **Confirm VS Code Python extension.** In VS Code: Extensions panel → search "Python" (by Microsoft) → install if missing. (Needed for the run button, intellisense, debugger.)
   - Verify Python itself: in the integrated terminal (`` Ctrl+` ``), run `python3 --version` (or `python --version` on Windows) → should print `Python 3.x`.
2. **Make a workspace.** Create files in `projects/`, or a separate practice folder. Open it: `code .`
3. **The REPL** — type `python3` in the terminal. This is a live scratchpad: type `2 + 2`, press Enter, see `4`. Type `exit()` to leave. Use it to test tiny things.
4. **A `.py` file** — the real way. Create `hello.py`, write `print("Hello, world")`, run with `python3 hello.py`. Explain: REPL is for quick experiments; `.py` files are programs you save and re-run.
5. **Comments** — `# this is a comment`, ignored by Python, notes for humans.

**Build A:** a `hello.py` that prints 3 lines about the learner.
**Sanity check:** the file runs from the terminal with no error and prints exactly what's expected.

---

## Part B — Foundations (Phase 1)

Teach in this order, one at a time, each with a run + a predict-and-change.

### 1. Variables — naming a value
> Why: so you can store something now and use it later.
```python
name = "Sam"           # a box labelled 'name' holding text
age = 21               # a box holding a number
print(name, age)
```
PEP-8 nudge: lowercase, words joined by underscores (`first_name`), descriptive.

### 2. Types — what kind of value
> Why: Python treats text and numbers differently; mixing them wrong is the #1 beginner bug.
- `int` — whole number `21`
- `float` — decimal `21.5`
- `str` — text, always in quotes `"hi"`
- `bool` — `True` / `False`
```python
print(type(age))       # <class 'int'>
print(type(name))      # <class 'str'>
```

### 3. Strings & f-strings — text you can build
> Why: almost every program shows text to a human.
```python
greeting = f"Hi {name}, you are {age} years old."
print(greeting)
print(name.upper())            # methods: things strings can do
print(len(name))               # length
```
The `f"..."` is an f-string: drop a variable in `{ }` and Python fills it in. This is the single most-used string tool — drill it.

### 4. Numbers & operators
```python
print(10 + 3)    # 13
print(10 - 3)    # 7
print(10 * 3)    # 30
print(10 / 3)    # 3.333...  (always a float)
print(10 // 3)   # 3   floor division
print(10 % 3)    # 1   remainder (modulo)
print(10 ** 2)   # 100 power
```
Modulo `%` matters — it's how you check even/odd (`n % 2 == 0`) and it powers the Phase 2 game.

### 5. Input & type conversion
> Why: a program that talks back. **Gotcha:** `input()` always gives a *string*, even "21".
```python
user_age = input("Your age? ")        # this is text "21", not number 21
user_age = int(user_age)              # convert to int to do math
print(f"Next year you'll be {user_age + 1}")
```
Show the bug first: `input() + 1` crashes → then fix with `int()`. The crash is the lesson.

**Build B (the payoff):** a tiny interactive CLI tool — `about_you.py`:
- asks name and birth year,
- computes age,
- prints a friendly f-string summary.

**Sanity check:** run it, type real answers, confirm the math is right. Then ask: "what happens if you type letters for the year?" → it crashes → seed the idea that Phase 5 (error handling) fixes this.

---

## Checkpoint — Phase 0+1 (must pass to advance)
Mix of formats. Log questions + answers in the session file.
1. **Predict:** what does `print(7 // 2, 7 % 2)` output?
2. **Predict:** what's `type(7 / 2)` — int or float? Why?
3. **Spot the bug:** `age = input("age "); print(age + 1)` — what breaks and how do you fix it?
4. **Write it:** given `name = "amit"`, print `Hello, AMIT!` using an f-string + a method.
5. **Explain back:** what's the difference between the REPL and a `.py` file?
6. **Write it:** a 3-line script that stores two numbers and prints their average.

Pass ≈ 5/6. Gaps → patch on the spot, note in study-state Open Questions, *then* advance to Phase 2.
