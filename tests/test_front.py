# tests/test_front.py
import pytest

from app_front import main  # импортируешь свой main.py Streamlit


# Пример теста для функции/логики
def test_add_input(monkeypatch):
    """Test input for summ."""
    result = main.add_numbers(3, 7)
    assert result == 10

def test_square_input(monkeypatch):
    """Test input for square."""
    result = main.square_numbers(4)
    assert result == 16

def test_ui_elements():
    """Test Streamlit main contain elements."""
    labels = main.get_ui_labels()  # функция, которая возвращает заголовки/лейблы
    assert "A" in labels
    assert "B" in labels
    assert "Add" in labels
    assert "Sub" in labels
    assert "Math App" in labels
