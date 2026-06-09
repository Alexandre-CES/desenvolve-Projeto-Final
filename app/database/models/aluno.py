from database.connection import Base
from sqlalchemy import Column, Integer, String

class Aluno(Base):
  __tablename__ = 'alunos'

  id = Column('id',Integer, primary_key=True, autoincrement=True)
  nome = Column('nome', String, nullable=False)
  email = Column('nome', String, nullable=False)

  def __init__(self, nome, email):
    self.nome = nome
    self.email = email
    