# Python Learning Guide — Nikita
### Built from the 13-hour transcript. Estimated reading + practice time: ~6 hours.

---

## VIDEO VERDICT
| Section | Watch? | Why |
|---------|--------|-----|
| 00:00 – 13:00 | ✅ Watch | Animated visuals of how Python executes code are genuinely good |
| 13:00 – end | ⏭ Skip | Everything below covers it faster |

---

# MODULE 1 — Python Fundamentals

## Comments
```python
# Single line comment

# Multi-line:
# Step 1: load data
# Step 2: clean data
# Step 3: analyze

x = 10  # inline comment — keep short
```

## Print
```python
print("Hello")               # double quotes
print('Hello')               # single quotes — same thing
print("Hi", "Nikita")        # comma adds space automatically
print("Line1\nLine2")        # \n = new line
print("Col1\tCol2")          # \t = tab
print("Say \"hello\"")       # \" = escaped quote inside double quotes
print("Path: C:\\Users")     # \\ = literal backslash
print("""
Line 1
Line 2
Line 3
""")                         # triple quotes = multi-line
```

**Real use:** Print intermediate results while building analysis scripts to verify your logic.

## Variables
```python
name = "Nikita"
age = 25
salary = 45000.50
is_student = False
empty = None

# Update
age = 26          # reassign
age += 1          # shortcut: age = age + 1
salary *= 1.10    # 10% raise
```

**Rule:** One equal `=` assigns. Two equals `==` compares.

## User Input
```python
name = input("Enter your name: ")    # always returns a string
age = int(input("Enter age: "))      # convert to int manually
```

## Data Types
| Type | Example | Notes |
|------|---------|-------|
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimals |
| `str` | `"hello"` | Always in quotes |
| `bool` | `True` / `False` | Capital first letter |
| `None` | `None` | No value / unknown |

```python
# Check data type
type(42)         # <class 'int'>
type("hello")    # <class 'str'>
type(True)       # <class 'bool'>
type(None)       # <class 'NoneType'>

# Convert types
int("42")        # → 42
float("3.14")    # → 3.14
str(100)         # → "100"
bool(0)          # → False
bool("hi")       # → True
```

**Challenge:** Ask user for name and age. Print: `"Hi [name], you'll be [age+1] next year."`

---

# MODULE 2 — Working with Strings

Strings are sequences. Every character has an index (position number starting at 0).

```
 H  e  l  l  o
 0  1  2  3  4     (positive index)
-5 -4 -3 -2 -1     (negative index)
```

## Indexing — Get one character
```python
word = "Python"
word[0]    # 'P'  (first)
word[-1]   # 'n'  (last)
word[2]    # 't'
```

## Slicing — Get multiple characters
```python
# [start : stop]  — stop is NOT included
word[0:3]   # 'Pyt'
word[:3]    # 'Pyt'  (start defaults to 0)
word[3:]    # 'hon'  (end defaults to last)
word[::2]   # 'Pto'  (every 2nd character)
word[::-1]  # 'nohtyP'  (reverse)
```

## String Methods — The Big List

### Type & Conversion
```python
type("hello")       # <class 'str'>
str(42)             # "42" — convert to string
```

### Measurement
```python
len("hello")           # 5 — number of characters
"ll".count("l")        # 2 — count occurrences
"Python".count("P")    # 1 — case sensitive
```

### Transformations
```python
# Case
"hello".upper()         # "HELLO"
"HELLO".lower()         # "hello"

# Cleaning whitespace
"  hi  ".strip()        # "hi"  — both sides
"  hi  ".lstrip()       # "hi  "  — left only
"  hi  ".rstrip()       # "  hi"  — right only

# Replace
"2026/05/30".replace("/", "-")    # "2026-05-30"
"$1,299.99".replace("$", "").replace(",", "")  # "1299.99"

# Split
"2026-05-30".split("-")    # ['2026', '05', '30']
"a,b,c".split(",")         # ['a', 'b', 'c']

# Join (opposite of split)
"-".join(["2026", "05", "30"])  # "2026-05-30"
```

