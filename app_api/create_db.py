from models import models
from modules.connect import Base, engine

Base.metadata.create_all(bind=engine)
print("Database created!")
