from sqlalchemy.orm import Session
from app.models import subject
from app.schemas import subject_schema
from fastapi import HTTPException, status


def get_all(db: Session):
    subjects = db.query(subject.Subject).all()
    return subjects


def create(request: subject_schema.SubjectBase, db: Session):
    subject_exists = (
        db.query(subject.Subject)
        .filter(subject.Subject.subject_code == request.subject_code)
        .first()
    )
    if not subject_exists:
        new_subject = subject.Subject(
            subject_code=request.subject_code,
            subject_name=request.subject_name,
            degree=request.degree,
            year=request.year,
        )
        db.add(new_subject)
        db.commit()
        db.refresh(new_subject)
        return new_subject
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Subject with subject_code {request.subject_code} already exists",
        )


def remove(subject_code: str, db: Session):
    result = (
        db.query(subject.Subject)
        .filter(subject.Subject.subject_code == subject_code)
        .first()
    )
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Subject with subject_code {subject_code} not found",
        )
    db.delete(result)
    db.commit()
    return "subject removed"


def update(subject_code: str, request: subject_schema.SubjectUpdate, db: Session):
    result = (
        db.query(subject.Subject)
        .filter(subject.Subject.subject_code == subject_code)
        .first()
    )
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Subject with subject_code {subject_code} not found",
        )

    result.subject_name = request.subject_name
    result.degree = request.degree
    result.year = request.year

    db.commit()
    db.refresh(result)
    return "subject updated"

def get_subject(subject_code: str, db: Session):
    result = (
        db.query(subject.Subject)
        .filter(subject.Subject.subject_code == subject_code)
        .first()
    )
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Subject with subject_code {subject_code} not found",
        )
    return result