### F-Strings (Modern Way to Build Strings)
```python
name = "Nikita"
age = 25
score = 95.678

# Old way (annoying)
print("Hi " + name + ", you are " + str(age))

# Modern way — f-string
print(f"Hi {name}, you are {age}")
print(f"Score: {score:.2f}")   # 2 decimal places → "Score: 95.68"
print(f"2 + 3 = {2 + 3}")      # expressions work too
```

### Searching
```python
text = "sara@gmail.com"

"@" in text               # True — exists anywhere
"@" not in text           # False
text.startswith("sara")   # True — from the left
text.endswith(".com")     # True — from the right
text.find("@")            # 4 — returns index of first match (-1 if not found)
```

### Validation
```python
"abc".isalpha()      # True — only letters
"123".isnumeric()    # True — only digits
"abc123".isalnum()   # True — letters or digits
```

## Real Data Analyst Use Cases
```python
# Standardize column values before analysis
name = "  MARIA  "
clean = name.strip().lower()   # "maria"

# Extract year from date string
date = "2026-05-30"
year = date[:4]               # "2026"
month = date[5:7]             # "05"

# Validate before storing
email = input("Email: ").strip().lower()
if "@" in email and "." in email:
    print("Valid email")

# Clean price data
price_str = "$1,299.99"
price = float(price_str.replace("$", "").replace(",", ""))  # 1299.99
```

**Challenge:** Given `"  JOHN_SMITH_ENG_USA  "`, extract: first name, last name, role, country as separate variables. Clean the data.

---

# MODULE 3 — Working with Numbers

## Operators
```python
10 + 3    # 13  — addition
10 - 3    # 7   — subtraction
10 * 3    # 30  — multiplication
10 / 3    # 3.333...  — division (always float)
10 // 3   # 3   — floor division (drops decimal)
10 % 3    # 1   — modulus (remainder)
2 ** 10   # 1024 — exponent

# Shortcuts
x = 10
x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
x //= 5  # x = 4
```

## Rounding
```python
abs(-8)           # 8 — absolute value (no sign)
round(3.567)      # 4 — standard rounding
round(3.567, 2)   # 3.57 — keep 2 decimals
round(3.5)        # 4 — banker's rounding (round half to even)

import math
math.floor(3.9)   # 3 — always round DOWN
math.ceil(3.1)    # 4 — always round UP
math.trunc(3.9)   # 3 — just drop the decimal, no rounding
```

**When to use what:**
- `round()` → reports, dashboards, displaying prices
- `math.ceil()` → resource allocation ("always have enough")
- `math.floor()` → conservative estimates
- `int()` or `math.trunc()` → just need whole number, no rounding needed

## Random Numbers
```python
import random
random.random()           # float between 0 and 1
random.randint(1, 100)   # integer between 1 and 100 (inclusive)
```

## Type Checking
```python
7.0.is_integer()          # True — float that is actually whole
isinstance(42, int)       # True
isinstance(42.0, float)   # True
isinstance("hi", str)     # True
```

**Challenge:** Generate a random number 1–100. Print if it's even or odd.

---

# MODULE 4 — Control Flow

## Boolean Basics
```python
True
False
bool(0)        # False
bool("")       # False
bool(None)     # False
bool([])       # False (empty list)
bool("hi")     # True
bool(42)       # True
```

## Comparison Operators
```python
5 == 5     # True
5 != 3     # True
5 > 3      # True
5 < 3      # False
5 >= 5     # True
5 <= 4     # False

# Chain comparison (Pythonic "between")
18 <= age <= 65    # True if age is between 18 and 65
```

## Logical Operators
```python
# and — BOTH must be True
True and True    # True
True and False   # False

# or — at least ONE must be True
True or False    # True
False or False   # False

# not — flips True/False
not True         # False
not False        # True
```

## Membership & Identity
```python
"a" in "data"          # True
3 in [1, 2, 3]         # True
"x" not in "hello"     # True

x = None
x is None              # True  ← use 'is' with None, not ==
x is not None          # False
```

