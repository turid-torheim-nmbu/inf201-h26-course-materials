# Review of intro to OOP, with 3 errors
# Turid Torheim, NMBU

class BankAccount:
    """Represents a simple bank account with managed balance."""

    def __init__(owner: str, balance: float = 100.0) -> None:
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        """Public read-only view of current balance."""
        return self._balance

    def withdraw(amount: float) -> None:
        """Withdraw funds from the account."""
        if amount > self._balance:
            raise ValueError("Insufficient funds!")
        self._balance -= amount

    def deposit(self, amount: float) -> None:
        """Deposit funds into the account."""
        self._balance += amount

    def __repr__(self) -> str:
        print(f"BankAccount(owner={self.owner!r}, balance={self.balance})")


# --- Test Code ---
account = BankAccount("Alice", balance=250.0)

# Increase balance by 100
account.balance = 350.0

# Print current balance
print(f"{account.owner}'s balance: ${account.balance()}")

# Perform a withdrawal
account.withdraw(50.0)
