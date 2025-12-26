from pydantic import BaseModel, EmailStr, Field
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional



class RegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)
    confirm_password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., max_length=72)


class LoginResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class ApplicationCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str]

    date_of_birth: Optional[date]
    gender_id: int
    qualification_id: int
    program_type_id: int
    course_id: int

    address: Optional[str]
    board_university: Optional[str]
    year_of_passing: Optional[int]
    percentage_cgpa: Optional[float]


class ApplicationResponse(BaseModel):
    id: int
    application_number: str
    full_name: str
    email: EmailStr
    payment_status: str
    application_status: str

    class Config:
        from_attributes = True
