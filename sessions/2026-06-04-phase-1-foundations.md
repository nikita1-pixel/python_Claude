---
session_number: 1
date: 2026-06-04
phase: 1
topic: Foundations — How Python Works + Built-in Functions
duration_min: ~90
---

# Session 1 — Phase 1: Foundations

**Goal of today:** Understand how Python executes code, use the terminal REPL confidently, know the core data types, and call built-in functions unaided.
**Files built:** `hello.py`, `basics_practice.py`

---

## Live Log

### Concept 1: Python REPL vs Script Files
> Why it exists: The REPL lets you experiment instantly — no save, no run, just type and see. Scripts let you save and repeat work.

Two ways to run Python:
1. **REPL** (`python` in terminal) — live, interactive, one line at a time. Great for quick experiments.
2. **Script** (`.py` file) — saved code you run with `python filename.py`. For real programs.

```
# In terminal — type this to open REPL:
python

# You'll see:
>>> 

# Type anything:
>>> 2 + 2
4
>>> print("hello")
hello

# Exit REPL:
>>> exit()
```

**Ran it — output:** _(fill in what you saw)_
**Predict-and-change:** _(change 2+2 to 10*5, predict 50 — was it right?)_
**Sanity check:** _(did `>>>` appear? did exit() close it?)_

---

### Concept 2: Variables
> Why it exists: Programs need to remember things. Variables are labelled boxes that hold values.

```python
# A variable = a name that points to a value
name = "Nikita"         # str (text)
age = 22                # int (whole number)
height = 5.6            # float (decimal number)
is_student = True       # bool (True or False)

print(name)
print(age)
print(height)
print(is_student)
```

**Ran it — output:** _(fill in)_
**Predict-and-change:** _(change name to your own name, predict the new output)_

---

### Concept 3: Data Types + type()
> Why it exists: Python treats numbers, text, and True/False very differently. `type()` tells you exactly what something is.

```python
# type() is a built-in function — pass it any value, it tells you the type
print(type("hello"))    # <class 'str'>
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>

x = 100
print(type(x))          # <class 'int'>
```

**Practice in REPL:**
```
>>> type("Nikita")
>>> type(99)
>>> type(3.14)
>>> type(True)
```

**Ran it — output:** _(fill in)_

---

### Concept 4: Built-in Functions — the Python toolbox
> Why it exists: Python ships with ~70 ready-made tools (functions). You don't build them — you call them.

The pattern is always: `function_name(input)` → gives you back a result.

```python
# print() — shows output
print("Hello, world!")

# len() — counts items in a string or list
print(len("Nikita"))        # 6 (number of letters)
print(len("Hello World"))   # 11

# input() — pauses and waits for the user to type something
name = input("What's your name? ")
print("Hi,", name)

# int(), float(), str() — convert between types
age_text = "22"             # this is a string, not a number
age_number = int(age_text)  # now it's an int you can do math with
print(age_number + 1)       # 23

pi_text = "3.14"
pi_number = float(pi_text)
print(pi_number * 2)        # 6.28

number = 99
number_as_text = str(number)
print("My number is " + number_as_text)  # join strings with +
```

**Ran it — output:** _(fill in)_

---

### Concept 5: f-strings (formatted strings)
> Why it exists: Gluing variables into text with `+` gets ugly fast. f-strings are clean, readable, and what every real Python dev uses.

```python
name = "Nikita"
age = 22
city = "Bangalore"

# Old clunky way (don't use this):
print("Name: " + name + ", Age: " + str(age))

# f-string — put an f before the quote, variables go in {}
print(f"Name: {name}, Age: {age}, City: {city}")

# You can do math inside {}:
print(f"In 5 years, you'll be {age + 5}")

# Works with any expression:
price = 100
discount = 0.2
print(f"Price after {discount*100}% off: {price - price*discount}")
```

**Ran it — output:** _(fill in)_
**Predict-and-change:** _(change age to 25, predict the second print)_

---

### Concept 6: Math Operators
> Why it exists: Python is a calculator — but also builds financial apps, games, ML models. Arithmetic is everywhere.

```python
a = 10
b = 3

print(a + b)    # 13 — addition
print(a - b)    # 7  — subtraction
print(a * b)    # 30 — multiplication
print(a / b)    # 3.333... — division (always gives float)
print(a // b)   # 3  — floor division (drop the decimal)
print(a % b)    # 1  — modulo (remainder after dividing)
print(a ** b)   # 1000 — exponent (10 to the power of 3)
```

**Practice in REPL — predict before running:**
```
>>> 17 % 5      # what's the remainder?
>>> 2 ** 8      # what's 2 to the power of 8?
>>> 7 // 2      # what happens to the .5?
```

---

### Concept 7: Comments
> Why it exists: Code is read by humans more than machines. Comments explain the WHY — future you will thank present you.

```python
# This is a single-line comment — Python ignores everything after #

name = "Nikita"   # inline comment — fine for short notes

# Multi-line? Just use multiple # lines:
# Step 1: get the user's name
# Step 2: greet them
name = input("Name: ")
print(f"Hey {name}!")
```

---

## Mini Build — Interactive Greeter

```python
# basics_practice.py
# A tiny CLI tool using everything from Phase 1

name = input("What's your name? ")
age = int(input("How old are you? "))
city = input("Which city? ")

print()  # blank line for spacing
print(f"Nice to meet you, {name}!")
print(f"You're {age} years old, living in {city}.")
print(f"In 10 years you'll be {age + 10}.")
print(f"Your name has {len(name)} letters.")
print(f"Type of age variable: {type(age)}")
```

**Ran it — output:** _(fill in your answers)_

---

## Checkpoint (Phase 1)

| # | Question | Answer | ✓/✗ |
|---|---|---|---|
| 1 | What does `type("hello")` return? | | |
| 2 | What's the output of `10 % 3`? | | |
| 3 | Fix this bug: `print("Age: " + 22)` | | |
| 4 | Write an f-string that prints `"Pi is 3.14"` using a variable | | |
| 5 | What does `len("Python")` return? | | |
| 6 | Explain: what's the difference between `//` and `/`? | | |

**Score:** /6 · **Gaps patched:** —

---

## What I can now do unaided
- Open the Python REPL and run code live
- Declare variables with the right type
- Call built-in functions: print, type, len, input, int, float, str
- Write f-strings to embed variables in text
- Do arithmetic including `%` and `//`
- Add comments

## Stuck on / open questions
-

## Next session starts with
Phase 2 — Control Flow: if/else, while loops, for loops → build a number-guessing game
