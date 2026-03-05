# tests/test_front.py
import pytest

from app_front import main


# Mock для add_numbers ---------------------------
def test_add_numbers(monkeypatch):
    """Test add_numbers function with mocked API response."""
    class MockResponse:
        def json(self):
            return {"result": 10}

    # Подменяем requests.get внутри app_front.main
    monkeypatch.setattr("app_front.main.requests.get", lambda url: MockResponse())
    result = main.add_numbers(3, 7)
    assert result == 10

# ---------------------------
# Mock для sub_numbers
# ---------------------------
def test_sub_numbers(monkeypatch):
    """Test sub_numbers function with mocked API response."""
    class MockResponse:
        def json(self):
            return {"result": 4}

    monkeypatch.setattr("app_front.main.requests.get", lambda url: MockResponse())
    result = main.sub_numbers(7, 3)
    assert result == 4

# ---------------------------
# UI labels
# ---------------------------
def test_ui_labels():
    """Test that Streamlit UI labels are present."""
    labels = main.get_ui_labels()
    assert "A" in labels
    assert "B" in labels
    assert "Add" in labels
    assert "Sub" in labels
    assert "Math App" in labels