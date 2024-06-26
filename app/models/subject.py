from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Subject(Base):
    __tablename__ = "subject"

    subject_code = Column(String, primary_key=True, index=True)
    subject_name = Column(String)
    degree = Column(String)
    year = Column(Integer)

