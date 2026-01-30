from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.database.session import get_db
from app.models.user import User
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 
#padrão de api

def create_access_token(data: dict): 
#ela vai recebr data que vai ser um dicionário

    to_encode = data.copy() 
    #vai usar copy() para gerar uma copia do data e colocar em to_encode

    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    #estamos criando o tempo de validade do token, que vai ser o horário atual + access_token_expire_time

    to_encode.update({"exp" : expire})
    #vai adicionar o campo "exp" c o valor de expire no dict copiado 

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    #aqui rola a criação do token, onde ele vai mesclar o dict de entrada, tempo limite, master secret key e algorithm
    #para criar uma string que vai ser o token! tipo isso: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
    
    return encoded_jwt #retorna o token criado! 


def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        #pega o token e desseca ele

        email: str | None = payload.get("sub") #pega o email se tiver

        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail= "invalid token"
                )

    except JWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail= "invalid or expired token"
                )
    
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=401)

    return user #entender melhor depois 