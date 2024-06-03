from sqlalchemy.orm import Session
from app.models import faculty
from app.schemas import faculty_schema
from fastapi import HTTPException, status

def get_all(db: Session):
    faculties = db.query(faculty.Faculty).all()
    return faculties

def create(request: faculty_schema.FacultyBase, db: Session):
    faculty_exists = db.query(faculty.Faculty).filter(faculty.Faculty.name == request.name).first()
    if not faculty_exists:
        new_faculty = faculty.Faculty(
            id=request.id,
            name=request.name,
        )
        db.add(new_faculty)
        db.commit()
        db.refresh(new_faculty)
        return new_faculty
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Faculty with faculty_name {request.name} already exists",
        )

def remove(faculty_id: int, db: Session):
    result = (
        db.query(faculty.Faculty)
        .filter(faculty.Faculty.id == faculty_id)
        .first()
    )
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Faculty with faculty_id {faculty_id} not found",
        )
    db.delete(result)
    db.commit()
    return "faculty removed"

def update(faculty_id: int, request: faculty_schema.FacultyUpdate, db: Session):
    result = (
        db.query(faculty.Faculty)
        .filter(faculty.Faculty.id == faculty_id)
        .first()
    )
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Faculty with faculty_id {faculty_id} not found",
        )

    result.name = request.name

    db.commit()
    db.refresh(result)
    return "faculty updated"