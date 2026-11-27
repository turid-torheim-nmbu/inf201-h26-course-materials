"""
Example code for represention fractions in terms of integer numerators and denominators.
Note: rhs and lhs indicated right hand side and left hand side respectively.

Written by Hans Ekkehard Plesser, NMBU
Added type hints and doc-strings: Turid Torheim, NMBU
"""


class Fraction:
    """Representing fractions between integers"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialise with a numerator and a denominator"""

        self.numer = int(numerator)
        self.denom = int(denominator)

        if self.numer != numerator:  # i.e. is not integer
            raise ValueError("Numerator must have integer value.")
        if self.denom != denominator:  # i.e. is not integer
            raise ValueError("Denominator must have integer value.")
        if self.denom <= 0:
            raise ValueError("Denominator must be > 0.")

    def __str__(self) -> str:
        """Print representation"""
        return f"{self.numer}/{self.denom}"

    def __repr__(self) -> str:
        """Display representation"""
        return f"Fraction({self.numer}, {self.denom})"

    def __eq__(self, rhs: Fraction) -> bool:
        """Equality"""
        try:
            return self.numer * rhs.denom == rhs.numer * self.denom
        except AttributeError:
            return self == Fraction(rhs, 1)

    def __ne__(self, rhs: Fraction) -> bool:
        """Not equal"""
        return not self == rhs

    def __lt__(self, rhs: Fraction) -> bool:
        """Less than"""
        try:
            return self.numer * rhs.denom < rhs.numer * self.denom
        except AttributeError:
            return self.numer < rhs * self.denom

    def __le__(self, rhs: Fraction) -> bool:
        """Less than or equal"""
        return self < rhs or self == rhs

    def __gt__(self, rhs: Fraction) -> bool:
        """Greater than"""
        try:
            return self.numer * rhs.denom > rhs.numer * self.denom
        except AttributeError:
            return self.numer > rhs * self.denom

    def __ge__(self, rhs: Fraction) -> bool:
        """Greater than or equal"""
        return rhs <= self

    def __neg__(self) -> Fraction:
        """Negative"""
        return Fraction(-self.numer, self.denom)

    def __add__(self, rhs: Fraction) -> Fraction:
        """Addition (self + rhs)"""
        try:
            return Fraction(self.numer * rhs.denom + self.denom * rhs.numer, self.denom * rhs.denom)
        except AttributeError:
            return self + Fraction(rhs, 1)

    def __radd__(self, lhs: Fraction) -> Fraction:
        """Addition (lhs + self)"""
        return self + lhs

    def __sub__(self, rhs: Fraction) -> Fraction:
        """Subtraction (self - rhs)"""
        return self + (-rhs)

    def __rsub__(self, lhs: Fraction) -> Fraction:
        """Subtraction (lhs - self)"""
        return -self + lhs

    def __mul__(self, rhs: Fraction) -> Fraction:
        """Multiplication (self*rhs)"""
        try:
            return Fraction(self.numer * rhs.numer, self.denom * rhs.denom)
        except AttributeError:
            return self * Fraction(rhs, 1)

    def __rmul__(self, lhs: Fraction) -> Fraction:
        """Multiplication (lhs*self)"""
        return self * lhs

    def __truediv__(self, rhs: Fraction) -> Fraction:
        """Division (self/rhs)"""
        try:
            return Fraction(self.numer * rhs.denom, self.denom * rhs.numer)
        except AttributeError:
            return self / Fraction(rhs, 1)

    def __rtruediv__(self, lhs: Fraction) -> Fraction:
        """Division (lhs/self)"""
        return Fraction(lhs, 1) / self

    def __pow__(self, rhs: int) -> Fraction:
        """Exponent (self**rhs)"""
        if isinstance(rhs, bool):
            raise ValueError("Exponent must be an integer.")
        try:
            rhs_int = int(rhs)
        except TypeError:
            raise ValueError("Exponent must be an integer.") from None

        if rhs != rhs_int:
            raise ValueError("Exponent must be an integer.")

        if rhs_int > 0:
            return Fraction(self.numer**rhs_int, self.denom**rhs_int)
        if rhs_int == 0:
            return Fraction(1, 1)
        return (1 / self) ** (-rhs_int)
