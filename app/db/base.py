from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.models.student import Student
from app.models.admin import Admin
