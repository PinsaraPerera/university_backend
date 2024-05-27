from typing import List, Optional
from pydantic import BaseModel

class StudentBase(BaseModel):
    student_no: str
    student_name: str
    degree_id: int
    specialization_id: int
    email: str
    faculty: int
    department_id: int
    image: str
    starting_yr: int

class Student(StudentBase):
    class Config:
        from_attributes = True