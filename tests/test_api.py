import uuid
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from app_api.main import app
from app_front.pages.read import (
    format_predictions,
    get_models,
    get_predictions,
    get_users,
)

client = TestClient(app)

# math ----------------------------------------------------
def test_root():
    """Test root."""
    r = client.get("/")
    assert r.status_code == 200

def test_add():
    """Test add route."""
    r = client.get("/add?a=5&b=7")
    assert r.status_code == 200
    assert r.json()["result"] == 12


def test_sub():
    """Test sub route."""
    r = client.get("/sub?a=7&b=5")
    assert r.status_code == 200
    assert r.json()["result"] == 2


def test_square():
    """Test square route."""
    r = client.get("/square?a=4")
    assert r.status_code == 200
    assert r.json()["result"] == 16

# DB -----------------------------------------------------
def test_read_db():
    """Test read DB."""
    r = client.get("/data/")
    assert r.status_code == 200
    assert isinstance(r.json(), dict)
    assert "users" in r.json()
    assert "models" in r.json()
    assert "predictions" in r.json()

# CREATE ---------------------------------
def test_create_user():
    """Test create user root."""
    name = f"user_{uuid.uuid4()}"

    r = client.post(f"/users/?name={name}")

    assert r.status_code == 200
    assert r.json()["name"] == name

def test_create_model():
    """Test create model root."""
    name = f"model_{uuid.uuid4()}"

    r = client.post(f"/models/?name={name}")

    assert r.status_code == 200
    assert r.json()["name"] == name


def test_get_users():
    """Test get users."""
    with patch("app_front.pages.read.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"id": 1, "name": "Alice"}
        ]

        res = get_users("http://test")

        assert isinstance(res, list)
        assert res[0]["name"] == "Alice"

def test_get_models():
    """Test get models."""
    with patch("app_front.pages.read.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"id": 1, "name": "ModelX"}
        ]

        res = get_models("http://test")

        assert res[0]["name"] == "ModelX"

def test_get_predictions():
    """Test."""
    with patch("app_front.pages.read.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "user_id": 1,
                "ai_model_id": 1,
                "probability": 0.9,
                "timestamp": "2026-01-01",
            }
        ]

        res = get_predictions("http://test")

        assert res[0]["probability"] == 0.9

# FORMAT TEST ----------------

def test_format_predictions():
    """Test format prediction."""
    users = [{"id": 1, "name": "Alice"}]
    models = [{"id": 1, "name": "ModelX"}]
    preds = [
        {
            "user_id": 1,
            "ai_model_id": 1,
            "probability": 0.85,
            "timestamp": "2026-01-01",
        }
    ]

    result = format_predictions(preds, users, models)

    assert result[0]["User"] == "Alice"
    assert result[0]["AI Model"] == "ModelX"
    assert result[0]["Probability"] == 0.85

def test_format_predictions_unknown():
    """Test."""
    users = []
    models = []
    preds = [
        {
            "user_id": 99,
            "ai_model_id": 99,
            "probability": 0.5,
            "timestamp": "2026-01-01",
        }
    ]

    result = format_predictions(preds, users, models)

    assert result[0]["User"] == "Unknown"
    assert result[0]["AI Model"] == "Unknown"


def test_get_users_error():
    """Test."""
    with patch("app_front.pages.read.requests.get") as mock_get:
        mock_get.side_effect = Exception("API error")

        with pytest.raises(Exception):
            get_users("http://test")

