from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.application_schema import ApplicationCreate, ApplicationResponse
from services.application_service import (
    create_application,
    get_application_by_id,
    get_application_by_number,
)

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.post("/", response_model=ApplicationResponse)
def submit_application(
    payload: ApplicationCreate,
    db: Session = Depends(get_db)
):
    return create_application(db, payload)


@router.get("/{application_id}", response_model=ApplicationResponse)
def fetch_application(application_id: int, db: Session = Depends(get_db)):
    return get_application_by_id(db, application_id)


@router.get("/by-number/{application_number}", response_model=ApplicationResponse)
def fetch_application_by_number(application_number: str, db: Session = Depends(get_db)):
    return get_application_by_number(db, application_number)
