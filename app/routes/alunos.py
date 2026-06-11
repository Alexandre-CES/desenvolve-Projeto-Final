from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import update
from sqlalchemy.orm import Session
from app.database.connection import get_session
from app.schemas.alunos import RegistrarAlunoSchema, AlterarNomeSchema, AlterarEmailSchema

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
  
  nome = session.query(Aluno).filter(Aluno.nome==registrar_aluno_schema.nome).first()
  if nome:
    raise HTTPException(status_code=400, detail=f'nome já está sendo usado')
  
  email = session.query(Aluno).filter(Aluno.email==registrar_aluno_schema.email).first()
  if email:
    raise HTTPException(status_code=400, detail=f'email já está sendo usado')
  
  novo_aluno = Aluno(registrar_aluno_schema.nome, registrar_aluno_schema.email)
  session.add(novo_aluno)
  session.commit()

  return{'message':'Aluno registrado com sucesso'}

  
#Read
@alunos_router.get('/listar_alunos')
async def listar_alunos(session = Depends(get_session)):
  
  alunos = session.query(Aluno).all()
  if not alunos:
    return{'message':'lista vazia'}
  else:
    return{
      'message':'alunos listados com sucesso',
      'alunos':alunos
    }
  
@alunos_router.get('/buscar_aluno')
async def buscar_aluno(aluno_id:int, session = Depends(get_session)):
  
  aluno = session.query(Aluno).filter(Aluno.id==aluno_id).first()
  if not aluno:
    raise HTTPException(status_code=400, detail=f'Aluno de id:{aluno_id} não existe')
  
  return{
    'message':'aluno retornado com sucesso',
    'aluno':aluno
  }

#Update 
@alunos_router.patch('/alterar_nome')
async def alterar_nome(
  aluno_id: int,
  alterarNomeSchema: AlterarNomeSchema,
  session = Depends(get_session)
):
  
  aluno = session.query(Aluno).filter(Aluno.id==aluno_id).first()
  if not aluno:
    raise HTTPException(status_code=400, detail=f'Aluno de id:{aluno_id} não existe')
  if aluno.nome == alterarNomeSchema.nome:
    raise HTTPException(status_code=400, detail=f'Novo nome não pode ser igual antigo')

  query = (
    update(Aluno)
    .where(Aluno.id==aluno_id)
    .values(nome=alterarNomeSchema.nome)
  )
  session.execute(query)
  session.commit()
  
  return{
    'message':'nome alterado com sucesso',
    'aluno':alterarNomeSchema.nome
  }
  
#Update 
@alunos_router.patch('/alterar_email')
async def alterar_email(
  aluno_id: int,
  alterarEmailSchema: AlterarEmailSchema,
  session = Depends(get_session)
):
  
  aluno = session.query(Aluno).filter(Aluno.id==aluno_id).first()
  if not aluno:
    raise HTTPException(status_code=400, detail=f'Aluno de id:{aluno_id} não existe')
  if aluno.email == alterarEmailSchema.email:
    raise HTTPException(status_code=400, detail=f'Novo email não pode ser igual antigo')
  
  query = (
    update(Aluno)
    .where(Aluno.id==aluno_id)
    .values(email=alterarEmailSchema.email)
  )
  session.execute(query)
  session.commit()
  
  return{
    'message':'email alterado com sucesso',
    'aluno':alterarEmailSchema.email
  }

@alunos_router.delete('/deletar_aluno', status_code=204)
async def deletar_aluno(aluno_id:int, session = Depends(get_session)):

  aluno = session.query(Aluno).filter(Aluno.id==aluno_id).first()
  if not aluno:
    raise HTTPException(status_code=400, detail=f'Aluno de id:{aluno_id} não existe')
  
  session.delete(aluno)
  session.commit()