from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Float, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from datetime import datetime
from typing import List



# Création de l'unité de contrôle --------------------------------------------------
engine = create_engine("sqlite:///mlops.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


# Classes --------------------------------------------------------------------------
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    
    predictions: Mapped[List["Prediction"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

class AIModel(Base):
    __tablename__ = "ai_model"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    predictions: Mapped[List["Prediction"]] = relationship(
        back_populates="model",
        cascade="all, delete-orphan"
    )

class Prediction(Base):
    __tablename__ = "prediction"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_account.id"),
        nullable=False
    )

    model_id: Mapped[int] = mapped_column(
        ForeignKey("ai_model.id"),
        nullable=False
    )

    probability: Mapped[float] = mapped_column(Float, nullable=False)

    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user: Mapped["User"] = relationship(back_populates="predictions")
    model: Mapped["AIModel"] = relationship(back_populates="predictions")


# III. Opérations CRUD et Jointures -------------------------------------------------
# 1. Create (Insertion)

with SessionLocal() as session:
    new_user = User(name="DataScientist_01")
    new_model = AIModel(name="EffectiveNet_V3", owner=new_user) # Liaison automatique
    
    session.add_all([new_user, new_model])
    session.commit() # Les données sont envoyées en base ici

with SessionLocal() as session:
    prediction = Prediction(
        user=new_user,
        model=new_model,
        probability=0.85
    )

    session.add(prediction)
    session.commit()

# 2. Read (Lecture et Jointures)

with SessionLocal() as session:
    stmt = select(AIModel).join(AIModel.owner).where(User.name == "Alice")
    models = session.scalars(stmt).all()


with SessionLocal() as session:
    stmt = select(User).options(selectinload(User.models))
    users = session.scalars(stmt).all()
# Les modèles sont déjà chargés en mémoire, pas de nouvelle requête SQL.

# 3. Update (Mise à jour)

with SessionLocal() as session:
    model = session.get(AIModel, 1) # Récupère le modèle avec l'ID 1
    model.name = "GPT-X-Turbo"
    session.commit()

# 4. Delete (Suppression)

with SessionLocal() as session:
    model_to_del = session.get(AIModel, 1)
    session.delete(model_to_del)
    session.commit()


stmt = (
    select(User.name, AIModel.name, Prediction.probability)
    .join(Prediction.user)
    .join(Prediction.model)
)

result = session.execute(stmt).all()

for row in result:
    print(row)