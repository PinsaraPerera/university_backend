from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import faculty_schema, admin_schema
from app.db.session import get_db
from sqlalchemy.orm import Session
import app.crud.faculty as faculty
from app.utils import oauth2


router = APIRouter(
    prefix="/faculty",
    tags=["Faculty"],
)


@router.post(
    "/create",
    response_model=faculty_schema.FacultyBase,
    status_code=status.HTTP_201_CREATED,
)
def create_faculty(
    request: faculty_schema.FacultyBase,
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends(),
):
    return faculty.create(request, db)


@router.get("/getAll", response_model=List[faculty_schema.FacultyBase])
def all(
    db: Session = Depends(get_db),
    # current_user: admin_schema.Admin = Depends()
):
    return faculty.get_all(db)


@router.delete("/delete/{faculty_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(
    faculty_id: int,
    db: Session = Depends(get_db),
    current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return faculty.remove(faculty_id, db)


@router.put("/update/{faculty_id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    faculty_id: int,
    request: faculty_schema.FacultyUpdate,
    db: Session = Depends(get_db),
    current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return faculty.update(faculty_id, request, db)
