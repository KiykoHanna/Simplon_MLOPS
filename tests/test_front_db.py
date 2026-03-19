# tests/test_front.py

from unittest.mock import patch

from app_front.pages.insert import (
    create_model,
    create_prediction,
    create_user,
    insert_prediction_flow,
)
from app_front.pages.udate_delete import delete_prediction, update_user


# test create ---------------------------------------------------
def test_create_user():
    """Test create user."""
    with patch("app_front.pages.insert.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"id": 1}

        res = create_user("http://test", "Alice")

        assert res == 1


def test_create_model():
    """Test create model."""
    with patch("app_front.pages.insert.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"id": 2}

        res = create_model("http://test", "ModelX")

        assert res == 2


def test_create_prediction():
    """Test create prediction."""
    with patch("app_front.pages.insert.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"result": "ok"}

        res = create_prediction("http://test", 1, 2, 0.9)

        assert res["result"] == "ok"


def test_insert_prediction_flow():
    """Test insert prediction."""
    with patch("app_front.pages.insert.requests.post") as mock_post:
        mock_post.return_value.status_code = 200

        # последовательные ответы API
        mock_post.return_value.json.side_effect = [
            {"id": 1},  # user
            {"id": 2},  # model
            {"result": "ok"},  # prediction
        ]

        res = insert_prediction_flow("http://test", "Alice", "ModelX", 0.9)

        assert res["result"] == "ok"

# test delete ------------------------------------------------
def test_delete_prediction():
    """Test delete_prediction."""
    with patch("app_front.main.requests.delete") as mock_delete:
        mock_delete.return_value.status_code = 200
        mock_delete.return_value.json.return_value = {"result": "ok"}

        res = delete_prediction("http://test", 1)

        assert res["result"] == "ok"

# test update -------------------------------------------------
def test_update_user():
    """Test update_user."""
    with patch("app_front.main.requests.put") as mock_put:
        mock_put.return_value.status_code = 200
        mock_put.return_value.json.return_value = {"result": "updated"}

        res = update_user("http://test", 1, "Alice")

        assert res["result"] == "updated"
