from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import student_schema, admin_schema
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.utils import oauth2
from app.crud import student

router = APIRouter(
    prefix="/student",
    tags=["Students"],
)


@router.get("/getAll", response_model=List[student_schema.Student])
def all(
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return student.get_all(db)


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create(
    request: student_schema.Student,
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return student.add(request, db)


@router.delete("/remove/{student_no}", status_code=status.HTTP_204_NO_CONTENT)
def remove(
    student_no: str,
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return student.remove(student_no, db)


@router.put("/update/{student_no}", status_code=status.HTTP_202_ACCEPTED)
def update(
    student_no: str,
    request: student_schema.Student,
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return student.update(student_no, request, db)


@router.get("/{student_no}", response_model=student_schema.Student)
def get_student(
    student_no: str,
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return student.show(student_no, db)
