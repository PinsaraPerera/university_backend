from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Student(Base):
    __tablename__ = "students"
    
    student_no = Column(String, primary_key=True, index=True)
    student_name = Column(String)
    degree_id = Column(Integer)
    specialization_id = Column(Integer)
    email = Column(String, unique=True, index=True)
    faculty = Column(Integer)
    department_id = Column(Integer)
    image = Column(String)
    starting_yr = Column(Integer)
    