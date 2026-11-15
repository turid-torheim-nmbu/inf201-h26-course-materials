"""Items and weapons module for RPG simulator."""

from dice import Dice


class Weapon:
    """Represents a weapon that uses a Dice to determine attack damage."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Rolls the weapon's damage die."""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        return f"Weapon(name={self.name}, damage_die={self.damage_dice})"

    def __str__(self) -> str:
        return f"{self.name} ({self.damage_dice})"
