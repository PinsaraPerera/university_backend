from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine
from app.api.endpoints import admin, student, authentication, faculty, subject, lecture, teacher

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(admin.router)
app.include_router(student.router)
app.include_router(faculty.router)
app.include_router(subject.router)
app.include_router(lecture.router)
app.include_router(teacher.router)
