# Phase 1 — Foundations

> **The point:** Every Python program — from a 3-line script to a Netflix recommendation engine — runs on these exact building blocks. Get these solid and everything else clicks.

**Status:** 🔥 Active  
**Back to:** [[Home]]

---

## 1. How Python Runs Code

Two modes — pick the right one for the job:

```
REPL  →  type in terminal, instant output, great for experiments
Script →  save as .py, run with python filename.py, for real programs
```

**Open the REPL:**
```bash
python
```
You'll see `>>>`. That's Python waiting. Type anything, hit Enter, see the result immediately.

**Exit REPL:**
```python
exit()
```

> [!tip] Rule of thumb
> REPL = scratch pad. Script = real work you want to save.

---

## 2. Variables

A variable is a **named box** that holds a value. Python figures out the type automatically.

```python
name     = "Nikita"   # str  — text goes in quotes
age      = 22         # int  — whole number, no quotes
height   = 5.6        # float — decimal number
student  = True       # bool — only True or False (capital T/F)
```

**Rules for naming variables:**
- Use lowercase + underscores: `user_name` not `UserName`
- No spaces, no starting with a number
- Make the name describe what it holds

> [!warning] Common mistake
> `age = "22"` — this is a **string**, not a number. You can't do math on it until you convert it with `int(age)`.

---

## 3. Data Types

| Type | What it holds | Example |
|---|---|---|
| `str` | Text (always in quotes) | `"hello"`, `'Nikita'` |
| `int` | Whole numbers | `42`, `-7`, `0` |
| `float` | Decimal numbers | `3.14`, `-0.5` |
| `bool` | True or False only | `True`, `False` |

**Check the type of anything:**
```python
type("hello")   # <class 'str'>
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type(True)      # <class 'bool'>
```

See [[Data Types]] for the full cheat sheet.

---

## 4. Built-in Functions 🛠️

Python ships with ~70 ready-made tools. **Pattern: `function_name(input)` → gives you a result.**

### The core six for Phase 1:

```python
# print() — show output on screen
print("Hello!")
print(42)
print(name, age)   # can print multiple things separated by commas

# type() — what type is this value?
type("hello")      # <class 'str'>

# len() — how many items / characters?
len("Nikita")      # 6
len([1, 2, 3])     # 3

# input() — pause and wait for user to type something
name = input("Enter your name: ")

# int(), float(), str() — convert between types
int("22")          # 22  (str → int)
float("3.14")      # 3.14 (str → float)
str(99)            # "99" (int → str)
```

> [!important] Why conversion matters
> `input()` **always returns a string**, even if the user types a number.
> So: `age = int(input("Age: "))` — without `int()`, you can't do math on `age`.

See [[Built-in Functions]] for the full reference.

---

## 5. f-strings (formatted strings)

The clean way to embed variables inside text. Every real Python dev uses these.

```python
name = "Nikita"
age  = 22

# Ugly old way — don't do this:
print("Hello " + name + ", you are " + str(age))

# f-string — put f before the opening quote, variables go in { }
print(f"Hello {name}, you are {age}")
# Output: Hello Nikita, you are 22

# You can run expressions inside { }:
print(f"In 10 years: {age + 10}")
print(f"Name length: {len(name)}")
print(f"Upper: {name.upper()}")
```

**Anatomy of an f-string:**

```
f"  text here   {  variable or expression  }  more text  "
↑               ↑                          ↑
f prefix        curly brace opens           curly brace closes
```

---

## 6. Math Operators

```python
10 + 3    # 13  — addition
10 - 3    # 7   — subtraction
10 * 3    # 30  — multiplication
10 / 3    # 3.333... — division (always float)
10 // 3   # 3   — floor division (drops the decimal)
10 % 3    # 1   — modulo = remainder after dividing
10 ** 3   # 1000 — exponentiation (10 to the power of 3)
```

> [!tip] Modulo trick
> `x % 2 == 0` → x is even. `x % 2 == 1` → x is odd.
> Used constantly in real code.

---

## 7. Comments

```python
# Single line comment — Python ignores everything after #

name = "Nikita"   # inline comment on same line as code

# Use comments to explain WHY, not WHAT:
# Bad:  x = x + 1   # adds 1 to x
# Good: x = x + 1   # account for 0-based indexing
```

---

## Mini Build — Interactive Greeter

```python
# basics_practice.py
# Uses: input, int, f-strings, len, type, math

name = input("What's your name? ")
age  = int(input("How old are you? "))
city = input("Which city? ")

print()
print(f"Nice to meet you, {name}!")
print(f"You're {age} in {city}.")
print(f"In 10 years you'll be {age + 10}.")
print(f"Your name has {len(name)} letters.")
print(f"Type of age: {type(age)}")
```

Run it: `python basics_practice.py`

---

## Phase 1 Checkpoint

Answer these before moving to Phase 2:

1. What does `type("hello")` return?
2. What's the output of `10 % 3`?
3. Fix the bug: `print("Age: " + 22)`
4. Write an f-string that prints `"Pi is 3.14"` using a variable `pi = 3.14`
5. What does `len("Python")` return?
6. What's the difference between `/` and `//`?

Score 5/6+ → Phase 2. Below that → patch the gaps first.

---

**Next:** [[Phase 2 - Control Flow]] — if/else, loops, number-guessing game
