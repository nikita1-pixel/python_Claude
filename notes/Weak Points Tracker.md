# Weak Points Tracker

> This file is the honest record. Every concept Nikita hesitated on, guessed wrong, or needed Claude to fix — logged here with a drill recommendation.
> 
> Updated every session wrap-up. Use this to open the NEXT session with: *"Before we move on — let's drill X from last time."*

**Back to:** [[Home]]

---

## How to read this

- **Tripped on** = what specifically went wrong (wrong prediction, runtime error, confusion)
- **Root cause** = the underlying misunderstanding
- **Drill** = the exact exercise that would patch the gap
- **Resolved?** = mark ✅ when Nikita nails it unaided in a later session

---

## Active Weak Points

| Session | Phase | Concept | Tripped on | Root cause | Drill | Resolved? |
|---|---|---|---|---|---|---|
| 1 | Phase 1 | PowerShell vs Python REPL | Ran `type("hello")` in PowerShell → error. `2+2` worked → thought it was Python. | PowerShell has its own `type` command (reads files). `>>>` = Python, `PS >` = PowerShell. | Start next session: "Which prompt means you're in Python?" | ⬜ |
| 1 | Phase 1 | Case sensitivity | Typed `Print(height)` → NameError. Python sees `Print` and `print` as different things. | Python is exact — built-ins are all lowercase. | Quick drill: spot which is wrong: `Len("hi")` `print("hi")` `Type(x)` | ⬜ |
| 1 | Phase 1 | Variable name must match exactly | Stored `you_age`, tried to use `your_age` → NameError. | Python has no fuzzy matching — the name must be character-perfect. | Before using a variable, check what you named it when you created it. | ⬜ |
| 1 | Phase 1 | `in` is a keyword, not `int()` | Typed `in(input(...))` → SyntaxError. | `in` is reserved for `for x in list`. The type-conversion function is `int()`. | Drill: what converts `"22"` to a number? `in()` or `int()`? | ⬜ |

---

## Resolved Weak Points
*(moved here once Nikita gets it clean)*

| Session fixed | Phase | Concept | Original issue | How it was drilled |
|---|---|---|---|---|
| | | | | |

---

## Patterns
*(filled as we accumulate data — look for recurring themes)*

> _Example: "Nikita consistently forgets that input() returns a string" — then we drill type conversion for 10 minutes at the start of the next 3 sessions until it's automatic._

- *(none yet — check back after 3+ sessions)*

---

## Drill Bank
*(quick exercises to fix common gaps — add one whenever a weak point surfaces)*

### Type conversion (input → int/float)
```python
# Run this in REPL, predict before hitting Enter:
x = input("Enter a number: ")   # type 5
print(x + 10)                   # what happens? why?
print(int(x) + 10)              # now what?
print(type(x), type(int(x)))    # what's the difference?
```

### Modulo (%)
```python
# Predict, then run:
print(10 % 3)    # ?
print(15 % 4)    # ?
print(7 % 7)     # ?
print(6 % 7)     # ? (tricky)
# Rule: result is always less than the divisor
```

### f-strings vs concatenation
```python
name = "Nikita"
age = 22
# Fix this without using str():
broken = "Name: " + name + " Age: " + age   # TypeError
# Write the f-string version:
fixed = f"..."
```

### Floor division vs regular division
```python
# Predict all six:
print(10 / 3)     # ?
print(10 // 3)    # ?
print(10 / 2)     # ?  (surprising one)
print(10 // 2)    # ?
print(7 / 7)      # ?
print(7 // 7)     # ?
```
