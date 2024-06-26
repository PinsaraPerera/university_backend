from pydantic import BaseModel, Field


class TeacherBase(BaseModel):
    name: str
    email: str
    department: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "sample@gmail.com",
                "department": "Computer Science",
            }
        }


class TeacherResponse(TeacherBase):
    id: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "email": "sample@gmail.com",
                "department": "Computer Science",
            }
        }
