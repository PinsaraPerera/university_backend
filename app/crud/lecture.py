from sqlalchemy.orm import Session
from app.models import lecture
from app.schemas import lecture_schema
from fastapi import HTTPException, status


def get_all(db: Session):
    lectures = db.query(lecture.Lecture).all()
    return lectures


def create(request: lecture_schema.LectureBase, db: Session):
    new_lecture = lecture.Lecture(
        faculty=request.faculty,
        degree=request.degree,
        academic_year=request.academic_year,
        subject_code=request.subject_code,
        teacher_id=request.teacher_id,
        day=request.day,
        time_slot={
            "start_time": request.time_slot.start_time,
            "end_time": request.time_slot.end_time,
        },
        lecture_hall=request.lecture_hall,
    )
    db.add(new_lecture)
    db.commit()
    db.refresh(new_lecture)
    return new_lecture


def remove(lecture_id: int, db: Session):
    result = db.query(lecture.Lecture).filter(lecture.Lecture.id == lecture_id).first()
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lecture with id {lecture_id} not found",
        )
    db.delete(result)
    db.commit()
    return "lecture removed"


def update(lecture_id: int, request: lecture_schema.LectureUpdate, db: Session):
    result = db.query(lecture.Lecture).filter(lecture.Lecture.id == lecture_id).first()
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lecture with id {lecture_id} not found",
        )
    result.faculty = request.faculty
    result.degree = request.degree
    result.academic_year = request.academic_year
    result.subject_code = request.subject_code
    result.teacher_id = request.teacher_id
    result.day = request.day
    result.time_slot = {
        "start_time": request.time_slot.start_time,
        "end_time": request.time_slot.end_time
    }
    result.lecture_hall = request.lecture_hall
    db.commit()
    db.refresh(result)
    return result


def get_by_day(day: str, db: Session):
    result = db.query(lecture.Lecture).filter(lecture.Lecture.day == day).all()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lecture with day {day} not found",
        )

    return result


def get_by_teacher(teacher_id: int, db: Session):
    result = (
        db.query(lecture.Lecture).filter(lecture.Lecture.teacher_id == 1).all()
    )

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lecture with teacher_id {teacher_id} not found",
        )

    return result


def get_by_degree(degree: int, db: Session):
    result = db.query(lecture.Lecture).filter(lecture.Lecture.degree == degree).all()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lecture with degree {degree} not found",
        )

    return result


def get_by_academic_year(academic_year: int, db: Session):
    result = (
        db.query(lecture.Lecture)
        .filter(lecture.Lecture.academic_year == academic_year)
        .all()
    )

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lecture with academic_year {academic_year} not found",
        )

    return result
