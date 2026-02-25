from fastapi import APIRouter, HTTPException, Depends
from app.schemas.create_user import CreateUser, UpdateUser, ResponseUser
from app.services.security import get_current_user
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.user import User
from app.services.security import hash_password

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/",
             response_model=ResponseUser,
             status_code=201
             )
def create_user(
                user: CreateUser,
                db: Session = Depends(get_db)):
    
    existing_user = (
        db.query(User)
        .filter(
            (User.username == user.username) |
            (User.email == user.email)
        )
        .first()
    )

    if existing_user: 
        raise HTTPException(
            status_code=409,
            detail="User already exists"
            )   
    
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/me",
            response_model=ResponseUser)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user



@router.put("/me",
            response_model=ResponseUser,
            status_code=200
            )
def modify_user(
                user: UpdateUser,
                db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user)
                ):
    
    existing_user = (
        db.query(User)
        .filter(User.id == current_user.id)
        .first()
    )

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
    )

    existing_user.username = user.username
    existing_user.email = user.email
    existing_user.password = hash_password(user.password)

    db.commit()
    db.refresh(existing_user)

    return existing_user



@router.delete("/me",
               status_code=204
               )
def delete_user(
                db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user)
                ):
    
    existing_user = (
        db.query(User)
        .filter(User.id == current_user.id)
        .first()
    )

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
    )

    db.delete(existing_user)
    db.commit()
