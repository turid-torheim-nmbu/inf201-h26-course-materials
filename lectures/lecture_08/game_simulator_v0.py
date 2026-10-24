# Procedural approach: Loose dictionaries and detached functions
# Turid Torheim, NMBU, 2026

def take_damage(player: dict, amount: int) -> None:
    """Player hp is updated after taking amount damage"""
    player["hp"] -= amount
    if player["hp"] < 0:
        player["hp"] = 0


def heal(player: dict, amount: int) -> None:
    """Player hp is updated after healing amount points"""
    player["hp"] += amount
