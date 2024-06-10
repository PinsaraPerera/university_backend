from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import lecture_schema, admin_schema
from app.db.session import get_db
from sqlalchemy.orm import Session
import app.crud.lecture as lecture
from app.utils import oauth2

router = APIRouter(
    prefix="/lecture",
    tags=["Lecture"],
)

@router.post("/create", response_model=lecture_schema.LectureBase, status_code=status.HTTP_201_CREATED)
def create_lecture(request: lecture_schema.LectureBase, db: Session = Depends(get_db)):
    return lecture.create(request, db)

@router.get("/getAll", response_model=List[lecture_schema.LectureResponse])
def all(db: Session = Depends(get_db)):
    return lecture.get_all(db)

@router.delete("/delete/{lecture_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(lecture_id: int, db: Session = Depends(get_db), current_user: admin_schema.Admin = Depends(oauth2.get_current_user)):
    return lecture.remove(lecture_id, db)

@router.put("/update/{lecture_id}", status_code=status.HTTP_202_ACCEPTED)
def update(lecture_id: int, request: lecture_schema.LectureUpdate, db: Session = Depends(get_db), current_user: admin_schema.Admin = Depends(oauth2.get_current_user)):
    return lecture.update(lecture_id, request, db)

@router.get("/getDay/{day}", response_model=List[lecture_schema.LectureResponse])
def get_by_day(day: str, db: Session = Depends(get_db)):
    return lecture.get_by_day(day, db)

@router.get("/getTeacher/{teacher_id}", response_model=List[lecture_schema.LectureResponse])
def get_by_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return lecture.get_by_teacher(teacher_id, db)

@router.get("/getDegree/{degree_id}", response_model=List[lecture_schema.LectureResponse])
def get_by_degree(degree_id: int, db: Session = Depends(get_db)):
    return lecture.get_by_degree(degree_id, db)

@router.get("/getYear/{academic_year}", response_model=List[lecture_schema.LectureResponse])
def get_by_academic_year(academic_year: int, db: Session = Depends(get_db)):
    return lecture.get_by_academic_year(academic_year, db)