from collections.abc import Callable


def make_multiplier(factor: float) -> Callable[[float], float]:
    """Create a function that multiplies its input by a fixed factor.

    Args:
        factor: The constant value used to scale inputs.

    Returns:
        A function that takes a number ``n`` and returns ``factor * n``.

    Example:
        >>> double = make_multiplier(2)
        >>> double(5)
        10
    Note: You can test this example using pytest:
    python -m pytest -v --doctest-modules multiplier_complete.py
    """
    def multiplier(n: float) -> float:
        return factor * n

    return multiplier
