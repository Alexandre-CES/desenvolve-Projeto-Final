from app.database.connection import Base
from sqlalchemy import Column, Integer, String

class Aluno(Base):
  __tablename__ = 'alunos'

  id = Column('id',Integer, primary_key=True, autoincrement=True)
  nome = Column('nome', String(100), nullable=False)
  email = Column('email', String(100), nullable=False)

  def __init__(self, nome, email):
    self.nome = nome
    self.email = email
    