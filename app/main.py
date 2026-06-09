
'''
  #! Manter importação do dotenv no topo, ao menos antes de qualquer "from app.database.connection"
  #?Using dotenv: 
    import os
    os.getenv("VARIABLE")
'''
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routes.alunos import alunos_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(alunos_router)

@app.get('/')
async def home():
  return {
    'message': 'Hello World!'
  }
