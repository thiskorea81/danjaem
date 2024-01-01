# routers/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
#from .. import crud, models, schemas, security, dependencies
# 상대 임포트를 절대 임포트로 변경
#from ..crud import crud
#from ..models import models
#from ..schemas import schemas
#from ..security import security
#from ..dependencies import dependencies
from crud import create_user, get_user_by_username  # 절대 임포트 사용
from models import User
from schemas import UserCreate, Token
from security import verify_password, create_access_token, authenticate_user
from dependencies import get_db
router = APIRouter()

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
