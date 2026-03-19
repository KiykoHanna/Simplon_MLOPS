# tests/test_front.py

from unittest.mock import patch

from app_front.pages.insert import (
    create_model,
    create_prediction,
    create_user,
    insert_prediction_flow,
)
from app_front.pages.udate_delete import delete_prediction, update_user


# ------------------- Test create user -------------------
def test_create_user():
    """Test create_user returns correct dict."""
    with patch("app_front.pages.insert.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"id": 1, "name": "Alice"}

        res = create_user("http://test", "Alice")

        assert isinstance(res, dict)
        assert res["id"] == 1
        assert res["name"] == "Alice"


# ------------------- Test create model -------------------
def test_create_model():
    """Test create_model via mocked API call."""
    with patch("app_front.pages.insert.requests.post") as mock_post:
        # Настраиваем мок, чтобы вернулся словарь с id и name
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"id": 2, "name": "ModelX"}

        res = create_model("http://test", "ModelX")

        assert res["id"] == 2
        assert res["name"] == "ModelX"


# ------------------- Test create prediction -------------------
def test_create_prediction():
    """Test create_prediction returns API result."""
    with patch("app_front.pages.insert.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"result": "ok"}

        res = create_prediction("http://test", 1, 2, 0.9)

        assert res["result"] == "ok"


# ------------------- Test full insert flow -------------------
def test_insert_prediction_flow():
    """Test insert_prediction_flow returns API result."""
    with patch("app_front.pages.insert.requests.post") as mock_post:
        mock_post.return_value.status_code = 200

        # Последовательные ответы API: user, model, prediction
        mock_post.return_value.json.side_effect = [
            {"id": 1, "name": "Alice"},  # user
            {"id": 2, "name": "ModelX"},  # model
            {"result": "ok"},  # prediction
        ]

        res = insert_prediction_flow("http://test", "Alice", "ModelX", 0.9)

        assert res["result"] == "ok"


# ------------------- Test delete prediction -------------------
def test_delete_prediction():
    """Test delete_prediction returns API result."""
    with patch("app_front.pages.udate_delete.requests.delete") as mock_delete:
        mock_delete.return_value.status_code = 200
        mock_delete.return_value.json.return_value = {"result": "ok"}

        res = delete_prediction("http://test", 1)

        assert res["result"] == "ok"


# ------------------- Test update user -------------------
def test_update_user():
    """Test update_user returns API result."""
    with patch("app_front.pages.udate_delete.requests.put") as mock_put:
        mock_put.return_value.status_code = 200
        mock_put.return_value.json.return_value = {"result": "updated"}

        res = update_user("http://test", 1, "Alice")

        assert res["result"] == "updated"

