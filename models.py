# models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Course(Base):
    __tablename__ = "courses"

    code = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    credits = Column(Integer)
    capacity = Column(Integer)
    prerequisites = Column(String)

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    department = Column(String)
