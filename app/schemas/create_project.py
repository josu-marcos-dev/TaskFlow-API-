from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None #o usuario pode colocar uma string como descrição, ou nada, ambos são aceitáveis!


class CreateProject(ProjectBase):
    pass

class UpdateProject(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ResponseProject(ProjectBase):
    project_id: int
    owner_id: int
    creation_date: datetime

    model_config = {"from_attributes": True}

#o pydantic serve para vc padronizar a entrada dos usuários, as responses da sua api, gerar mensagens de erro, criar jsons e muito mais
#basemodel e bem poderoso
