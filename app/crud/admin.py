from sqlalchemy.orm import Session
import app.models.admin as admin
from app.schemas import admin_schema
from fastapi import HTTPException, status
from app.utils import hashing


def create(request: admin_schema.Admin, db: Session):
    new_admin = admin.Admin(
        id=request.id,
        name=request.name,
        email=request.email,
        password=hashing.Hash.bcrypt(request.password),
    )

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

def show(id: int, db: Session):
    user = db.query(admin.Admin).filter(admin.Admin.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"Admin with id {id} not found")
    return user
