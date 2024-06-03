from pydantic import BaseModel

class FacultyBase(BaseModel):
    id: int
    name: str

class FacultyUpdate(BaseModel):
    name: str