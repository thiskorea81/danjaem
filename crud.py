# crud.py

from sqlalchemy.orm import Session
#from . import models, schemas
# 상대 임포트를 절대 임포트로 변경
from models import User, Course, Teacher  # 모델 클래스 직접 임포트
from schemas import UserCreate, CourseCreate, TeacherCreate  # 스키마도 필요에 따라 임포트

# User CRUD operations
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Course CRUD operations
def get_course(db: Session, course_code: str):
    return db.query(Course).filter(Course.code == course_code).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: CourseCreate):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# Teacher CRUD operations
def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()

def get_teachers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Teacher).offset(skip).limit(limit).all()

def create_teacher(db: Session, teacher: TeacherCreate):
    db_teacher = Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

# ... (나머지 CRUD 연산)
