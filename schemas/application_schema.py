from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


class ApplicationCreate(BaseModel):
    full_name: str = Field(..., min_length=3)
    email: EmailStr

    gender_id: int
    qualification_id: int
    program_type_id: int
    course_id: int

    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    board_university: Optional[str] = None
    year_of_passing: Optional[int] = None
    percentage_cgpa: Optional[Decimal] = None

    passport_photo: Optional[str] = None
    id_proof: Optional[str] = None
    academic_certificate: Optional[str] = None


class ApplicationResponse(BaseModel):
    id: int
    application_number: str
    full_name: str
    email: str

    gender_id: int
    qualification_id: int
    program_type_id: int
    course_id: int

    payment_status: str
    application_status: str
    created_at: datetime

    class Config:
        from_attributes = True
