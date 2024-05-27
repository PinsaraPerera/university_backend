from sqlalchemy.orm import Session
from app.models import student
from app.schemas import student_schema
from fastapi import HTTPException, status


def get_all(db: Session):
    students = db.query(student.Student).all()
    return students


def add(request: student_schema.Student, db: Session):
    student_exists = db.query(student.Student).filter(student.Student.student_no == request.student_no).first()
    if not student_exists:
        new_student = student.Student(
            student_no=request.student_no,
            student_name=request.student_name,
            degree_id=request.degree_id,
            specialization_id=request.specialization_id,
            email=request.email,
            faculty=request.faculty,
            department_id=request.department_id,
            image=request.image,
            starting_yr=request.starting_yr,
        )
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Student with student_no {request.student_no} already exists",
        )


def remove(student_no: str, db: Session):
    student = (
        db.query(student.Student)
        .filter(student.Student.student_no == student_no)
        .first()
    )
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with student_no {student_no} not found",
        )
    db.delete(student)
    db.commit()
    return "student removed"


def update(student_no: str, request: student_schema.Student, db: Session):

    student = (
        db.query(student.Student)
        .filter(student.Student.student_no == student_no)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with student_no {student_no} not found",
        )

    student.student_name = request.student_name
    student.degree_id = request.degree_id
    student.specialization_id = request.specialization_id
    student.email = request.email
    student.faculty = request.faculty
    student.department_id = request.department_id
    student.image = request.image
    student.starting_yr = request.starting_yr

    db.commit()
    db.refresh(student)
    return "student updated"


def show(student_no: str, db: Session):
    student = db.query(student.Student).filter(student.Student.student_no == student_no).first()
    
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with student_no {student_no} not found",
        )
    return student
