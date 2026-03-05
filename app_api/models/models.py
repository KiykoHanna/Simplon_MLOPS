from datetime import datetime

from app_api.modules.connect import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    """Represents a user in the database."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    predictions = relationship("Prediction", back_populates="user")


class AIModel(Base):
    """Represents an AI model in the database."""

    __tablename__ = "aimodels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    predictions = relationship("Prediction", back_populates="aimodel")


class Prediction(Base):
    """Represents a prediction made by a model for a user."""

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ai_model_id = Column(Integer, ForeignKey("aimodels.id"))
    probability = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="predictions")
    aimodel = relationship("AIModel", back_populates="predictions")