## If / Elif / Else
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)   # "B"
```

**Rules:**
- `if` — first condition, required
- `elif` — follow-up conditions, optional, as many as you want
- `else` — fallback, optional, must come last
- Once one condition is True, Python skips the rest

## Inline If (Ternary)
```python
# For simple one-liners only
status = "pass" if score >= 60 else "fail"
label = "high" if price > 100 else "medium" if price > 50 else "low"
```

## Match / Case (Python 3.10+)
```python
# Use when comparing one value to many fixed options
country_code = "DE"

match country_code:
    case "DE":
        print("Germany")
    case "FR":
        print("France")
    case "IN":
        print("India")
    case _:             # default
        print("Unknown")
```

## For Loop
```python
# Iterate over a list
for name in ["Alice", "Bob", "Charlie"]:
    print(name)

# Iterate N times
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step=2)
    print(i)

# Get index + value together
for i, name in enumerate(["Alice", "Bob"], start=1):
    print(f"{i}. {name}")

# Loop over string characters
for char in "Python":
    print(char)
```

## While Loop
```python
# Counter-based
count = 1
while count <= 5:
    print(count)
    count += 1    # MUST update or infinite loop!

# Event-based (while True + break)
while True:
    answer = input("Type 'yes' to continue: ")
    if answer == "yes":
        break
    print("Try again.")
```

## Loop Control
```python
# break — stop the loop completely (emergency exit)
for item in data:
    if item is None:
        print("Found bad data — stopping")
        break

# continue — skip this iteration, keep going
for item in data:
    if item == "":
        continue    # skip empty items
    process(item)

# else on for loop — runs ONLY if loop completed without break
for item in emails:
    if "@" not in item:
        print(f"Bad email: {item}")
        break
else:
    print("All emails valid")   # only prints if no break happened
```

**Challenge:** Print the 7× table (7×1 through 7×10) using a loop. Then build a number guessing game (random 1–100, user guesses until correct).

---

# MODULE 5 — Data Structures

## Choosing the Right Type
| Type | Ordered | Duplicates | Mutable | Access By | Use When |
|------|---------|-----------|---------|-----------|----------|
| `list` | ✅ | ✅ | ✅ | Index | Default choice |
| `tuple` | ✅ | ✅ | ❌ | Index | Data that must not change |
| `set` | ❌ | ❌ | ✅ | — | Unique values, fast lookup |
| `dict` | ✅ | Keys: ❌ | ✅ | Key | Related info, mapping |

---

## Lists `[]`

### Create
```python
names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, None]
empty = []
matrix = [[1, 2, 3], [4, 5, 6]]   # 2D list
```

### Read
```python
names[0]     # "Alice"  (first)
names[-1]    # "Charlie"  (last)
names[1:3]   # ["Bob", "Charlie"]  (slice)
names[:2]    # ["Alice", "Bob"]
names[1:]    # ["Bob", "Charlie"]
```

### Analyze
```python
len(numbers)         # 5
max(numbers)         # 5
min(numbers)         # 1
sum(numbers)         # 15
sorted(numbers)      # returns new sorted list
numbers.count(3)     # 1 — how many times 3 appears
numbers.index(3)     # 2 — position of first 3
3 in numbers         # True
all([1, 2, 3])       # True — all truthy
any([0, 0, 1])       # True — at least one truthy
```

### Modify
```python
names.append("Diana")           # add to end
names.insert(1, "Eve")         # insert at position 1
names.remove("Bob")            # remove by value (first match)
names.pop()                    # remove & return last item
names.pop(0)                   # remove & return item at index 0
names[0] = "Anna"              # update by index
names.clear()                  # remove everything
```

### Sort & Organize
```python
numbers.sort()                  # sort in-place, ascending
numbers.sort(reverse=True)      # sort in-place, descending
numbers.reverse()               # flip in-place
sorted(numbers)                 # returns new sorted list (original unchanged)
```

### Copy (Important!)
```python
# WRONG — both variables point to same list
copy = original               # changes to one affect both!

# Correct for simple lists
copy = original.copy()

