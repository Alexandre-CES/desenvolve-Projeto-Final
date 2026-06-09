from pydantic import BaseModel

class RegistrarAlunoSchema(BaseModel):
  nome: str
  email: str

  class Config:
    from_attributes = True