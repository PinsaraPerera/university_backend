from pydantic import BaseModel

class SubjectBase(BaseModel):
    subject_code: str
    subject_name: str
    degree: str
    year: int

class SubjectUpdate(BaseModel):
    subject_name: str
    degree: str
    year: int

