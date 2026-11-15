"""engine.py - Combat engine for turn-based battles between characters."""

from characters import Character


class Battle:
    """Manages combat between a hero and an enemy character."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy

    def play_round(self, verbose: bool = False) -> list[str]:
        """Executes one round of combat, printing and returning all event messages."""
        round_logs: list[str] = []  # Logs from this round of combat

        if not self.hero.is_alive or not self.enemy.is_alive:
            return round_logs  # Battle has ended

        # Hero attacks enemy
        hero_logs = self.hero.attack(self.enemy)
        round_logs.extend(hero_logs)

        # Enemy counter-attacks if still alive
        if self.enemy.is_alive:
            enemy_logs = self.enemy.attack(self.hero)
            round_logs.extend(enemy_logs)

        # Battle controls console output
        if verbose:
            for log in round_logs:
                print(log)

        return round_logs

    def simulate_battle(self, verbose: bool = False) -> Character:
        """Simulates combat until one character is defeated and returns the winner."""
        if verbose:
            print(f"=== BATTLE START: {self.hero.name} vs {self.enemy.name} ===")

        round_num = 1
        while self.hero.is_alive and self.enemy.is_alive:
            if verbose:
                print(f"\n--- Round {round_num} ---")
            self.play_round(verbose=verbose)
            round_num += 1

        winner = self.hero if self.hero.is_alive else self.enemy
        if verbose:
            print(f"\n=== BATTLE END: {winner.name} is victorious! ===")
        return winner  # This way you can access the winner also when verbose=False
