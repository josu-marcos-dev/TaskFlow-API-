from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class CreateUser(UserBase):
    password: str

class UpdateUser(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class ResponseUser(UserBase):
    id: int
    creation_date: datetime
    model_config = {"from_attributes": True}

#schemas vão ser resposáveis por criar o user para você, a rota so conecta as coisas, 
#quando o cliente mandar uma solicitação de post, ele manda as infos e o schema padroniza e responde! 