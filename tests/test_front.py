# tests/test_front.py
import pytest

from app_front import main  # импортируешь свой main.py Streamlit


# Пример теста для функции/логики
def test_add_input(monkeypatch):
    """Тестируем функцию, которая обрабатывает ввод пользователя."""
    # Предположим, в main есть функция process_input(a, b)
    result = main.process_input(3, 7)
    assert result == 10

def test_square_input(monkeypatch):
    """Тестируем квадрат числа."""
    result = main.process_square(4)
    assert result == 16

def test_ui_elements():
    """Проверяем, что Streamlit main содержит ключевые элементы."""
    # Для примера можно проверить наличие строк с заголовками
    ui_texts = main.get_ui_texts()  # функция, которая возвращает заголовки/лейблы
    assert "Enter your numbers" in ui_texts
    assert "Result" in ui_texts
