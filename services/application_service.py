from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime

from models.models import Applications
from schemas.application_schema import ApplicationCreate


def generate_application_number(db: Session) -> str:
    count = db.query(Applications).count() + 1
    return f"APP{count:05d}"   # APP00001


def create_application(db: Session, data: ApplicationCreate):
    # 🔹 generate application number
    application_number = generate_application_number(db)

    application = Applications(
        application_number=application_number,
        full_name=data.full_name,
        email=data.email,

        gender_id=data.gender_id,
        qualification_id=data.qualification_id,
        program_type_id=data.program_type_id,
        course_id=data.course_id,

        phone=data.phone,
        date_of_birth=data.date_of_birth,
        address=data.address,
        board_university=data.board_university,
        year_of_passing=data.year_of_passing,
        percentage_cgpa=data.percentage_cgpa,

        passport_photo=data.passport_photo,
        id_proof=data.id_proof,
        academic_certificate=data.academic_certificate,
    )

    db.add(application)
    db.commit()
    db.refresh(application)

    return application


def get_application_by_id(db: Session, application_id: int):
    app = db.query(Applications).filter(Applications.id == application_id).first()
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    return app


def get_application_by_number(db: Session, application_number: str):
    app = (
        db.query(Applications)
        .filter(Applications.application_number == application_number)
        .first()
    )
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    return app


def delete_application_by_id(db: Session, application_id: int):
    application = (
        db.query(Applications)
        .filter(Applications.id == application_id)
        .first()
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    db.delete(application)
    db.commit()

    return {
        "message": "Application deleted successfully",
        "application_id": application_id
    }