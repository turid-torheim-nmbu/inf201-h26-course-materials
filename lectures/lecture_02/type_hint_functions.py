# Some examples to show what type hints do (and don't do) in Python.
# Turid Torheim, NMBU


def add_no_hints(x, y):
    """Add two numbers together."""
    return x + y


def add_with_hints(x: int | float, y: int | float) -> int | float:
    """Add two numbers together."""
    return x + y


print(add_no_hints(1, 2))  # Output: 3
print(add_no_hints(1.5, 2.5))  # Output: 4.0
print(add_no_hints("hello", " world"))  # Output: "hello world"

print(add_with_hints(1, 2))
print(add_with_hints(1.5, 2.5))
print(add_with_hints("hello", " world"))
