from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.master_schema import CourseResponse, MasterResponse
from services.master_service import (
    get_genders,
    get_qualifications,
    get_program_types,
    get_courses
)

router = APIRouter(prefix="/masters", tags=["Masters"])

@router.get("/genders", response_model=list[MasterResponse])
def list_genders(db: Session = Depends(get_db)):
    return get_genders(db)

@router.get("/qualifications", response_model=list[MasterResponse])
def list_qualifications(db: Session = Depends(get_db)):
    return get_qualifications(db)

@router.get("/program-types", response_model=list[MasterResponse])
def list_program_types(db: Session = Depends(get_db)):
    return get_program_types(db)


@router.get("/courses", response_model=list[CourseResponse])
def list_courses(
    program_type_id: int | None = None,
    db: Session = Depends(get_db)
):
    return get_courses(db, program_type_id)