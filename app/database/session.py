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

