import operator
from collections.abc import Callable

import pytest
from temperature import Temperature


def test_valid_initialization_and_normalization() -> None:
    t1 = Temperature(25, "c")
    assert t1.value == 25.0
    assert t1.unit == "C"

    t_default = Temperature(273)
    assert t_default.value == 273.0
    assert t_default.unit == "K"


@pytest.mark.parametrize("bad_unit", ["R", "Celsius", "", "kelvin"])
def test_invalid_unit_raises(bad_unit: str) -> None:
    with pytest.raises(ValueError, match="Invalid unit"):
        Temperature(20, bad_unit)


@pytest.mark.parametrize(
    ("value", "unit"),
    [
        (-273.16, "C"),
        (-459.68, "F"),
        (-0.01, "K"),
    ],
)
def test_below_absolute_zero_raises(value: float, unit: str) -> None:
    with pytest.raises(ValueError, match="absolute zero"):
        Temperature(value, unit)


@pytest.mark.parametrize(
    ("celsius", "fahrenheit", "kelvin"),
    [
        (-273.15, -459.67, 0.0),       # Absolute zero
        (-40.0, -40.0, 233.15),        # Celsius == Fahrenheit intersection
        (0.0, 32.0, 273.15),           # Freezing point of water
        (37.0, 98.6, 310.15),          # Human body temperature
        (100.0, 212.0, 373.15),        # Boiling point of water
    ],
)
def test_unit_conversions(
    celsius: float, fahrenheit: float, kelvin: float
) -> None:
    t_c = Temperature(celsius, "C")
    assert t_c.to_celsius() == pytest.approx(celsius)
    assert t_c.to_fahrenheit() == pytest.approx(fahrenheit)
    assert t_c.to_kelvin() == pytest.approx(kelvin)

    t_f = Temperature(fahrenheit, "F")
    assert t_f.to_celsius() == pytest.approx(celsius)
    assert t_f.to_fahrenheit() == pytest.approx(fahrenheit)
    assert t_f.to_kelvin() == pytest.approx(kelvin)

    t_k = Temperature(kelvin, "K")
    assert t_k.to_celsius() == pytest.approx(celsius)
    assert t_k.to_fahrenheit() == pytest.approx(fahrenheit)
    assert t_k.to_kelvin() == pytest.approx(fahrenheit)


def test_convert_to_bad_units() -> None:
    bad_unit = "A"
    t_c = Temperature(200, "C")
    with pytest.raises(ValueError, match="Invalid target unit"):
        t_c.convert_to(bad_unit)
    t_f = Temperature(200, "F")
    with pytest.raises(ValueError, match="Invalid target unit"):
        t_f.convert_to(bad_unit)
    t_k = Temperature(200, "K")
    with pytest.raises(ValueError, match="Invalid target unit"):
        t_k.convert_to(bad_unit)


def test_convert_to_returns_new_instance() -> None:
    original = Temperature(100, "C")
    converted = original.convert_to("f")
    assert converted.unit == "F"
    assert converted.value == pytest.approx(212.0)
    assert original.unit == "C"  # Original remains unchanged


def test_round_trip_conversion_precision() -> None:
    t = Temperature(23.45, "C")
    round_trip = t.convert_to("F").convert_to("K").convert_to("C")
    assert round_trip == t


def test_cross_unit_comparisons() -> None:
    freezing_c = Temperature(0, "C")
    freezing_f = Temperature(32, "F")
    boiling_k = Temperature(373.15, "K")

    assert freezing_c == freezing_f
    assert freezing_c <= freezing_f
    assert freezing_c >= freezing_f
    assert not (freezing_c < freezing_f)
    assert not (freezing_c > freezing_f)

    assert freezing_c < boiling_k
    assert boiling_k > freezing_f
    assert (freezing_c == "0 C") is False


def test_string_representations() -> None:
    t = Temperature(21.5, "c")
    assert repr(t) == "Temperature(21.5, C)"
    assert str(t) == "21.50 C"


@pytest.mark.parametrize(
    "dunder_name",
    ["__eq__", "__ne__", "__lt__", "__le__", "__gt__", "__ge__"],
)
def test_comp_dunders_return_not_implemented(dunder_name: str) -> None:
    t = Temperature(300)
    dunder = getattr(t, dunder_name)
    assert dunder(300) is NotImplemented


@pytest.mark.parametrize(
    "op",
    [operator.lt, operator.le, operator.gt, operator.ge],
)
def test_ordering_operators_raise_type_error(op: Callable[[object, object], bool]) -> None:
    t = Temperature(300)
    with pytest.raises(TypeError):
        op(t, 300)


def test_equality_operators_fallback_to_identity() -> None:
    t = Temperature(300)
    assert (t == 300) is False
    assert (t != 300) is True
