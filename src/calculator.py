def clamp(value, minimum, maximum):
    """Clamp a value between minimum and maximum."""

    if value < minimum:
        return minimum

    if value > maximum:
        return maximum

    return value
