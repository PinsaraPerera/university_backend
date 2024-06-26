from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.subject import Subject

class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    faculty = Column(String)
    degree = Column(Integer)
    academic_year = Column(Integer)
    subject_code = Column(String, ForeignKey("subject.subject_code"))
    teacher_id = Column(Integer)
    day = Column(String)
    time_slot = Column(JSON)
    lecture_hall = Column(String)

    # Define the relationship to Subject
    subject = relationship("Subject")
