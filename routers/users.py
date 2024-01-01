# routers/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
#from .. import crud, models, schemas, dependencies
# 상대 임포트를 절대 임포트로 변경
from crud import create_user, get_user_by_username, get_user
from schemas import User, UserCreate
from dependencies import get_db

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)

@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_user(db, skip=skip, limit=limit)
    return users
