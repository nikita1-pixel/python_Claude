# Cheat sheet — basics (Phases 0–1)

Quick paste-ready reference. Grows as you learn.

## Run things
```bash
python3 --version      # check Python is installed
python3                # open the REPL (exit() to leave)
python3 hello.py       # run a script
```

## Print & comment
```python
print("Hello")         # show text
print(a, b)            # multiple values, space-separated
# this is a comment    # ignored by Python
```

## Variables & types
```python
name = "Sam"      # str
age = 21          # int
height = 5.9      # float
is_ready = True   # bool
type(age)         # -> <class 'int'>
```

## Strings
```python
f"Hi {name}, age {age}"   # f-string (the workhorse)
name.upper()              # SAM
name.lower()
len(name)                 # length
name + " " + "C"          # join with +
```

## Numbers
```python
+  -  *            # add, subtract, multiply
/                  # divide -> always float
//                 # floor divide -> drops the decimal
%                  # modulo -> remainder (even check: n % 2 == 0)
**                 # power
```

## Input (always a string!)
```python
x = input("Age? ")   # x is "21" (text)
x = int(x)           # convert before doing math
int("21")  str(21)  float("3.5")   # conversions
```

## The #1 beginner gotcha
`input()` returns text. `input() + 1` crashes. Convert first: `int(input(...)) + 1`.
