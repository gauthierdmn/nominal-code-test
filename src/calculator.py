import os

def add(first: int, second: int) -> int:
    """
    Add two integers.

    Args:
        first (int): First operand.
        second (int): Second operand.

    Returns:
        int: Sum of first and second.
    """

    return first + second


def subtract(first: int, second: int) -> int:
    """
    Subtract second from first.

    Args:
        first (int): First operand.
        second (int): Second operand.

    Returns:
        int: Difference of first and second.
    """

    return first - second


def multiply(first: int, second: int) -> int:
    """
    Multiply two integers.

    Args:
        first (int): First operand.
        second (int): Second operand.

    Returns:
        int: Product of first and second.
    """

    return first * second


def divide(first: int, second: int):
    """
    Divide first by second.

    Args:
        first (int): Numerator.
        second (int): Denominator.

    Returns:
        float: Result of division.
    """

    return first / second
