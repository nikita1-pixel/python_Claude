# Python Glossary — Full Universe Map

> **Color key**
> 🟢 = **Learned + practiced** — you have used this in a real terminal session
> 🔵 = **Python universe** — exists, coming up in a future phase
> 🟢* = was 🔵, now learned — update the emoji + add * when it clicks

**Back to:** [[Home]]

---

## SECTION 1 — Phase 1 Learned Terms 🟢
*These are the terms you have actually run in a terminal. Full definition + example here.*

---

> [!success]+ 🟢 REPL (Read-Eval-Print Loop)
> **What it is:** The live Python interpreter you open by typing `python` in the terminal. Type one line → Python reads it, evaluates it, prints the result, loops back.
> **How to spot it:** Prompt changes to `>>>`
> **How to open:** type `python` in terminal. **How to exit:** `exit()`
> ```python
> >>> 2 + 2
> 4
> >>> "hello"
> 'hello'
> ```
> **Don't confuse with:** PowerShell prompt `PS C:\>` — that's Windows, not Python.

---

> [!success]+ 🟢 Script (.py file)
> **What it is:** A saved file of Python code you run with `python filename.py`. Unlike the REPL, it runs all lines top to bottom in one go.
> **When to use:** Any real program you want to save and repeat.
> ```bash
> python basics_practice.py
> ```

---

> [!success]+ 🟢 Variable
> **What it is:** A named box that holds a value. You create one with `=` (assignment).
> Python reads the right side first, computes it, then stores it under the name on the left.
> ```python
> name = "Nikita"   # the box is called "name", it holds "Nikita"
> age  = 22
> ```
> **Naming rules:** lowercase + underscores (`user_name`), no spaces, no starting with a number.

---

> [!success]+ 🟢 str (string)
> **What it is:** The Python type for text. Always wrapped in quotes (single or double — same thing).
> ```python
> name = "Nikita"
> city = 'Bangalore'
> empty = ""          # empty string is valid
> ```
> **Key operations:** `len()`, `+` (join), `[0]` (first char), `.upper()`, `.lower()`, f-string embedding.

---

> [!success]+ 🟢 int (integer)
> **What it is:** The Python type for whole numbers — no decimal point.
> ```python
> age   = 22
> score = -5
> big   = 1_000_000   # underscores = readable commas, no effect on value
> ```
> **Key operations:** all math operators. Convert from str: `int("22")`.

---

> [!success]+ 🟢 float
> **What it is:** The Python type for decimal numbers.
> ```python
> height = 5.6
> pi     = 3.14159
> ```
> **Gotcha:** regular division `/` always returns a float, even `10 / 2` → `5.0`.

---

> [!success]+ 🟢 bool (boolean)
> **What it is:** The Python type with exactly two values: `True` or `False` (capital first letter — always).
> ```python
> is_student = True
> is_working = False
> ```
> **Under the hood:** `True == 1`, `False == 0`. Comparison operators return bools.

---

> [!success]+ 🟢 type()
> **What it is:** A built-in function that tells you the type of any value.
> ```python
> type("hello")   # <class 'str'>
> type(42)        # <class 'int'>
> type(3.14)      # <class 'float'>
> type(True)      # <class 'bool'>
> ```
> **Pattern:** `type(anything)` → tells you what kind of thing it is.

---

> [!success]+ 🟢 print()
> **What it is:** The built-in function that displays output on screen.
> ```python
> print("Hello")                    # single value
> print("Name:", name, "Age:", age) # multiple args, space-separated
> print(1, 2, 3, sep="-")          # custom separator → 1-2-3
> print("loading", end="...")       # no newline at end
> print()                           # blank line
> ```

---

> [!success]+ 🟢 len()
> **What it is:** Built-in function that counts items — characters in a string, items in a list.
> ```python
> len("Nikita")    # 6
> len("hello")     # 5
> len([1, 2, 3])   # 3  (lists — Phase 3)
> ```
> **Gotcha:** doesn't work on int or float — `len(42)` → TypeError.

---

> [!success]+ 🟢 input()
> **What it is:** Built-in function that pauses the program and waits for the user to type something. **Always returns a string — even if the user types a number.**
> ```python
> name = input("What's your name? ")   # returns str
> age  = int(input("How old? "))        # convert immediately if you need math
> ```
> **Critical gotcha:** `input()` → `str`. Always. Wrap with `int()` or `float()` if you need a number.

---

