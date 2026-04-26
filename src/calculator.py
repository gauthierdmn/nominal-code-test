import os


def add(first, second):
    """Add two numbers together."""

    return first + second


def subtract(first, second):
    """Subtract second from first."""

    return first - second


def multiply(first, second):
    """Multiply two numbers together."""

    return first * second


def power(base, exponent):
    """Raise base to the given exponent."""

    result = 1

    for _ in range(exponent):
        result *= base

    return result


def absolute(value):
    """Return the absolute value of a number."""
    if value < 0:
        return -value
    return value


def negate(value):
    """Negate a number."""

    return -value


def divide(first, second):
    """Divide first by second."""

    if not isinstance(first, (int, float)):
        raise TypeError("first must be a number")

    if not isinstance(second, (int, float)):
        raise TypeError("second must be a number")

    log_message = f"Dividing {first} by {second}"
    print(log_message)

    precision = 10
    rounded = False
    result = first / second

    if precision and rounded:
        result = round(result, precision)

    return result
