# from __future__ import annotations  # include this if you are using an earlier version of Python than 3.14
import math


class Temperature:
    """Represents a physical temperature value in Celsius, Fahrenheit, or Kelvin."""

    VALID_UNITS = ("C", "F", "K")
    _TOLERANCE = 1e-9

    def __init__(self, value: float, unit: str = "K") -> None:
        """Initialise with value and unit"""
        normalized_unit = unit.strip().upper()
        if normalized_unit not in self.VALID_UNITS:
            raise ValueError(
                f"Invalid unit {unit}. Expected one of {self.VALID_UNITS}."
            )

        self._value = float(value)
        self._unit = normalized_unit

        if self.to_kelvin() < -self._TOLERANCE:
            raise ValueError(
                f"Temperature {self._value} °{self._unit} is below absolute zero."
            )

    @property
    def value(self) -> float:
        """View temperature value"""
        return self._value

    @property
    def unit(self) -> str:
        """View temperature unit"""
        return self._unit

    def to_kelvin(self) -> float:
        """Convert temperature to Kelvin"""
        if self._unit == "K":
            return self._value
        if self._unit == "C":
            return self._value + 273.15
        return (self._value - 32.0) * 5.0 / 9.0 + 273.15

    def to_celsius(self) -> float:
        """Convert temperature to Celsius"""
        if self._unit == "C":
            return self._value
        if self._unit == "K":
            return self._value - 273.15
        return (self._value - 32.0) * 5.0 / 9.0

    def to_fahrenheit(self) -> float:
        """Convert temperature to Fahrenheit"""
        if self._unit == "F":
            return self._value
        if self._unit == "C":
            return self._value * 9.0 / 5.0 + 32.0
        return (self._value - 273.15) * 9 / 5 + 32.0
        # return (self._value - 273.15) * 9.0 / 5.0 + 32.0

    def convert_to(self, target_unit: str) -> Temperature:
        """Convert temperature to target unit"""
        normalized = target_unit.strip().upper()
        if normalized == "C":
            return Temperature(self.to_celsius(), "C")
        if normalized == "F":
            return Temperature(self.to_fahrenheit(), "F")
        if normalized == "K":
            return Temperature(self.to_kelvin(), "K")
        raise ValueError(
            f"Invalid target unit {target_unit}. Expected one of {self.VALID_UNITS}."
        )

    def __repr__(self) -> str:
        """Display representation of Temperature object"""
        return f"Temperature({self._value}, {self._unit})"

    def __str__(self) -> str:
        """Print representation of Temperature object"""
        return f"{self._value:.2f} {self._unit}"

    def __eq__(self, other: object) -> bool:
        """Equality of two Temperature objects"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return math.isclose(
            self.to_kelvin(),
            other.to_kelvin(),
            rel_tol=self._TOLERANCE,
            abs_tol=self._TOLERANCE,
        )

    def __lt__(self, other: object) -> bool:
        """Less than comparison between Temperature and another object"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return not (self == other) and self.to_kelvin() < other.to_kelvin()

    def __le__(self, other: object) -> bool:
        """Less than or equal to comparison between Temperature and another object"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self == other) or (self.to_kelvin() < other.to_kelvin())

    def __gt__(self, other: object) -> bool:
        """Greater than comparison between Temperature and another object"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return not (self == other) and self.to_kelvin() > other.to_kelvin()

    def __ge__(self, other: object) -> bool:
        """Greater than or equal to comparison between Temperature and another object"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self == other) or (self.to_kelvin() > other.to_kelvin())