> [!success]+ 🟢 int() / float() / str() — type conversion
> **What it is:** Built-in functions that convert a value from one type to another.
> ```python
> int("22")       # "22" → 22     (str to int)
> float("3.14")   # "3.14" → 3.14 (str to float)
> str(99)         # 99 → "99"     (int to str — always works)
> int("hello")    # ValueError! — can't convert non-numeric string
> int(3.9)        # 3 — truncates, does NOT round
> ```

---

> [!success]+ 🟢 f-string (formatted string literal)
> **What it is:** The modern, clean way to embed variables inside text. Put `f` before the opening quote, variables go in `{ }`.
> ```python
> name = "Nikita"
> age  = 22
> print(f"Hello {name}, you are {age}")    # Hello Nikita, you are 22
> print(f"In 10 years: {age + 10}")        # expressions work inside {}
> print(f"Length: {len(name)}")             # function calls work too
> ```
> **Don't use:** the old `"Hello " + name + "!"` — messy and causes TypeError with non-strings.

---

> [!success]+ 🟢 Math operators
> **What they are:** Symbols that perform arithmetic on numbers.
> ```python
> 10 + 3    # 13   addition
> 10 - 3    # 7    subtraction
> 10 * 3    # 30   multiplication
> 10 / 3    # 3.333... always float
> 10 // 3   # 3    floor division — drops decimal
> 10 % 3    # 1    modulo — remainder after dividing
> 10 ** 3   # 1000 exponentiation
> ```
> **Trick:** `x % 2 == 0` means x is even. Used constantly.

---

