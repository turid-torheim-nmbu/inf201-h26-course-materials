"""
Illustrate how to test that code raises a specific exception.
"""

import pytest


def inv(x: int | float) -> int | float:
    """Return the mathematical inverse of x, i.e., a values such that x * inv(x) == 1."""

    if x == 0:
        raise ValueError

    return 1 / x


def test_inv_raises() -> None:
    with pytest.raises(ValueError):
        inv(0)
