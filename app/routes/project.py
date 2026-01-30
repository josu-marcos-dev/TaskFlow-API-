from fastapi import APIRouter, HTTPException, Depends
from app.schemas.create_project import CreateProject, ResponseProject, UpdateProject
from app.services.security import get_current_user
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.project import Project
from app.models.user import User

router = APIRouter(tags=["Projects"])

@router.post("/users/{user_id}/projects",
             response_model= ResponseProject,
             status_code=201
             )
def create_project(user_id: int,
                   project: CreateProject, 
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)
                   ):
    
    if user_id != current_user.id:
        raise HTTPException(403, "Not your user")

    existing_project = (
        db.query(Project)
        .filter(
            Project.title == project.title,
            Project.owner_id == current_user.id
        )
        .first()
    )

    if existing_project: #se a query estiver correta, manda erro, se não, prossegue!
        raise HTTPException(
            status_code=409,
            detail="Project already exists"
            )

    new_project = Project(
        title=project.title,
        description=project.description,
        owner_id=user_id
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project
#ver se os campos de criação estão corretos com base no schemas (gpto)



@router.get("/users/{user_id}/projects",
            response_model= list[ResponseProject],
            status_code=200
            )
def get_all_user_projects(
                     user_id: int,
                     db: Session = Depends(get_db),
                     current_user: User = Depends(get_current_user)
                     ):
    
    if user_id != current_user.id:
        raise HTTPException(
            detail= "Not your user",
            status_code=403
        )

    all_projects = (
        db.query(Project)
        .filter(
            Project.owner_id == current_user.id
        )
        .all()
    )

    return all_projects



@router.put("/users/{user_id}/projects/{project_id}",
            response_model=UpdateProject,
            status_code=200
            )
def modify_project(project_id: int, 
                   user_id:int,
                   project: UpdateProject,
                   db: Session = Depends(get_db),  
                   current_user: User = Depends(get_current_user)
                   ):
    
    if user_id != current_user.id:
        raise HTTPException(
            detail= "Not your user",
            status_code=403
        )
    
    existing_project = ( 
        db.query(Project) 
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id
            )
        .first() 
        )
        
    if not existing_project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
    )

    existing_project.title = project.title
    existing_project.description = project.description

    db.commit() #salva de vez
    db.refresh(existing_project) #atualiza id, data, etc

    return existing_project




@router.delete("/users/{user_id}/projects/{project_id}",
               status_code=204
               )
def delete_project(user_id: int,
                   project_id: int,
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)
                   ):
    
    if user_id != current_user.id:
        raise HTTPException(
            detail= "Not your user",
            status_code=403
        )

    existing_project = ( 
        db.query(Project) 
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id
            )
        .first() 
        )
        
    if not existing_project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
    )

    db.delete(existing_project)
    db.commit()