# Correct for nested lists (matrix)
import copy
deep = copy.deepcopy(original)
```

### Combine
```python
a = [1, 2]
b = [3, 4]
combined = a + b              # [1, 2, 3, 4] — new list
a.extend(b)                   # stretches a to [1, 2, 3, 4]
pairs = list(zip(a, b))       # [(1, 3), (2, 4)] — pair by position
```

### Unpack
```python
name, age, city = ["Nikita", 25, "Berlin"]
first, *rest = [1, 2, 3, 4, 5]        # first=1, rest=[2,3,4,5]
first, *middle, last = [1,2,3,4,5]    # first=1, last=5
name, _, country = ["Nikita", 25, "India"]  # _ = throw away
```

### Iterate
```python
for item in names:
    print(item)

for i, item in enumerate(names):
    print(f"{i}: {item}")
```

### Transformation & Filtering — map, filter, list comprehension
```python
# map — apply function to every item
upper_names = list(map(str.upper, names))
clean_names = list(map(str.strip, names))

# filter — keep items that pass condition
long_names = list(filter(lambda x: len(x) > 4, names))

# LIST COMPREHENSION — most Pythonic (combines loop + filter + transform)
# Syntax: [expression  for item in list  if condition]

# Transform only
squares = [x**2 for x in range(10)]

# Filter only
evens = [x for x in range(20) if x % 2 == 0]

# Transform + filter
big_prices = [p * 0.9 for p in prices if p > 100]   # 10% discount on items over 100

# Clean a list of strings
clean = [s.strip().lower() for s in names if s.strip() != ""]
```

**List comprehension is the most important Python pattern for data analysts. Master it.**

---

## Tuples `()`

```python
config = ("localhost", 5432, "mydb")   # database connection — should not change
coords = (48.8566, 2.3522)             # lat/long

# Access same as list
config[0]    # "localhost"
config[1:]   # (5432, "mydb")

# Unpack
host, port, db = config

# Can't modify
config[0] = "newhost"   # TypeError!
```

**Use when:** Data must be protected. DB credentials, coordinates, RGB colors, fixed settings.

---

## Sets `{}`

```python
unique_ids = {101, 102, 103, 101}   # {101, 102, 103} — duplicate removed

# Add / Remove
unique_ids.add(104)
unique_ids.discard(999)    # safe remove (no error if missing)
unique_ids.remove(101)     # removes, raises error if missing

# Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # Union: {1,2,3,4,5,6} — everything from both
a & b    # Intersection: {3,4} — only what's in BOTH
a - b    # Difference: {1,2} — in a but NOT in b
a ^ b    # Symmetric diff: {1,2,5,6} — in one but NOT both

# Check relationships
a.issubset(b)      # Is every item of a in b?
a.issuperset(b)    # Does a contain everything in b?
a.isdisjoint(b)    # Do they share nothing?
```

**Use when:** Finding duplicates, comparing datasets, fast membership checks.

```python
# Practical: remove duplicates from a list
ids = [1, 2, 2, 3, 3, 3]
unique = list(set(ids))   # [1, 2, 3]

# Find customers in both lists
vip = {"Alice", "Bob", "Charlie"}
buyers = {"Bob", "Charlie", "Diana"}
vip_buyers = vip & buyers   # {"Bob", "Charlie"}
```

---

## Dictionaries `{key: value}`

```python
user = {
    "id": 1,
    "name": "Nikita",
    "age": 25,
    "city": "Delhi"
}
```

### Access
```python
user["name"]              # "Nikita" — KeyError if missing
user.get("name")          # "Nikita" — None if missing (safe)
user.get("email", "N/A")  # "N/A" — custom default if missing
"name" in user            # True — check key exists
```

### Modify
```python
user["age"] = 26                           # update existing
user["email"] = "n@gmail.com"             # add new key
user.update({"age": 27, "city": "Mumbai"}) # update multiple
del user["city"]                           # delete key
removed = user.pop("age")                 # delete + return value
user.popitem()                            # remove last added pair
user.clear()                              # remove everything
```

### Iterate
```python
for key in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():    # ← use this
    print(f"{key}: {value}")
```

### View Objects
```python
user.keys()     # dict_keys(['id', 'name', 'age'])
user.values()   # dict_values([1, 'Nikita', 25])
user.items()    # dict_items([('id',1), ('name','Nikita'), ...])
```

### Create Smart
```python
# From keys with default value
columns = ["id", "name", "age", "city"]
template = dict.fromkeys(columns, None)
# {'id': None, 'name': None, 'age': None, 'city': None}
```

### Dictionary Comprehension
```python
# {key: value  for item in iterable  if condition}
squares = {x: x**2 for x in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}

