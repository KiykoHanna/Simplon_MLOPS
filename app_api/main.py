import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from math_utils.my_math import add, square, sub
from models import models
from modules import crud
from modules.connect import get_db

load_dotenv()

app = FastAPI()

if os.getenv("DOCKER", "false").lower() == "true":
    API_URL = os.getenv("API_URL")  # внутри Docker
else:
    API_URL = "http://localhost:8000"  # локально

API_PORT = int(os.getenv("API_PORT", 8000))
API_HOST = os.getenv("API_HOST", "0.0.0.0")


# math----------------------------------------------------
@app.get("/")
def root():
    """Create root endpoint."""
    return {"message": "API running"}


@app.get("/add")
def add_route(a: int, b: int):
    """Create add endpoint."""
    return {"result": add(a, b)}


@app.get("/sub")
def sub_route(a: int, b: int):
    """Create sub endpoint."""
    return {"result": sub(a, b)}


@app.get("/square")
def square_route(a: int):
    """Create square royte endpoint."""
    return {"result": square(a)}


# DB POST--------------------------------------------------------
@app.post("/users/")
def create_user(name: str, db: Session = Depends(get_db)):
    """Create a user."""
    user = crud.create_user(db, name)  # пусть возвращает объект
    return {"id": user.id, "name": user.name}


@app.post("/models/")
def create_model(name: str, db: Session = Depends(get_db)):
    """Post models, endpoint."""
    model = crud.create_model(db, name)
    return {"id": model.id, "name": model.name}


@app.post("/predictions/")
def create_prediction(
    user_id: int,
    model_id: int,
    probability: float,
    db: Session = Depends(get_db),
):
    """Post prediction, endpoint."""
    pred_id = crud.create_prediction(db, user_id, model_id, probability)
    return {"id": pred_id}


# DB ALL GET  -----------------------------------------------------
@app.get("/data/")
def get_all_data(db: Session = Depends(get_db)):
    """Return all users, models, and predictions."""
    return crud.read_all(db)


# DB GET ID --------------------------------------------------------


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get a user by ID, endpoint."""
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.get("/models/{model_id}")
def get_model(model_id: int, db: Session = Depends(get_db)):
    """Get a model by ID, endpoint."""
    model = db.query(models.AIModel).filter(models.AIModel.id == model_id).first()

    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")

    return model


# GET USERS, MODELS, PREDICTIONS ---------------------------------------


@app.get("/users/")
def get_all_users(db: Session = Depends(get_db)):
    """Return all users."""
    users = db.query(models.User).all()
    return [{"id": u.id, "name": u.name} for u in users]


@app.get("/models/")
def get_all_models(db: Session = Depends(get_db)):
    """Return all AI models."""
    ai_models = db.query(models.AIModel).all()
    return [{"id": m.id, "name": m.name} for m in ai_models]


@app.get("/predictions/")
def get_all_predictions(db: Session = Depends(get_db)):
    """Return all predictions.

    Returns:
        list[dict]:
        Each dict contains 'id', 'user_id', 'ai_model_id', 'probability', 'timestamp'

    """
    preds = db.query(models.Prediction).all()
    return [
        {
            "id": p.id,
            "user_id": p.user_id,
            "ai_model_id": p.ai_model_id,
            "probability": p.probability,
            "timestamp": p.timestamp.isoformat() if p.timestamp else None,
        }
        for p in preds
    ]


# DB DELETE ---------------------------------------------------------


@app.delete("/prediction/{pred_id}")
def del_pred(pred_id: int, db: Session = Depends(get_db)):
    """Delete prediction by id, endpoint."""
    crud.delete_user(db, pred_id)
    return {"result": "Prediction est suprimé"}


# DB UPDATE ---------------------------------------------------------


@app.put("/users/{user_id}")
def update_user(user_id: int, new_name: str, db: Session = Depends(get_db)):
    """Update user information by id."""
    crud.update_user(db, user_id, new_name)
    return {"result": "Information est renouvlé"}


@app.put("/models/{model_id}")
def update_model(model_id: int, new_name: str, db: Session = Depends(get_db)):
    """Update model information by id, endpoint."""
    crud.update_model(db, model_id, new_name)
    return {"result": "Information est renouvlé"}
