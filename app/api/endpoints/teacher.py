from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import teacher_schema, admin_schema
from app.db.session import get_db
from sqlalchemy.orm import Session
import app.crud.teacher as teacher
from app.utils import oauth2

router = APIRouter(
    prefix="/teacher",
    tags=["Teacher"],
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create(
    request: teacher_schema.TeacherBase,
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return teacher.add(request, db)

@router.get("/getAll", response_model=List[teacher_schema.TeacherResponse])
def all(
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return teacher.get_all(db)

@router.get("/{teacher_id}", response_model=teacher_schema.TeacherResponse)
def get_teacher(
    teacher_id: int,
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return teacher.show(teacher_id, db)

@router.put("/update/{teacher_id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    teacher_id: int,
    request: teacher_schema.TeacherBase,
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return teacher.update(teacher_id, request, db)

@router.delete("/remove/{teacher_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(
    teacher_id: int,
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return teacher.remove(teacher_id, db)