# Filter dict — keep only string values, uppercased
string_vals = {k: v.upper() for k, v in user.items() if isinstance(v, str)}
```

### Real Data Analyst Uses
```python
# Mapping technical → friendly labels
status_map = {"1": "Open", "2": "In Progress", "3": "Closed"}
status_map["2"]   # "In Progress"

# Country abbreviations
countries = {"DE": "Germany", "FR": "France", "IN": "India"}

# Config / connection settings
db_config = {
    "host": "localhost",
    "port": 5432,
    "database": "analytics_db",
    "user": "admin"
}

# Aggregate — count occurrences
sales = ["Jan", "Feb", "Jan", "Mar", "Jan", "Feb"]
counts = {}
for month in sales:
    counts[month] = counts.get(month, 0) + 1
# {'Jan': 3, 'Feb': 2, 'Mar': 1}
```

**Challenge:** Given a list of numbers, use list comprehension to return only the even ones. Store name/score pairs in a dict, print them sorted by score.

---

# MODULE 6 — Functions

## Why Functions
- Write once, use many times
- If logic changes, fix in ONE place
- Makes code readable and organized

## Basic Syntax
```python
# Definition
def greet():
    print("Hello!")

# Call
greet()    # nothing happens until you call it
```

## Parameters & Arguments
```python
# Parameters = placeholders in the definition
# Arguments = actual values in the call

def clean_name(name):          # 'name' is a parameter
    return name.strip().lower()

clean_name("  NIKITA  ")       # "  NIKITA  " is the argument
```

## Return Values
```python
def add(a, b):
    return a + b

result = add(3, 5)   # result = 8

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5])  # low=1, high=5
```

## Multiple Parameters
```python
def calculate_discount(price, rate):
    return price * (1 - rate)

# Positional (order matters)
calculate_discount(100, 0.20)

# Keyword (order doesn't matter, safer for 3+ params)
calculate_discount(price=100, rate=0.20)
calculate_discount(rate=0.20, price=100)   # same result
```

## Default Parameters
```python
def greet(name, language="English"):
    if language == "English":
        return f"Hello, {name}!"
    elif language == "Spanish":
        return f"Hola, {name}!"

greet("Nikita")                 # uses default: "Hello, Nikita!"
greet("Nikita", "Spanish")     # "Hola, Nikita!"
```

**Rule:** Parameters with defaults must come AFTER parameters without defaults.

## Variable Arguments
```python
# *args — any number of positional arguments (stored as tuple)
def total(*numbers):
    return sum(numbers)

total(1, 2, 3)       # 6
total(1, 2, 3, 4, 5) # 15

# **kwargs — any number of keyword arguments (stored as dict)
def create_user(**info):
    return info

create_user(name="Nikita", age=25, city="Delhi")
# {'name': 'Nikita', 'age': 25, 'city': 'Delhi'}
```

## Variable Scope
```python
tax_rate = 0.18   # GLOBAL — accessible everywhere

def calculate_tax(price):
    tax = price * tax_rate    # can read global
    total = price + tax       # LOCAL — only exists inside function
    return total

# Can't access 'tax' or 'total' outside the function
```

## Lambda (Anonymous Functions)
```python
# One-line functions — used with map/filter/sort
double = lambda x: x * 2
double(5)   # 10

# With map
prices = [10, 25, 50, 100]
discounted = list(map(lambda p: p * 0.9, prices))

# With filter
expensive = list(filter(lambda p: p > 30, prices))

# With sort (sort list of dicts by value)
employees = [{"name": "Bob", "salary": 60000}, {"name": "Alice", "salary": 75000}]
employees.sort(key=lambda e: e["salary"], reverse=True)
```

## Function Types by Purpose

### 1. Action Functions — Do something, no return needed
```python
def save_to_log(message, filepath="app.log"):
    with open(filepath, "a") as f:
        f.write(message + "\n")

