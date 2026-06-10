# Data Types

> Python needs to know what kind of thing it's dealing with — a number it can do math on, or text it can slice and join.

**Back to:** [[Home]] | [[Phase 1 - Foundations]]

---

## The Four Core Types (Phase 1)

### str — text

```python
name = "Nikita"
city = 'Bangalore'    # single or double quotes — same thing
empty = ""            # empty string is valid

# Operations:
len(name)             # 6  — number of characters
name.upper()          # "NIKITA"
name.lower()          # "nikita"
name[0]               # "N"  — first character (index 0)
name[-1]              # "a"  — last character
"iki" in name         # True — substring check
name + " Kumar"       # "Nikita Kumar" — concatenation
```

### int — whole numbers

```python
age     = 22
score   = -5
big     = 1_000_000   # underscore = readable comma (no effect on value)

# Math:
age + 1    # 23
age * 2    # 44
age // 5   # 4   (floor div)
age % 5    # 2   (remainder)
```

### float — decimals

```python
height = 5.6
pi     = 3.14159
rate   = 0.075

# Division always gives float:
10 / 3    # 3.3333...

# Rounding:
round(3.14159, 2)   # 3.14
```

### bool — True or False

```python
is_student = True
is_working = False

# Bools are actually 1 and 0:
True + True   # 2
int(True)     # 1
int(False)    # 0

# Comparison operators produce bools:
10 > 5     # True
10 == 10   # True
10 != 5    # True
```

---

## Type Conversion Cheat Sheet

```
str  →  int    :  int("22")       ✅ if string looks like a number
str  →  float  :  float("3.14")   ✅ same rule
int  →  str    :  str(99)         ✅ always works
int  →  float  :  float(3)        ✅ → 3.0
float → int    :  int(3.9)        ✅ truncates (not rounds!) → 3
str  →  int    :  int("hello")    ❌ ValueError — can't convert
```

---

## How to check the type

```python
type(42)           # <class 'int'>
type("hi")         # <class 'str'>
type(3.14)         # <class 'float'>
type(True)         # <class 'bool'>

# Check in an if:
x = 42
isinstance(x, int)    # True
isinstance(x, str)    # False
```

---

## Common mistakes

```python
# 1. input() always returns str — even if user types a number
n = input("Number: ")
n + 10               # TypeError! "22" + 10 doesn't work
int(n) + 10          # ✅ fix

# 2. Mixing str + int without converting
"Age: " + 22         # TypeError
"Age: " + str(22)    # ✅ "Age: 22"

# 3. int vs float after division
10 / 2               # 5.0 (float!) not 5
10 // 2              # 5   (int)
```
