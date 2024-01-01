# schemas.py

from pydantic import BaseModel
from typing import Optional

#  사용자 인증 토큰을 나타내는 Pydantic 모델
class Token(BaseModel):
    access_token: str
    token_type: str

# 사용자 인증 토큰의 데이터를 검증하기 위한 Pydantic 모델
class TokenData(BaseModel):
    username: str | None = None

# User 스키마
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: Optional[bool] = True

    class Config:
        from_attributes = True

# Course 스키마
class CourseBase(BaseModel):
    code: str
    title: str

class CourseCreate(CourseBase):
    teacher_id: int
    credits: int
    capacity: int
    prerequisites: Optional[str] = None

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True

# Teacher 스키마
class TeacherBase(BaseModel):
    name: str
    phone_number: str
    email: str
    department: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int

    class Config:
        from_attributes = True
