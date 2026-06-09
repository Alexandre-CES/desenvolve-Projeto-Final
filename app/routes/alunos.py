from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_session
from app.schemas import RegistrarAlunoSchema

from app.database.models.aluno import Aluno

alunos_router = APIRouter(prefix='/alunos', tags=['alunos'])

@alunos_router.get('/')
async def alunos():
  return{'message':'rota de alunos'}

#Create
@alunos_router.post('/registrar_aluno', status_code=201)
async def registrar_aluno(
  registrar_aluno_schema: RegistrarAlunoSchema,
  session: Session = Depends(get_session)
):
  try:
    email = session.query(Aluno).filter(Aluno.email==registrar_aluno_schema.email).first()
    if email:
      raise HTTPException(status_code=400, detail=f'email já está sendo usado')
    
    novo_aluno = Aluno(registrar_aluno_schema.nome, registrar_aluno_schema.email)
    session.add(novo_aluno)
    session.commit()

    return{'message':'Aluno registrado com sucesso'}
  
  except Exception as e:
    raise HTTPException(status_code=500, detail=f'algo deu errado!: {e}')