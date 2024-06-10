from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import subject_schema, admin_schema
from app.db.session import get_db
from sqlalchemy.orm import Session
import app.crud.subject as subject
from app.utils import oauth2


router = APIRouter(
    prefix="/subject",
    tags=["Subject"],
)


@router.post(
    "/create",
    response_model=subject_schema.SubjectBase,
    status_code=status.HTTP_201_CREATED,
)
def create_subject(request: subject_schema.SubjectBase, db: Session = Depends(get_db)):
    return subject.create(request, db)


@router.get("/getAll", response_model=List[subject_schema.SubjectBase])
def all(db: Session = Depends(get_db)):
    return subject.get_all(db)


@router.delete("/delete/{subject_code}", status_code=status.HTTP_204_NO_CONTENT)
def remove(
    subject_code: str,
    db: Session = Depends(get_db),
    current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return subject.remove(subject_code, db)


@router.put("/update/{subject_code}", status_code=status.HTTP_202_ACCEPTED)
def update(
    subject_code: str,
    request: subject_schema.SubjectUpdate,
    db: Session = Depends(get_db),
    current_user: admin_schema.Admin = Depends(oauth2.get_current_user),
):
    return subject.update(subject_code, request, db)


@router.get("/get/{subject_code}", response_model=subject_schema.SubjectBase)
def get(subject_code: str, db: Session = Depends(get_db)):
    return subject.get_subject(subject_code, db)
