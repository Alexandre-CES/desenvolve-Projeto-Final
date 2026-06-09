from app.database.connection import Base
from sqlalchemy import Column, Integer, ForeignKey

class Curso(Base):
  __tablename__ = 'matriculas'

  id = Column('id',Integer, primary_key=True, autoincrement=True)
  aluno_id = Column('aluno_id',Integer, ForeignKey('alunos.id'), nullable=False)
  curso_id = Column('curso_id',Integer, ForeignKey('cursos.id'), nullable=False)
  

  def __init__(self, aluno_id, curso_id):
    self.aluno_id = aluno_id
    self.curso_id = curso_id