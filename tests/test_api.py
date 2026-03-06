import uuid

from fastapi.testclient import TestClient

from app_api.main import app

client = TestClient(app)

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

def test_read_db():
    """Test read DB."""
    r = client.get("/users/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)



def test_create_user():
    """Test create user root."""
    name = f"user_{uuid.uuid4()}"

    r = client.post(f"/users/?name={name}")

    assert r.status_code == 200
    assert r.json()["name"] == name
