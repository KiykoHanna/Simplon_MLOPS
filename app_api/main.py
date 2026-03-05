import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .math.my_math import add, square, sub
from .models import models
from .modules import crud
from .modules.connect import get_db

load_dotenv()

app = FastAPI()

API_PORT = int(os.getenv("API_PORT", 8000))
API_HOST = os.getenv("API_HOST", "0.0.0.0")

# math----------------------------------------------------
@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/add")
def add_route(a: int, b: int):
    return {"result": add(a,b)}

@app.get("/sub")
def sub_route(a: int, b: int):
    return {"result": sub(a,b)}

@app.get("/square")
def square_route(x: int):
    return {"result": square(x)}

# DB POST--------------------------------------------------------
@app.post("/users/")
def add_user(name: str, db: Session = Depends(get_db)):
    return crud.create_user(db, name)

@app.post("/models/")
def add_model(name: str, db: Session = Depends(get_db)):
    return crud.create_model(db, name)

@app.post("/predictions/")
def add_prediction(
    user_id: int, model_id: int, probability: float, db: Session = Depends(get_db)
    ):
    return crud.create_prediction(db, user_id, model_id, probability)

# DB GET  -----------------------------------------------------

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.get("/models/")
def get_models(db: Session = Depends(get_db)):
    return db.query(models.AIModel).all()

@app.get("/predictions/")
def get_predictions(db: Session = Depends(get_db)):
    return db.query(models.Prediction).all()