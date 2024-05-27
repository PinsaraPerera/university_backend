from typing import List, Optional
from pydantic import BaseModel

class AdminBase(BaseModel):
    id: int
    name: str
    email: str
    password: str

class Admin(BaseModel):
    name: str
    email: str
    