> [!success]+ 🟢 Comment (#)
> **What it is:** Text that Python ignores completely. For humans reading the code.
> ```python
> # This whole line is ignored
> x = 5   # inline comment — fine for short notes
> ```
> **Rule:** comment the WHY, not the WHAT. "add 1 to compensate for 0-indexing" ✅. "add 1 to x" ✗.

---

> [!success]+ 🟢 Assignment (=)
> **What it is:** The operator that stores a value into a variable. NOT the same as equals-check (that's `==`).
> ```python
> name = "Nikita"   # assignment: store "Nikita" in name
> name == "Nikita"  # comparison: is name equal to "Nikita"? → True
> ```

---

> [!success]+ 🟢 PowerShell vs Python REPL
> **What it is:** Two completely different programs on Windows.
> ```
> PS C:\Users\nikita>    ← PowerShell (Windows shell). type() here = reads a file.
> >>>                    ← Python REPL. type() here = returns the type of a value.
> ```
> **To get to Python:** type `python` in PowerShell. Wait for `>>>`.

---

## SECTION 2 — Python Universe 🔵
*Every term you'll eventually encounter. Blue now → green when learned.*
*Update: change 🔵 to 🟢* when you first use it in a real session.*

---

### Fundamentals

| Status | Term | One-liner |
|---|---|---|
| 🔵 | statement | A complete instruction Python executes (one line = one statement usually) |
| 🔵 | expression | Code that produces a value — `2 + 2`, `len("hi")`, `True` |
| 🔵 | keyword | Reserved word Python owns — `if`, `for`, `def`, `class` — can't use as variable names |
| 🔵 | identifier | The name you give to a variable, function, or class |
| 🔵 | literal | A hardcoded value in code — `42`, `"hello"`, `True`, `3.14` |
| 🔵 | syntax | The grammar rules of Python — what's legal vs what causes a SyntaxError |
| 🔵 | indentation | The spaces/tabs at the start of a line — Python uses these to define blocks (not braces) |
| 🔵 | block | A group of lines at the same indentation level, belonging to one `if`/`for`/`def` etc. |
| 🔵 | namespace | A container that maps names to objects — keeps variables from colliding |

---

### Data Types

| Status | Term | One-liner |
|---|---|---|
| 🟢 | str | Text type — `"hello"` |
| 🟢 | int | Whole number type — `42` |
| 🟢 | float | Decimal number type — `3.14` |
| 🟢 | bool | True/False type |
| 🔵 | NoneType | The type of `None` — Python's "nothing here" value |
| 🔵 | None | The absence of a value — like null in other languages |
| 🔵 | complex | Complex numbers — `3+4j` — used in scientific computing |
| 🔵 | bytes | Immutable sequence of raw bytes — used for binary data, files |
| 🔵 | bytearray | Mutable version of bytes |

---

### Operators

| Status | Term | One-liner |
|---|---|---|
| 🟢 | `+` `-` `*` `/` | Basic arithmetic |
| 🟢 | `//` | Floor division — drops decimal |
| 🟢 | `%` | Modulo — remainder |
| 🟢 | `**` | Exponentiation |
| 🟢 | `=` | Assignment — store a value |
| 🔵 | `+=` `-=` `*=` `/=` | Augmented assignment — `x += 1` means `x = x + 1` |
| 🔵 | `==` `!=` | Equality / inequality — returns bool |
| 🔵 | `<` `>` `<=` `>=` | Comparison — returns bool |
| 🔵 | `and` `or` `not` | Logical operators |
| 🔵 | `in` `not in` | Membership — `"a" in "cat"` → True |
| 🔵 | `is` `is not` | Identity — checks if two variables point to the SAME object |
| 🔵 | `:=` | Walrus operator — assign AND use in one expression (Python 3.8+) |

---

### Control Flow

| Status | Term | One-liner |
|---|---|---|
| 🔵 | `if` | Run a block only if a condition is True |
| 🔵 | `elif` | "else if" — check another condition if the first was False |
| 🔵 | `else` | Run a block if all previous conditions were False |
| 🔵 | `while` | Loop — keep running as long as a condition is True |
| 🔵 | `for` | Loop — run once for each item in a sequence |
| 🔵 | `range()` | Generate a sequence of numbers — `range(5)` → 0,1,2,3,4 |
| 🔵 | `break` | Exit a loop immediately |
| 🔵 | `continue` | Skip the rest of this iteration, go to the next |
| 🔵 | `pass` | Do nothing — placeholder for empty blocks |
| 🔵 | `match` / `case` | Pattern matching — Python's switch statement (3.10+) |

---

### Functions

| Status | Term | One-liner |
|---|---|---|
| 🔵 | `def` | Keyword to define a function |
| 🔵 | function | A reusable block of code with a name — call it anywhere |
| 🔵 | parameter | The variable name in the function definition — `def greet(name):` |
| 🔵 | argument | The actual value you pass when calling — `greet("Nikita")` |
| 🔵 | `return` | Send a value back to the caller — function ends here |
| 🔵 | default argument | Parameter with a fallback value — `def greet(name="friend"):` |
| 🔵 | keyword argument | Passing args by name — `greet(name="Nikita")` |
| 🔵 | `*args` | Accept any number of positional arguments as a tuple |
| 🔵 | `**kwargs` | Accept any number of keyword arguments as a dict |
| 🔵 | `lambda` | Anonymous one-line function — `lambda x: x + 1` |
| 🔵 | docstring | String at the top of a function explaining what it does |
| 🔵 | scope | Where a variable is visible — local (inside function) vs global |
| 🔵 | `global` | Declare a variable as global inside a function |
| 🔵 | `nonlocal` | Access a variable from an enclosing (not global) scope |
| 🔵 | closure | A function that remembers variables from its enclosing scope |
| 🔵 | decorator | A function that wraps another function — `@my_decorator` |
| 🔵 | recursion | A function that calls itself — must have a base case to stop |
| 🔵 | `enumerate()` | Loop with both index and value — `for i, v in enumerate(list)` |
| 🔵 | `zip()` | Loop two sequences together in parallel |
| 🔵 | `map()` | Apply a function to every item in a sequence |
| 🔵 | `filter()` | Keep only items where function returns True |

---

### Data Structures

| Status | Term | One-liner |
|---|---|---|
| 🔵 | list | Ordered, mutable collection — `[1, 2, 3]` |
| 🔵 | tuple | Ordered, immutable collection — `(1, 2, 3)` — can't change after creation |
| 🔵 | set | Unordered collection of unique items — `{1, 2, 3}` — no duplicates |
| 🔵 | frozenset | Immutable version of set |
| 🔵 | dict (dictionary) | Key-value pairs — `{"name": "Nikita", "age": 22}` |
| 🔵 | key | The lookup label in a dict — `"name"` in the example above |
| 🔵 | value | What the key maps to — `"Nikita"` |
| 🔵 | index | Position in a sequence — `list[0]` is the first item |
| 🔵 | slice | Extract a sub-sequence — `list[1:4]` |
| 🔵 | list comprehension | One-line list builder — `[x*2 for x in range(5)]` |
| 🔵 | dict comprehension | One-line dict builder — `{k: v for k, v in pairs}` |
| 🔵 | set comprehension | One-line set builder — `{x for x in items}` |
| 🔵 | nested | A data structure inside another — list of lists, dict of dicts |
| 🔵 | mutable | Can be changed after creation — list, dict, set |
| 🔵 | immutable | Cannot be changed after creation — str, int, tuple |
| 🔵 | iterable | Anything you can loop over — str, list, tuple, dict, range |
| 🔵 | iterator | Object that produces the next value on demand |

---

### String Methods

| Status | Term | One-liner |
|---|---|---|
| 🔵 | `.upper()` | `"hello".upper()` → `"HELLO"` |
| 🔵 | `.lower()` | `"HELLO".lower()` → `"hello"` |
| 🔵 | `.strip()` | Remove whitespace from both ends |
| 🔵 | `.split()` | Split string into list — `"a,b,c".split(",")` → `["a","b","c"]` |
| 🔵 | `.join()` | Join list into string — `"-".join(["a","b"])` → `"a-b"` |
| 🔵 | `.replace()` | `"hello".replace("l","r")` → `"herro"` |
| 🔵 | `.find()` | Index of first match, -1 if not found |
| 🔵 | `.count()` | How many times substring appears |
| 🔵 | `.startswith()` | Returns bool — does string start with this? |
| 🔵 | `.endswith()` | Returns bool — does string end with this? |
| 🔵 | `.isdigit()` | Is every character a digit? |
| 🔵 | `.isalpha()` | Is every character a letter? |
| 🔵 | `.title()` | `"hello world".title()` → `"Hello World"` |
| 🔵 | `.format()` | Old-style string formatting — use f-strings instead |

---

### List Methods

| Status | Term | One-liner |
|---|---|---|
| 🔵 | `.append()` | Add one item to the end |
| 🔵 | `.extend()` | Add all items from another list to the end |
| 🔵 | `.insert()` | Insert at a specific index |
| 🔵 | `.remove()` | Remove first occurrence of a value |
| 🔵 | `.pop()` | Remove and return item at index (default: last) |
| 🔵 | `.sort()` | Sort in place |
| 🔵 | `.reverse()` | Reverse in place |
| 🔵 | `.index()` | Find index of first occurrence |
| 🔵 | `.copy()` | Shallow copy of the list |
| 🔵 | `.clear()` | Remove all items |
| 🔵 | `sorted()` | Return a new sorted list (built-in, works on any iterable) |
| 🔵 | `reversed()` | Return a reversed iterator |

---

### Dict Methods

| Status | Term | One-liner |
|---|---|---|
| 🔵 | `.keys()` | All keys as a view |
| 🔵 | `.values()` | All values as a view |
| 🔵 | `.items()` | All key-value pairs as tuples |
| 🔵 | `.get()` | Safe lookup — returns None (not error) if key missing |
| 🔵 | `.update()` | Merge another dict in |
| 🔵 | `.pop()` | Remove a key and return its value |
| 🔵 | `.setdefault()` | Return value if key exists, else set it to a default |

---

### More Built-in Functions

| Status | Term | One-liner |
|---|---|---|
| 🟢 | `print()` | Show output |
| 🟢 | `input()` | Get user input (always str) |
| 🟢 | `type()` | What type is this? |
| 🟢 | `len()` | Count items |
| 🟢 | `int()` | Convert to integer |
| 🟢 | `float()` | Convert to float |
| 🟢 | `str()` | Convert to string |
| 🔵 | `bool()` | Convert to boolean |
| 🔵 | `range()` | Generate number sequence |
| 🔵 | `list()` | Convert to list |
| 🔵 | `tuple()` | Convert to tuple |
| 🔵 | `dict()` | Create a dict |
| 🔵 | `set()` | Create a set |
| 🔵 | `sum()` | Add up all numbers in an iterable |
| 🔵 | `max()` | Largest item |
| 🔵 | `min()` | Smallest item |
| 🔵 | `abs()` | Absolute value — `abs(-5)` → `5` |
| 🔵 | `round()` | Round a float — `round(3.14159, 2)` → `3.14` |
| 🔵 | `open()` | Open a file |
| 🔵 | `isinstance()` | Is this value an instance of a type? — `isinstance(x, int)` |
| 🔵 | `id()` | Unique identity number of an object in memory |
| 🔵 | `dir()` | List all attributes/methods of an object |
| 🔵 | `help()` | Show documentation for anything |
| 🔵 | `any()` | True if at least one item in iterable is True |
| 🔵 | `all()` | True if every item in iterable is True |
| 🔵 | `callable()` | Is this object a function? |
| 🔵 | `iter()` | Get an iterator from an iterable |
| 🔵 | `next()` | Get the next value from an iterator |
| 🔵 | `vars()` | Return `__dict__` of an object |
| 🔵 | `hasattr()` | Does this object have this attribute? |
| 🔵 | `getattr()` | Get an attribute by name string |
| 🔵 | `setattr()` | Set an attribute by name string |

---

### File Handling

| Status | Term | One-liner |
|---|---|---|
| 🔵 | `open()` | Open a file — `open("file.txt", "r")` |
| 🔵 | file mode `r` | Read mode |
| 🔵 | file mode `w` | Write mode — overwrites |
| 🔵 | file mode `a` | Append mode — adds to end |
| 🔵 | file mode `rb`/`wb` | Binary read/write — for images, zip files etc. |
| 🔵 | `.read()` | Read entire file as string |
| 🔵 | `.readline()` | Read one line |
| 🔵 | `.readlines()` | Read all lines into a list |
| 🔵 | `.write()` | Write a string to file |
| 🔵 | `.close()` | Close the file handle |
| 🔵 | `with` statement | Context manager — auto-closes the file for you |

---

### Error Handling

| Status | Term | One-liner |
|---|---|---|
| 🔵 | `try` | Attempt code that might fail |
| 🔵 | `except` | Catch a specific error and handle it |
| 🔵 | `finally` | Always runs — cleanup code |
| 🔵 | `raise` | Deliberately throw an error |
| 🔵 | `Exception` | Base class for all errors |
| 🔵 | `ValueError` | Right type, wrong value — `int("hello")` |
| 🔵 | `TypeError` | Wrong type — `"age: " + 22` |
| 🔵 | `IndexError` | List index out of range |
| 🔵 | `KeyError` | Dict key doesn't exist |
| 🔵 | `AttributeError` | Object doesn't have that attribute/method |
| 🔵 | `NameError` | Variable used before being defined |
| 🔵 | `ZeroDivisionError` | Dividing by zero |
| 🔵 | `FileNotFoundError` | File path doesn't exist |
| 🔵 | `StopIteration` | Iterator has no more items |
| 🔵 | `SyntaxError` | Code breaks Python's grammar rules |
| 🔵 | custom exception | A class that extends Exception — for your own error types |

---

### OOP (Object-Oriented Programming)

| Status | Term | One-liner |
|---|---|---|
| 🔵 | `class` | Blueprint for creating objects |
| 🔵 | object | An instance of a class — a specific "thing" built from the blueprint |
| 🔵 | instance | Same as object |
| 🔵 | `__init__` | Constructor — runs when a new object is created |
| 🔵 | `self` | Reference to the current instance inside a method |
| 🔵 | method | A function that belongs to a class |
| 🔵 | attribute | A variable that belongs to an object — `self.name` |
| 🔵 | inheritance | A class that gets all the features of another class |
| 🔵 | `super()` | Call the parent class's method |
| 🔵 | encapsulation | Bundling data + methods together, hiding internals |
| 🔵 | polymorphism | Same method name, different behaviour in different classes |
| 🔵 | abstraction | Hiding complexity, exposing only what's needed |
| 🔵 | `@property` | Make a method look like an attribute |
| 🔵 | `@classmethod` | Method that takes the class, not an instance, as first arg |
| 🔵 | `@staticmethod` | Method with no access to class or instance |
| 🔵 | `__str__` | What `print(obj)` shows |
| 🔵 | `__repr__` | Official string representation — for debugging |
| 🔵 | `__len__` | Makes `len(obj)` work on your class |
| 🔵 | `__eq__` | Makes `obj1 == obj2` work |
| 🔵 | dunder / magic methods | Methods with `__double_underscores__` — Python's hook system |
| 🔵 | MRO (Method Resolution Order) | The order Python searches classes for a method in inheritance |
| 🔵 | dataclass | Decorator that auto-generates `__init__`, `__repr__` etc. |

---

### Modules & Packages

| Status | Term | One-liner |
|---|---|---|
| 🔵 | module | A `.py` file you import — `import math` |
| 🔵 | package | A folder of modules with `__init__.py` |
| 🔵 | `import` | Load a module — `import os` |
| 🔵 | `from ... import` | Import specific names — `from math import pi` |
| 🔵 | `as` (alias) | Rename on import — `import numpy as np` |
| 🔵 | `__name__` | A module's own name — `"__main__"` when run directly |
| 🔵 | `__main__` | The guard for "only run this if directly executed" |
| 🔵 | stdlib | Python's standard library — batteries included, no install needed |
| 🔵 | pip | Package installer — `pip install pandas` |
| 🔵 | venv | Virtual environment — isolated Python for each project |
| 🔵 | `requirements.txt` | List of packages a project needs — `pip freeze > requirements.txt` |
| 🔵 | third-party | Packages not in stdlib — installed via pip |

---

### Standard Library Highlights

| Status | Module | What it does |
|---|---|---|
| 🔵 | `os` | File system — paths, dirs, env vars |
| 🔵 | `sys` | Python runtime — `sys.argv`, `sys.exit()` |
| 🔵 | `math` | Math functions — `math.sqrt()`, `math.pi` |
| 🔵 | `random` | Random numbers — `random.randint()`, `random.choice()` |
| 🔵 | `datetime` | Dates and times |
| 🔵 | `time` | Timing — `time.sleep()` |
| 🔵 | `json` | Read/write JSON — `json.loads()`, `json.dumps()` |
| 🔵 | `csv` | Read/write CSV files |
| 🔵 | `re` | Regular expressions — pattern matching in strings |
| 🔵 | `pathlib` | Modern file paths — `Path("folder/file.txt")` |
| 🔵 | `collections` | Extra data structures — `Counter`, `defaultdict`, `deque` |
| 🔵 | `itertools` | Tools for iterating — `chain`, `product`, `combinations` |
| 🔵 | `functools` | Functional tools — `reduce`, `lru_cache`, `partial` |
| 🔵 | `copy` | `copy.deepcopy()` — proper copy of nested structures |
| 🔵 | `logging` | Proper logging — better than print() for real apps |
| 🔵 | `unittest` | Built-in testing framework |
| 🔵 | `argparse` | Parse command-line arguments |
| 🔵 | `subprocess` | Run shell commands from Python |
| 🔵 | `threading` | Run things concurrently |
| 🔵 | `io` | In-memory file-like objects |

---

### Advanced Python

| Status | Term | One-liner |
|---|---|---|
| 🔵 | generator | Function that yields values one at a time — memory-efficient |
| 🔵 | `yield` | Pause a generator function and return a value |
| 🔵 | context manager | Handles setup/teardown — the thing `with` uses |
| 🔵 | `async` / `await` | Asynchronous code — do multiple things "at once" |
| 🔵 | coroutine | An async function |
| 🔵 | `asyncio` | The stdlib for async programming |
| 🔵 | type hints | Optional type annotations — `def greet(name: str) -> str:` |
| 🔵 | `namedtuple` | Tuple with named fields — like a tiny class |
| 🔵 | `enum` | Enumeration — a fixed set of named constants |
| 🔵 | `@dataclass` | Auto-generates boilerplate for data-holding classes |

---

### Popular Third-Party Packages

| Status | Package | What it does |
|---|---|---|
| 🔵 | `pandas` | DataFrames — the Excel of Python (Phase 7) |
| 🔵 | `numpy` | Fast arrays and math — foundation of data science |
| 🔵 | `matplotlib` | Plotting and charts |
| 🔵 | `seaborn` | Beautiful statistical charts on top of matplotlib |
| 🔵 | `requests` | HTTP requests — call any web API in 3 lines |
| 🔵 | `beautifulsoup4` | Web scraping — parse HTML |
| 🔵 | `flask` | Lightweight web framework |
| 🔵 | `fastapi` | Modern, fast API framework |
| 🔵 | `django` | Full-stack web framework |
| 🔵 | `sqlalchemy` | Databases in Python |
| 🔵 | `pytest` | Testing framework — better than unittest |
| 🔵 | `pydantic` | Data validation and settings |
| 🔵 | `streamlit` | Turn Python scripts into web apps (Phase 9 candidate) |
| 🔵 | `selenium` | Browser automation |
| 🔵 | `pillow` | Image processing |
| 🔵 | `scikit-learn` | Machine learning |
| 🔵 | `tensorflow` / `pytorch` | Deep learning |

---

## Update Log
*When a 🔵 term becomes 🟢, log it here so progress is visible.*

| Date | Term | Session |
|---|---|---|
| 2026-06-04 | REPL, variable, str, int, float, bool, type(), print(), len(), input(), int()/float()/str(), f-string, math operators, comment, assignment, PowerShell vs Python | Session 1 — Phase 1 |
