from pydantic import BaseModel, Field
from .subject_schema import SubjectBase

class TimeSlot(BaseModel):
    start_time: str
    end_time: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "start_time": "08:00",
                "end_time": "10:00"
            }
        }

class LectureBase(BaseModel):
    faculty: str
    degree: int
    academic_year: int
    subject_code: str
    teacher_id: int
    day: str
    time_slot: TimeSlot
    lecture_hall: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "faculty": "Engineering",
                "degree": 1,
                "academic_year": 2,
                "subject_code": "CSCI22012",
                "teacher_id": 1,
                "day": "Monday",
                "time_slot": {"start_time": "08:00", "end_time": "10:00"},
                "lecture_hall": "A-101"
            }
        }

class LectureUpdate(BaseModel):
    faculty: str
    degree: int
    academic_year: int
    subject_code: str
    teacher_id: int
    day: str
    time_slot: TimeSlot
    lecture_hall: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "faculty": "Engineering",
                "degree": 1,
                "academic_year": 2,
                "subject_code": "CSCI22012",
                "teacher_id": 1,
                "day": "Monday",
                "time_slot": {"start_time": "08:00", "end_time": "10:00"},
                "lecture_hall": "A-101"
            }
        }


class LectureResponse(BaseModel):# response from the database
    id: int
    faculty: str
    degree: int
    academic_year: int
    subject_code: str
    teacher_id: int
    day: str
    time_slot: TimeSlot
    lecture_hall: str
    subject: SubjectBase  # Nested SubjectBase model

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "faculty": "Science",
                "degree": 1,
                "academic_year": 2,
                "subject_code": "CS101",
                "teacher_id": 1,
                "time_slot": {"start_time": "09:00", "end_time": "10:00"},
                "lecture_hall": "Room 101",
                "subject": {
                    "subject_code": "CS101",
                    "subject_name": "Computer Science 101",
                    "degree": "B.Sc.",
                    "year": 2024
                }
            }
        }