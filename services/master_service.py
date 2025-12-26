from sqlalchemy.orm import Session
from models.models import (
    MasterGender,
    MasterQualifications,
    MasterProgramTypes,
    MasterCourses
)

def get_genders(db: Session):
    return db.query(MasterGender).order_by(MasterGender.id).all()

def get_qualifications(db: Session):
    return db.query(MasterQualifications).order_by(MasterQualifications.id).all()

def get_program_types(db: Session):
    return db.query(MasterProgramTypes).order_by(MasterProgramTypes.id).all()

def get_courses(db: Session, program_type_id: int | None = None):
    query = db.query(MasterCourses)
    if program_type_id:
        query = query.filter(MasterCourses.program_type_id == program_type_id)
    return query.order_by(MasterCourses.id).all()