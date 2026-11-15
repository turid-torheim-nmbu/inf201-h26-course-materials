"""
A simple example of PyTest tests for a "square" function.

Usually, the function to be tested would be in a separate file from the tests.
"""

import pytest


def square(x: int | float) -> int | float:
    """
    Return the square of x.

    Note: This function is intentionally buggy.
    """
    return x * x


@pytest.mark.parametrize("x, expected",
                         [[1, 1],
                          [2, 4]
                          ])
def test_square(x: int | float, expected: int | float) -> int | float:
    assert square(x) == expected
