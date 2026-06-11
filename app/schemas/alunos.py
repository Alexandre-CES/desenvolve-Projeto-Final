from pydantic import BaseModel

class RegistrarAlunoSchema(BaseModel):
  nome: str
  email: str

  class Config:
    from_attributes = True

class AlterarNomeSchema(BaseModel):
  nome: str

  class Config:
    from_attributes = True

class AlterarEmailSchema(BaseModel):
  email: str

  class Config:
    from_attributes = True