"""characters.py - All character types for the RPG simulator.

Contains the base Character class alongside specialized subclasses (Warrior, Mage).
All combat actions return lists of log strings.
"""

from items import Weapon


class Character:
    """Represents a base character in the RPG."""

    DEFAULT_HP_MAX: int = 100
    DEFAULT_DAMAGE: int = 10

    # --- Constructor ---
    def __init__(
        self,
        name: str,
        hp_max: int = DEFAULT_HP_MAX,
        damage: int = DEFAULT_DAMAGE,
        weapon: Weapon | None = None,
    ) -> None:
        if hp_max <= 0:
            raise ValueError("Max HP must be greater than 0.")
        if damage <= 0:
            raise ValueError("Damage must be greater than 0")

        self.name = name
        self.hp_max = hp_max
        self._hp = hp_max  # Protected attribute
        self.damage = damage
        self.weapon = weapon

    # --- Properties ---
    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Returns True if the character's HP is greater than 0."""
        return self._hp > 0

    # --- Representation Methods ---
    def __repr__(self) -> str:
        return f"Character(name={self.name}, hp={self.hp}, damage={self.damage}, weapon={self.weapon})"

    def __str__(self) -> str:
        weapon_str = f" equipped with {self.weapon.name}" if self.weapon else ""
        return f"Character: {self.name} with {self.hp}/{self.hp_max} HP{weapon_str}"

    # --- Public Methods ---
    def take_damage(self, amount: int) -> list[str]:
        """Reduces character HP by amount and returns a list of combat event messages."""
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")

        self._hp = max(self._hp - amount, 0)
        return [
            f"{self.name} took {amount} damage! ({self._hp}/{self.hp_max} HP remaining)"
        ]

    def heal(self, amount: int) -> list[str]:
        """Restores HP by amount and returns a list of combat event messages."""
        if not self.is_alive:
            return [f"{self.name} is defeated and cannot be healed!"]

        if amount < 0:
            raise ValueError("Heal amount cannot be negative.")

        self._hp = min(self._hp + amount, self.hp_max)
        return [
            f"{self.name} healed for {amount} HP! ({self._hp}/{self.hp_max} HP)"
        ]

    def attack(self, target: Character) -> list[str]:
        """Attacks target character, collecting logs from the entire attack sequence."""
        if not self.is_alive:
            return [f"{self.name} is defeated and cannot attack!"]

        dealt_damage = (
            self.weapon.roll_damage() if self.weapon else self.damage
        )
        logs = [
            f"{self.name} attacks {target.name} for {dealt_damage} damage!"
        ]

        # Cascades logs returned by take_damage up to the caller
        damage_logs = target.take_damage(dealt_damage)
        logs.extend(damage_logs)  # Will work independent on the length of the log returned by take_damage()
        return logs

    def equip_weapon(self, weapon: Weapon) -> str:
        """Equips a weapon to the character and returns a confirmation string."""
        self.weapon = weapon
        return f"{self.name} equipped {weapon.name}!"

    def introduce(self) -> str:
        """Creates string that introduces character."""
        return f"Hi, my name is {self.name}!"


class Warrior(Character):
    """A heavily armored character with built-in damage mitigation."""

    DEFAULT_ARMOR: int = 5

    def __init__(
        self,
        name: str,
        hp_max: int = 120,
        damage: int = 12,
        armor: int = DEFAULT_ARMOR,
        weapon: Weapon | None = None,
    ) -> None:
        super().__init__(
            name=name, hp_max=hp_max, damage=damage, weapon=weapon
        )
        self.armor = armor

    def __repr__(self) -> str:
        return f"Warrior(name={self.name}, hp={self.hp}, armor={self.armor}, weapon={self.weapon})"

    def take_damage(self, amount: int) -> list[str]:
        """Overrides take_damage to take armor into account."""
        effective_damage = max(amount - self.armor, 0)
        blocked = amount - effective_damage

        logs = [f"🛡️ {self.name}'s armor blocked {blocked} damage!"]
        # Delegate remaining HP calculation and logging to parent class
        logs.extend(super().take_damage(effective_damage))
        return logs


class Mage(Character):
    """A spellcasting character that uses mana to deal double-damage attacks."""

    DEFAULT_MANA_MAX: int = 30

    def __init__(
        self,
        name: str,
        hp_max: int = 80,
        damage: int = 8,
        mana_max: int = DEFAULT_MANA_MAX,
        weapon: Weapon | None = None,
    ) -> None:
        super().__init__(
            name=name, hp_max=hp_max, damage=damage, weapon=weapon
        )
        self.mana_max = mana_max
        self._mana = mana_max

    @property
    def mana(self) -> int:
        """Read-only property for current mana."""
        return self._mana

    def __repr__(self) -> str:
        return f"Mage(name={self.name}, hp={self.hp}, mana={self.mana}/{self.mana_max}, weapon={self.weapon})"

    def attack(self, target: Character) -> list[str]:
        """Overrides attack to cast a Fireball spell if sufficient mana exists."""
        if not self.is_alive:
            return [f"{self.name} is defeated and cannot attack!"]

        if self._mana >= 10:
            self._mana -= 10
            spell_damage = self.damage * 2
            logs = [
                (
                    f"🔥 {self.name} casts Fireball on {target.name} for {spell_damage} damage! "
                    f"(Mana left: {self._mana}/{self.mana_max})"
                )
            ]
            logs.extend(target.take_damage(spell_damage))
            return logs
        else:
            self._mana = min(self._mana + 5, self.mana_max)  # Cannot reach more than mana_max
            logs = [
                f"🪄 {self.name} is low on mana and uses a basic attack, restoring mana ({self._mana}/{self.mana_max})."
            ]
            logs.extend(super().attack(target))
            return logs
