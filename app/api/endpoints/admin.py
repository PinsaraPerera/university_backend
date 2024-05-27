from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import admin_schema
from app.db.session import get_db
from sqlalchemy.orm import Session
import app.crud.admin as admin


router = APIRouter(
    prefix="/admin",
    tags=["Admins"],
)


@router.post("/", response_model=admin_schema.Admin)
def create_admin(request: admin_schema.AdminBase, db: Session = Depends(get_db)):
    return admin.create(request, db)


@router.get("/{id}", response_model=admin_schema.Admin)
def get_admin(id: int, db: Session = Depends(get_db)):
    return admin.show(id, db)
