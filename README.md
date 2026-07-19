# Calculator

A tiny calculator library. It exists to be watched by
[DocSentry](https://github.com/mannas632006/DocSentry-_-Keepin-It-Real): every function below is
documented with a **specific, checkable claim**, so changing the code makes this file measurably
false.

## add

`add(a, b)` returns the sum of two numbers.

```python
add(2, 3)      # -> 5
```

## subtract

`subtract(a, b)` returns `a` minus `b`.

```python
subtract(5, 3)   # -> 2
```

## divide

`divide(a, b, safe=True)` divides `a` by `b`.

By default `safe` is **True**, so dividing by zero returns `None` rather than raising a
`ZeroDivisionError`. Pass `safe=False` if you want the raw exception instead.

```python
# this comment must not be parsed as a markdown heading
divide(10, 2)              # -> 5.0
divide(1, 0)               # -> None       (safe defaults to True)
divide(1, 0, safe=False)   # -> raises ZeroDivisionError
```

## round_to

`round_to(value, places=8)` rounds `value` to the given number of decimal places.

Defaults to **8** places.

```python
round_to(3.14159)      # -> 3.14159
round_to(3.14159, 4)   # -> 3.1416
```

## Notes

Nothing else to say here. This section mentions no function, so DocSentry should never link a code
change to it.
