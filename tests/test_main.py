"""tests.test_main.py."""

import pytest

from app.modules.my_math import add, print_data, square, sub


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

def test_sub(a, b, expected):
    """Test that add returns the correct sum."""
    assert add(a, b) == expected
