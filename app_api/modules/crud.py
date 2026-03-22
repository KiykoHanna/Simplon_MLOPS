from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import models


# Create ----------------------------------------------------------------------------
def create_user(db: Session, name: str):
    """Create a user if not exists, else return existing one.

    Args:
        db (Session): SQLAlchemy session
        name (str): User name

    Returns:
        User: SQLAlchemy User object with id and name

    """
    try:
        # Проверяем, есть ли такой пользователь
        user = db.query(models.User).filter(models.User.name == name).first()
        if user:
            return user

        # Создаём нового пользователя
        user = models.User(name=name)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except IntegrityError:
        db.rollback()
        # На случай гонки или уникальной ошибки
        user = db.query(models.User).filter(models.User.name == name).first()
        if user:
            return user
        raise HTTPException(status_code=500, detail="Failed to create user")


def create_model(db: Session, name: str):
    """Create an AI model if not exists, else return existing one.

    Args:
        db (Session): SQLAlchemy session
        name (str): Model name

    Returns:
        AIModel: SQLAlchemy AIModel object with id and name

    """
    try:
        model = db.query(models.AIModel).filter(models.AIModel.name == name).first()
        if model:
            return model

        model = models.AIModel(name=name)
        db.add(model)
        db.commit()
        db.refresh(model)
        return model

    except IntegrityError:
        db.rollback()
        model = db.query(models.AIModel).filter(models.AIModel.name == name).first()
        if model:
            return model
        raise HTTPException(status_code=500, detail="Failed to create model")


def create_prediction(db: Session, user_id: int, model_id: int, probability: float):
    """Create prediction."""
    pred = models.Prediction(
        user_id=user_id, ai_model_id=model_id, probability=probability
    )
    db.add(pred)
    db.commit()
    db.refresh(pred)
    return pred


# Read DB ----------------------------------------------------------------------------
def read_all(db: Session):
    """Read all data."""
    users = db.query(models.User).all()
    models_list = db.query(models.AIModel).all()
    predictions = db.query(models.Prediction).all()

    return {
        "users": [{"id": u.id, "name": u.name} for u in users],
        "models": [{"id": m.id, "name": m.name} for m in models_list],
        "predictions": [
            {
                "id": p.id,
                "user_id": p.user_id,
                "ai_model_id": p.ai_model_id,
                "probability": p.probability,
                "timestamp": p.timestamp.isoformat(),
            }
            for p in predictions
        ],
    }


def read_user(db: Session, user_name: str):
    """Read user by name."""
    return db.query(models.User).filter(models.User.name == user_name).first()


def read_model(db: Session, model_name: str):
    """Read model by name."""
    return db.query(models.AIModel).filter(models.AIModel.name == model_name).first()


# Update ---------------------------------------------------------------------------
def update_user(db: Session, user_id: int, new_name: str):
    """Update user name."""
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.name = new_name
        db.commit()
        db.refresh(user)
    return user


def update_model(db: Session, model_id: int, name: str):
    """Update AI model name."""
    model = db.query(models.AIModel).filter(models.AIModel.id == model_id).first()
    if model:
        model.name = name
        db.commit()
        db.refresh(model)
    return model


def update_prediction(db: Session, pred_id: int, probability: float):
    """Update prediction probability."""
    pred = db.query(models.Prediction).filter(models.Prediction.id == pred_id).first()
    if pred:
        pred.probability = probability
        db.commit()
        db.refresh(pred)
    return pred


# Delete ---------------------------------------------------------------------------
def delete_user(db: Session, user_id: int):
    """Delete user by ID."""
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


def delete_model(db: Session, model_id: int):
    """Delete AI model by ID."""
    model = db.query(models.AIModel).filter(models.AIModel.id == model_id).first()
    if model:
        db.delete(model)
        db.commit()
    return model


def delete_prediction(db: Session, pred_id: int):
    """Delete prediction by ID."""
    pred = db.query(models.Prediction).filter(models.Prediction.id == pred_id).first()
    if pred:
        db.delete(pred)
        db.commit()
    return pred
