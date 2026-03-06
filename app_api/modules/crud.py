from app_api.models import models
from sqlalchemy.orm import Session

# Create ----------------------------------------------------------------------------
def create_user(db: Session, name: str):
    """Create user.
    Args:"""
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

# Update ---------------------------------------------------------------------------
def update_user(db: Session, user_id: int, name: str):
    """Update user name."""
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.name = name
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
