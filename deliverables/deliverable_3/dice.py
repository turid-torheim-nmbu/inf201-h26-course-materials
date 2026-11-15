"""Dice rolling module for RPG simulator."""

import random


class Dice:
    """Represents an n-sided dice."""

    def __init__(self, sides: int = 6) -> None:
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")
        self.sides = sides

    def roll(self) -> int:
        """Simulates rolling the dice."""
        return random.randint(1, self.sides)

    def __call__(self) -> int:
        """Allows calling the dice instance directly like a function (e.g., d6())."""
        return self.roll()

    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"
