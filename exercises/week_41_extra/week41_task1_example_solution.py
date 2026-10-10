# Example solution for task 1 of the week 41 exercises
# Turid Torheim, NMBU

from collections.abc import Iterable
from typing import Any


def flatten_list(nested_list: list[Any]) -> list[Any]:
    """Recursively flattens a nested list structure.

    Args:
        nested_list: A (potentially) nested list.

    Returns:
        A single flat list containing all scalar elements in sequence.
    """
    flat = []
    for item in nested_list:
        if isinstance(item, Iterable) and not isinstance(
            item, (str, bytes, bytearray)
        ):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


# Some test cases
assert flatten_list([1, [2, [3, 4], 5], 6, [[7]]]) == [1, 2, 3, 4, 5, 6, 7]
print("1st: OK!")
assert flatten_list(["hello", ["world", ["python"]]]) == ["hello", "world", "python"]
print("2nd: OK!")
assert flatten_list([[], [[]], [[[[1]]]]]) == [1]
print("3rd: OK!")
assert flatten_list([]) == []
print("4th: OK!")
