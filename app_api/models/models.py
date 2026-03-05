from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app_api.modules.connect import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    predictions = relationship("Prediction", back_populates="user")


class AIModel(Base):
    __tablename__ = "aimodels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    predictions = relationship("Prediction", back_populates="aimodel")


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ai_model_id = Column(Integer, ForeignKey("aimodels.id"))
    probability = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="predictions")
    aimodel = relationship("AIModel", back_populates="predictions")
