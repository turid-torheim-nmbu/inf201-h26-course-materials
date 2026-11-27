"""
Example code for testing represention fractions in terms of integer numerators and denominators.
Written by Hans Ekkehard Plesser, NMBU
Added type hints and doc-strings: Turid Torheim, NMBU
"""


import pytest
from fraction import Fraction


@pytest.mark.parametrize('num, den',
                         [(2, 3),
                          (2., 3.),
                          (4, 1),
                          (0, 1),
                          (-5, 12)])
def test_create_legal(num: int, den: int) -> None:
    """Parametrised test of valid fraction denominator and numerator pairs"""
    Fraction(num, den)


@pytest.mark.parametrize('num, den',
                         [(2, 0),
                          (0, 0),
                          (0, -1),
                          (5, -12),
                          (3.2, 2),
                          (2, 3.1)])
def test_create_illegal(num: int, den: int) -> None:
    """Parametrised test of non-valid fraction denominator and numerator pairs"""
    with pytest.raises(ValueError):
        Fraction(num, den)


@pytest.mark.parametrize('x, y',
                         [(Fraction(1, 2), Fraction(1, 2)),
                          (Fraction(1, 2), Fraction(2, 4)),
                          (2, Fraction(4, 2)),
                          (Fraction(9, 3), 3),
                          (-Fraction(4, 5), Fraction(-4, 5)),
                          (-Fraction(-4, 5), Fraction(4, 5)),
                          (Fraction(2, 3), Fraction(2., 3.))
                          ])
def test_eq(x: Fraction, y: Fraction) -> None:
    """Parametrised test of equality"""
    assert x == y


@pytest.mark.parametrize('x, y',
                         [(Fraction(3, 2), Fraction(2, 4)),
                          (2, Fraction(2, 4)),
                          (Fraction(3, 9), 3),
                          (Fraction(4, 5), 0),
                          ])
def test_neq(x: Fraction, y: Fraction) -> None:
    """Parametrised test of inequality"""
    assert x != y


@pytest.mark.parametrize('x, y, res',
                         [(Fraction(1, 2), Fraction(2, 3), Fraction(7, 6)),
                          (Fraction(-1, 2), Fraction(2, 3), Fraction(1, 6)),
                          (Fraction(1, 2), 1, Fraction(3, 2)),
                          (1, Fraction(1, 2), Fraction(3, 2)),
                          ])
def test_add(x: Fraction, y: Fraction, res: Fraction) -> None:
    """Parametrised test of addition"""
    assert x + y == res


@pytest.mark.parametrize('x, y, res',
                         [(Fraction(1, 2), Fraction(2, 3), Fraction(-1, 6)),
                          (Fraction(-1, 2), Fraction(2, 3), Fraction(-7, 6)),
                          (Fraction(1, 2), 1, Fraction(-1, 2)),
                          (1, Fraction(1, 2), Fraction(1, 2)),
                          ])
def test_sub(x: Fraction, y: Fraction, res: Fraction) -> None:
    """Parametrised test of subtraction"""
    assert x - y == res


@pytest.mark.parametrize('x, y, res',
                         [(Fraction(1, 2), Fraction(2, 3), Fraction(1, 3)),
                          (Fraction(-1, 2), Fraction(2, 3), Fraction(-1, 3)),
                          (Fraction(1, 2), 1, Fraction(1, 2)),
                          (1, Fraction(1, 2), Fraction(1, 2)),
                          (Fraction(5, 7), Fraction(2, 3), Fraction(10, 21)),
                          (0, Fraction(1, 2), Fraction(0, 1))
                          ])
def test_mul(x: Fraction, y: Fraction, res: Fraction) -> None:
    """Parametrised test of multiplication"""
    assert x * y == res


@pytest.mark.parametrize('x, y, res',
                         [(Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)),
                          (Fraction(-1, 2), Fraction(2, 3), Fraction(-3, 4)),
                          (Fraction(1, 2), 1, Fraction(1, 2)),
                          (1, Fraction(1, 2), Fraction(2, 1)),
                          (Fraction(5, 7), Fraction(2, 3), Fraction(15, 14)),
                          (0, Fraction(1, 2), Fraction(0, 1))
                          ])
def test_div(x: Fraction, y: Fraction, res: Fraction) -> None:
    """Parametrised test of division"""
    assert x / y == res


@pytest.mark.parametrize('x, y, res',
                         [(Fraction(-1, 2), 2, Fraction(1, 4)),
                          (Fraction(2, 3), -1, Fraction(3, 2)),
                          (Fraction(2, 3), 2., Fraction(4, 9)),
                          (Fraction(2, 3), 0, Fraction(1, 1)),
                          ])
def test_pow(x: Fraction, y: Fraction, res: Fraction) -> None:
    """Parametrised test of valid powers"""
    assert x**y == res


@pytest.mark.parametrize('x, y',
                         [(Fraction(1, 2), Fraction(2, 1)),
                          (Fraction(1, 2), 1.5),
                          (Fraction(1, 2), False),
                          ])
def test_pow_error(x: Fraction, y: Fraction) -> None:
    """Parametrised test of non-valid powers"""
    with pytest.raises(ValueError):
        x**y


@pytest.mark.parametrize('x, y',
                         [(Fraction(2, 3), Fraction(4, 5)),
                          (Fraction(-2, 3), Fraction(-1, 3)),
                          (Fraction(-2, 3), 0),
                          (1, Fraction(5, 3)),
                          (Fraction(2, 3), 0.7)
                          ])
def test_less_than(x: Fraction, y: Fraction) -> None:
    """Parametrised test of less than comparison"""
    assert x < y


@pytest.mark.parametrize('x, y',
                         [(Fraction(2, 3), Fraction(4, 5)),
                          (Fraction(-2, 3), Fraction(-1, 3)),
                          (Fraction(-2, 3), 0),
                          (1, Fraction(5, 3)),
                          (Fraction(2, 3), 0.7)
                          ])
def test_greater_than(x: Fraction, y: Fraction) -> None:
    """Parametrised test of greater than comparison"""
    assert y > x


@pytest.mark.parametrize('x, y',
                         [(Fraction(2, 3), Fraction(4, 5)),
                          (Fraction(2, 3), Fraction(2, 3))
                          ])
def test_less_equal(x: Fraction, y: Fraction) -> None:
    """Parametrised test of less than or equal comparison"""
    assert x <= y


@pytest.mark.parametrize('x, y',
                         [(Fraction(2, 3), Fraction(4, 5)),
                          (Fraction(2, 3), Fraction(2, 3))
                          ])
def test_greater_equal(x: Fraction, y: Fraction) -> None:
    """Parametrised test of greater than or equal comparison"""
    assert y >= x


def test_equal_is_not_less() -> None:
    """Test of difference between equal and less than"""
    assert not Fraction(2, 3) < Fraction(2, 3)


def test_equal_is_not_greater() -> None:
    """Test of difference between equal and greater than"""
    assert not Fraction(2, 3) > Fraction(2, 3)


def test_str() -> None:
    """Test of print representation"""
    assert str(Fraction(-2, 3)) == "-2/3"


def test_repr() -> None:
    """Test of display representation"""
    assert repr(Fraction(-2, 3)) == "Fraction(-2, 3)"