save_to_log("User logged in")
```

### 2. Transformation Functions — Take input, return new shape
```python
def clean_email(email):
    """Clean and validate email format."""
    cleaned = email.strip().lower()
    return cleaned

def parse_date(date_str):
    """Split 'YYYY-MM-DD' into parts."""
    parts = date_str.split("-")
    return {"year": parts[0], "month": parts[1], "day": parts[2]}
```

### 3. Validation Functions — Return True/False
```python
def is_valid_email(email):
    """Check basic email format."""
    return "@" in email and "." in email and len(email) > 5

def is_valid_age(age):
    """Check if age is reasonable."""
    return isinstance(age, int) and 0 <= age <= 120
```

### 4. Orchestrator Functions — Call other functions in order
```python
def process_user_registration(raw_email, raw_age):
    """Full registration pipeline."""
    email = clean_email(raw_email)
    
    if not is_valid_email(email):
        save_to_log(f"Invalid email: {email}")
        return None
    
    if not is_valid_age(raw_age):
        save_to_log(f"Invalid age: {raw_age}")
        return None
    
    user = {"email": email, "age": raw_age}
    save_to_log(f"User registered: {email}")
    return user
```

## Professional Function Standards (Pip 8)
```python
# BAD
def discPrint(P, R):
    print(P - P*R)

# GOOD
def calculate_discount(price: float, rate: float) -> float:
    """Calculate final price after applying a percentage discount.
    
    Args:
        price (float): Original product price
        rate (float): Discount rate as decimal (e.g. 0.20 for 20%)
    
    Returns:
        float: Final discounted price
    """
    return price * (1 - rate)
```

**Rules:**
1. `snake_case` for names — `calculate_discount` not `CalculateDiscount`
2. Name starts with a verb — `get_`, `calculate_`, `is_`, `validate_`
3. Add docstring — at minimum one line
4. Use `return`, not `print` inside functions
5. Don't modify parameters — use local variables
6. Add type hints for 3+ param functions

**Challenge:** Build a BMI calculator function: takes `weight_kg` and `height_m`, returns BMI value and category string (Underweight / Normal / Overweight / Obese).

---

# QUICK REFERENCE CHEAT SHEET

## String Methods
| Method | What it does |
|--------|-------------|
| `.upper()` / `.lower()` | Change case |
| `.strip()` | Remove whitespace both sides |
| `.replace(old, new)` | Replace substring |
| `.split(sep)` | Split into list |
| `.find(x)` | Index of first x (-1 if not found) |
| `.count(x)` | Count occurrences |
| `.startswith(x)` | Bool: starts with x |
| `.endswith(x)` | Bool: ends with x |
| `.isalpha()` | Bool: only letters |
| `.isnumeric()` | Bool: only numbers |

## List Methods
| Method | What it does |
|--------|-------------|
| `.append(x)` | Add to end |
| `.insert(i, x)` | Add at position i |
| `.remove(x)` | Remove first match by value |
| `.pop(i)` | Remove by index (default: last) |
| `.sort()` | Sort in-place |
| `.reverse()` | Flip in-place |
| `.copy()` | Shallow copy |
| `.extend(list)` | Add all items from another list |
| `.index(x)` | Position of first x |
| `.count(x)` | Count occurrences |

## Dict Methods
| Method | What it does |
|--------|-------------|
| `.get(key, default)` | Safe access |
| `.update({...})` | Update multiple keys |
| `.pop(key)` | Remove + return |
| `.keys()` | All keys |
| `.values()` | All values |
| `.items()` | All key-value pairs |

---

# PROGRESS TRACKER

| Module | Status | Challenge Done? |
|--------|--------|----------------|
| 1 — Fundamentals | ⬜ | ⬜ |
| 2 — Strings | ⬜ | ⬜ |
| 3 — Numbers | ⬜ | ⬜ |
| 4 — Control Flow | ⬜ | ⬜ |
| 5 — Data Structures | ⬜ | ⬜ |
| 6 — Functions | ⬜ | ⬜ |

---

*Tip: Don't read this like a book. Read a section → open profile.py → write the examples yourself → do the challenge. Then move on.*
