from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from app_api.modules.connect import Base
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    """Represents a user in the database."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)

    predictions: Mapped[List["Prediction"]] = relationship(
        "Prediction", back_populates="user"
    )


class AIModel(Base):
    """Represents an AI model in the database."""

    __tablename__ = "aimodels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)

    predictions: Mapped[List["Prediction"]] = relationship(
        "Prediction", back_populates="aimodel"
    )


class Prediction(Base):
    """Represents a prediction made by a model for a user."""

    __tablename__ = "predictions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    ai_model_id: Mapped[int] = mapped_column(Integer, ForeignKey("aimodels.id"))
    probability: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped[Optional[User]] = relationship("User", back_populates="predictions")
    aimodel: Mapped[Optional[AIModel]] = relationship(
        "AIModel", back_populates="predictions"
    )
