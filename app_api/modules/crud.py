from app_api.models import models
from sqlalchemy.orm import Session


def create_user(db: Session, name: str):
    """Create user."""
    user = models.User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_model(db: Session, name: str):
    """Create model."""
    model = models.AIModel(name=name)
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

def create_prediction(db: Session, user_id: int, model_id: int, probability: float):
    """Create prediction."""
    pred = models.Prediction(
        user_id=user_id, ai_model_id=model_id, probability=probability)
    db.add(pred)
    db.commit()
    db.refresh(pred)
    return pred
