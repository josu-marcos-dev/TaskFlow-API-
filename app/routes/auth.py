from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.auth import AuthResponse, AuthLogin
from app.services.security import create_access_token, hash_password, verify_password
from fastapi.security import OAuth2PasswordRequestForm #nisso aqui tb
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.user import User

router = APIRouter(prefix= "/auth", tags=["Auth"])

# Post /auth/login
@router.post("/login", response_model=AuthResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    
    user = (
        db.query(User)
        .filter(User.username == form_data.username)
        .first()
    )

    if not user or not verify_password(form_data.password, user.password): 
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
            )
        
    access_token = create_access_token(
        data = {"sub": user.email}
    )

    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }