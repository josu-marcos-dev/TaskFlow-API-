from pydantic import BaseModel, EmailStr

class AuthBase(BaseModel):
    email: EmailStr
    password: str

class AuthLogin(AuthBase):
    pass

class AuthResponse(BaseModel): #note que esse é o único schema que o reponse usa basemodel e não herda a classe
    #isso é pq nesse caso, o pydantic deve ser reponsável por estruturar a response
    access_token: str
    token_type: str
    #mas para dar certo, no endpoint, no path do router vc deve adicionar: response_model=AuthResponse