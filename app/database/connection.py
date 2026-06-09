from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Base = declarative_base()

#session config
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#Open and close session
'''
    #? how to use:

    from sqlalchemy.orm import Session
    from database.connection import get_session

    session : Session = Depends(get_session)

    aluno = session.query()
'''
def get_session():
  try:
    session = SessionLocal()
    yield session
  finally:
    session.close()