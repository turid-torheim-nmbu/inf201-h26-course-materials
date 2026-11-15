"""
A simple example of PyTest tests for a "square" function.

Usually, the function to be tested would be in a separate file from the tests.
"""


def square(x: int | float) -> int | float:
    """
    Return the square of x.

    Note: This function is intentionally buggy.
    """
    return x * x * x


def test_square_1() -> None:
    assert square(1) == 1


def test_square_2() -> None:
    assert square(2) == 4
