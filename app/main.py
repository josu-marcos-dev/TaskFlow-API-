from fastapi import FastAPI
from app.database.session import engine
from app.database.base import Base
from app.routes import project as project_routes, task as task_routes, user as user_routes, auth
from app.models import project, task, user


app = FastAPI()

app.include_router(project_routes.router, prefix="/api")
app.include_router(task_routes.router, prefix="/api")
app.include_router(user_routes.router, prefix="/api")
app.include_router(auth.router, prefix="/api")

@app.get("/")
async def root():
    return {"status": "TaskFlow API rodando"}

Base.metadata.create_all(bind=engine) #cria todas as tabelas