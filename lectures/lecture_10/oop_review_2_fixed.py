"""Pet class with subclasses, and a Toy class"""


class Toy:
    """Represents a toy"""

    def __init__(self, name: str) -> None:
        """Create a toy with a name"""
        self.name = name


class Pet:
    """Represents any pet"""

    def __init__(self, name: str, toy: Toy | None = None) -> None:
        """Creates a pet with an optional toy"""
        self.name = name
        self.toy = toy

    def talk(self) -> str:
        """A string the pet can say"""
        return "I can't talk"


class Dog(Pet):
    """Pet of type Dog"""

    def talk(self) -> None:
        """A string the dog can say"""
        return "Bark!"
