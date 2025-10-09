from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    fullname: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    fullname: str
    email: EmailStr
    created_at: datetime
