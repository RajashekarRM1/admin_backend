from pydantic import BaseModel
from typing import Optional

class MasterCreate(BaseModel):
    name: str


class MasterResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class GenderResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class QualificationResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ProgramTypeResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class CourseResponse(BaseModel):
    id: int
    course_name: str
    program_type_id: Optional[int]

    class Config:
        from_attributes = True
