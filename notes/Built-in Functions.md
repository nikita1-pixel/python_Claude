# Built-in Functions

> Python ships ~70 ready-made tools. You call them — you don't build them.
> **Pattern:** `function_name(argument)` → returns a result

**Back to:** [[Home]] | [[Phase 1 - Foundations]]

---

## Phase 1 Core Six

| Function | What it does | Example | Returns |
|---|---|---|---|
| `print()` | Show output on screen | `print("hello")` | nothing (None) |
| `type()` | What type is this? | `type(42)` | `<class 'int'>` |
| `len()` | Count items / characters | `len("hi")` | `2` |
| `input()` | Pause, wait for user | `input("Name: ")` | string |
| `int()` | Convert to integer | `int("22")` | `22` |
| `float()` | Convert to decimal | `float("3.14")` | `3.14` |
| `str()` | Convert to string | `str(99)` | `"99"` |

---

## print() — details

```python
print("hello")              # single value
print("name:", name)        # multiple args — space separated
print(1, 2, 3, sep="-")     # custom separator → 1-2-3
print("loading", end="...") # don't add newline at end
print()                     # blank line
```

---

## input() — always returns a string

```python
raw = input("Enter a number: ")
print(type(raw))   # <class 'str'> — even if user typed 42

# Always convert if you need a number:
n = int(input("Enter a number: "))
print(n + 10)      # now this works
```

---

## Type conversion — when and why

```python
# str → int:  when you get a number from input() and want to do math
age = int(input("Age: "))

# int → str:  when you want to join a number into a string with +
msg = "Age is " + str(age)

# str → float:  for decimals
price = float(input("Price: "))

# What happens if conversion fails?
int("hello")   # ValueError — "hello" can't become a number
               # Fix: use try/except (Phase 5)
```

---

## More built-ins you'll meet soon

| Function | Phase | What it does |
|---|---|---|
| `range()` | 2 | generate a sequence of numbers |
| `list()` | 3 | convert to list |
| `dict()` | 3 | create a dictionary |
| `sorted()` | 3 | sort a list |
| `max()` / `min()` | 3 | largest / smallest |
| `sum()` | 3 | add up numbers |
| `abs()` | 4 | absolute value |
| `round()` | 4 | round a float |
| `open()` | 5 | open a file |
| `enumerate()` | 4 | loop with index |
| `zip()` | 4 | loop two lists together |
