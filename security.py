# security.py

from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
#from . import schemas
from schemas import UserCreate, Token
from crud import get_user_by_username

# 비밀번호 해싱을 위한 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT 토큰을 위한 SECRET_KEY와 알고리즘을 정의합니다.
SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Pydantic의 User 모델을 사용하여 사용자의 인증 정보를 표현하는 함수가 필요합니다.
# 예를 들어:
def authenticate_user(username: str, password: str, db: Session):
    user = get_user_by_username(db, username=username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
