"""tests.test_main.py."""

import pandas as pd
import pytest

from app_api.math.my_math import add, print_data, square, sub


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 12),
        (20, 2, 22),
        (0, 2, 2),
    ],
)
def test_add(a, b, expected):
    """Test that add returns the correct sum."""
    assert add(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 8),
        (20, 2, 18),
        (0, 2, -2),
    ],
)
def test_sub(a, b, expected):
    """Test that sub returns the correct difference."""
    assert sub(a, b) == expected

@pytest.mark.parametrize(
    "a, expected",
    [
        (5, 25),
        (0, 0),
        (-4, 16),
    ],
)
def test_square(a, expected):
    """Test that square returns the correct result."""
    assert square(a) == expected


@pytest.fixture
def test_print_data():
    """Test that print data returns the correct result."""
    assert print_data(pd.DataFrame([1, 2, 3])) == len([1, 2, 3])

