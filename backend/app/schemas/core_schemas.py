
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class CompanyBase(BaseModel):
    name: str
    owner_email: EmailStr

class CompanyCreate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: EmailStr
    role: str = "staff"

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    company_id: int
    class Config:
        from_attributes = True
