from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")

db = create_engine(DATABASE_URL)
Base = declarative_base()

