import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL) #“SQLAlchemy, essa é a porta pra falar com o banco”

SessionLocal = sessionmaker(
    autocommit=False, #salvamento não automático
    autoflush=False, #evita comportamento automático de manipulação
    bind=engine #usa aquela porta criada
)

def get_db():
    db = SessionLocal() #abre sessão de conexão com banco
    try:
        yield db #entrega conexão pro endpoint
    finally: 
        db.close() #fecha conexão no fim da request

#esse arquivo por padrão sempre guarda:
#1. URL do banco --> string mais a baixo
#2. Engine (porta de entrada)
#3. SessionLocal (sessões de uso)

#engine é tipo a porta de entrada né, e tipo o a linha telefonica e sessionlocal vai ser a chamada

#FastAPI lida com python, PostgreSQL lida com SQL, como comunicar e conectar ambos? 
#tradutor: SQLAlchemy!

#vamos gerar endereço de conexão do banco com fastapi -> apenas sinaliza onde ta o DB
#string:  "postgresql://user:password@localhost:5432/taskflow"
#aqui temos respectivamente: tipo de banco > usuário > senha > onde roda > porta(padrão) > nome do banco