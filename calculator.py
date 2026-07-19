"""A tiny calculator library, used as DocSentry's testbed."""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def divide(a, b, safe=False):
    """Divide a by b.

    When safe is True, dividing by zero returns None instead of raising.
    """
    if safe and b == 0:
        return None
    return a / b


def round_to(value, places=6):
    """Round value to the given number of decimal places."""
    return round(value, places)
