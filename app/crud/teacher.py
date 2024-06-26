from sqlalchemy.orm import Session
from app.models import teacher
from app.schemas import teacher_schema
from fastapi import HTTPException, status


def get_all(db: Session):
    teachers = db.query(teacher.Teacher).all()
    return teachers


def add(request: teacher_schema.TeacherBase, db: Session):
    teacher_exists = (
        db.query(teacher.Teacher).filter(teacher.Teacher.email == request.email).first()
    )
    if not teacher_exists:
        new_teacher = teacher.Teacher(
            name=request.name,
            email=request.email,
            department=request.department,
        )
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        return new_teacher
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Teacher with email {request.email} already exists",
        )


def remove(teacher_id: int, db: Session):
    result = db.query(teacher.Teacher).filter(teacher.Teacher.id == teacher_id).first()
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Teacher with id {teacher_id} not found",
        )
    db.delete(result)
    db.commit()
    return "teacher removed"


def update(teacher_id: int, request: teacher_schema.TeacherBase, db: Session):

    result = db.query(teacher.Teacher).filter(teacher.Teacher.id == teacher_id).first()

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Teacher with id {teacher_id} not found",
        )

    result.name = request.name
    result.email = request.email
    result.department = request.department

    db.commit()
    db.refresh(result)
    return result

def show(teacher_id: int, db: Session):
    result = db.query(teacher.Teacher).filter(teacher.Teacher.id == teacher_id).first()
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Teacher with id {teacher_id} not found",
        )
    return result
