from app.database.connection import Base
from sqlalchemy import Column, Integer, String

class Curso(Base):
  __tablename__ = 'cursos'

  id = Column('id',Integer, primary_key=True, autoincrement=True)
  titulo = Column('titulo', String(50), nullable=False)
  

  def __init__(self, titulo):
    self.titulo = titulo
    