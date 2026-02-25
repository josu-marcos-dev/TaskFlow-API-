from fastapi import APIRouter, HTTPException, Depends
from app.schemas.create_task import CreateTask, ResponseTask, UpdateTask
from app.services.security import get_current_user
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.task import Task
from app.models.project import Project
from app.models.user import User


router = APIRouter(prefix= "/projects", tags=["Tasks"])

#o post converte objeto pydantic para dict, e importante que ele receba apenas os campos que o schemas permite!

@router.post("/{project_id}/tasks",
             response_model= ResponseTask,
             status_code=201) #path certinho
def create_new_task(project_id: int, #pega o id do projeto para conectar
                    task: CreateTask, #depende do schemas de task para receber dados
                    db: Session = Depends(get_db), #depende de get_db para ligar endpoint com db
                    current_user: User = Depends(get_current_user)): #auth
    
    #verifica autorização para mexer na task
    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id
        )
        .first()
    )

    if not project: #se não tiver autorização, é barrado!
        raise HTTPException(403, "Not your project")
    
    #verifica se a task em si ja existe
    existing_task = ( #query nada mais é doque uma pergunta ao db
        db.query(Task) #local: no DB na tabela task
        .filter(
            Task.title == task.title, #vai filtrar por task title e task project_id 
            Task.project_id == project_id
            )
        .first() #pega a primeira ou nenhuma!
        )#pergunta "uma task com esse titulo, e desse, projeto existe no db?"

    if existing_task: #se a query estiver correta, manda erro, se não, prossegue!
        raise HTTPException(
            status_code=409,
            detail="Task already exists in this project"
            )
    #query para verificação, todas seguem: local + filtros + quantidade + erro caso não de certo

    #se não, cria uma nova task
    new_task = Task(
        title=task.title,
        description=task.description, 
        priority=task.priority,
        status=task.status,
        project_id=project_id,
    )

    #adiciona, e salva no db
    db.add(new_task) #coloca na transação
    db.commit() #salva de vez
    db.refresh(new_task) #atualiza id, data, etc
    #combo que substitui append.lista de fake dados (lista de dados hard coded na versão antiga)

    #retorna o resultado final
    return new_task 



@router.get("/{project_id}/tasks", 
            response_model=list[ResponseTask], 
            status_code=200
            )  
def get_all_tasks(project_id: int,
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)
                   ):
    
    #verifica autorização para mexer na task
    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id
        )
        .first()
    )

    if not project:
        raise HTTPException(403, "Not your project")
    
    all_tasks = (
        db.query(Task)
        .filter(
            Task.project_id == project_id
        )
        .all()
    )

    return all_tasks



@router.get("/{project_id}/tasks/{task_id}",
            response_model= ResponseTask, 
            status_code=200)
def get_task_by_id(project_id: int,
                   task_id: int,
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    
    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id
        )
        .first()
    )

    if not project: 
        raise HTTPException(403, "Not your project")
     
    existing_task = ( 
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.project_id == project_id
            )
        .first() 
        )
     
    if not existing_task: 
        raise HTTPException(
            status_code=404,
            detail="Task not found"
            )
     
    return existing_task



@router.put("/{project_id}/tasks/{task_id}",
             response_model= UpdateTask,
             status_code=200)
def modify_task(project_id: int,
                task_id: int,
                task: UpdateTask,
                db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user)
                ):
    
    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id
        )
        .first()
    )

    if not project: 
        raise HTTPException(403, "Not your project")

    existing_task = ( 
        db.query(Task) 
        .filter(
            Task.id == task_id,
            Task.project_id == project_id
            )
        .first() 
        )
    
    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
    )
    
    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.priority = task.priority
    existing_task.status = task.status

    db.commit() 
    db.refresh(existing_task) 

    return existing_task



@router.delete("/{project_id}/tasks/{task_id}",
               status_code=204)
def delete_task(project_id: int,
                task_id: int,
                db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user)
                ):
    
    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id
        )
        .first()
    )

    if not project: 
        raise HTTPException(403, "Not your project")

    existing_task = ( 
        db.query(Task) 
        .filter(
            Task.id == task_id,
            Task.project_id == project_id
            )
        .first()
        )
    
    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
    )

    db.delete(existing_task)
    db.commit()