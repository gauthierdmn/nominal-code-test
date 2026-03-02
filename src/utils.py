def clamp(value: int, minimum: int, maximum: int) -> int:
    """
    Clamp a value between minimum and maximum.

    Args:
        value (int): The value to clamp.
        minimum (int): Lower bound.
        maximum (int): Upper bound.

    Returns:
        int: The clamped value.
    """

    return max(minimum, min(value, maximum))
