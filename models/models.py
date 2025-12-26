from typing import Optional
import datetime
import decimal

from sqlalchemy import Boolean, Date, DateTime, ForeignKeyConstraint, Identity, Integer, Numeric, PrimaryKeyConstraint, String, Text, UniqueConstraint, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class MasterGender(Base):
    __tablename__ = 'master_gender'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='master_gender_pkey'),
        UniqueConstraint('name', name='master_gender_name_key')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)

    applications: Mapped[list['Applications']] = relationship('Applications', back_populates='gender')


class MasterProgramTypes(Base):
    __tablename__ = 'master_program_types'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='master_program_types_pkey'),
        UniqueConstraint('name', name='master_program_types_name_key')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    master_courses: Mapped[list['MasterCourses']] = relationship('MasterCourses', back_populates='program_type')
    applications: Mapped[list['Applications']] = relationship('Applications', back_populates='program_type')


class MasterQualifications(Base):
    __tablename__ = 'master_qualifications'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='master_qualifications_pkey'),
        UniqueConstraint('name', name='master_qualifications_name_key')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    applications: Mapped[list['Applications']] = relationship('Applications', back_populates='qualification')


class UsersRegistration(Base):
    __tablename__ = 'users_registration'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='users_registration_pkey'),
        UniqueConstraint('email', name='users_registration_email_key')
    )

    id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class MasterCourses(Base):
    __tablename__ = 'master_courses'
    __table_args__ = (
        ForeignKeyConstraint(['program_type_id'], ['master_program_types.id'], name='master_courses_program_type_id_fkey'),
        PrimaryKeyConstraint('id', name='master_courses_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    course_name: Mapped[str] = mapped_column(String(100), nullable=False)
    program_type_id: Mapped[Optional[int]] = mapped_column(Integer)

    program_type: Mapped[Optional['MasterProgramTypes']] = relationship('MasterProgramTypes', back_populates='master_courses')
    applications: Mapped[list['Applications']] = relationship('Applications', back_populates='course')


class Applications(Base):
    __tablename__ = 'applications'
    __table_args__ = (
        ForeignKeyConstraint(['course_id'], ['master_courses.id'], name='applications_course_id_fkey'),
        ForeignKeyConstraint(['gender_id'], ['master_gender.id'], name='applications_gender_id_fkey'),
        ForeignKeyConstraint(['program_type_id'], ['master_program_types.id'], name='applications_program_type_id_fkey'),
        ForeignKeyConstraint(['qualification_id'], ['master_qualifications.id'], name='applications_qualification_id_fkey'),
        PrimaryKeyConstraint('id', name='applications_pkey'),
        UniqueConstraint('application_number', name='applications_application_number_key')
    )

    id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    application_number: Mapped[str] = mapped_column(String(30), nullable=False)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    gender_id: Mapped[int] = mapped_column(Integer, nullable=False)
    qualification_id: Mapped[int] = mapped_column(Integer, nullable=False)
    program_type_id: Mapped[int] = mapped_column(Integer, nullable=False)
    course_id: Mapped[int] = mapped_column(Integer, nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(String(15))
    date_of_birth: Mapped[Optional[datetime.date]] = mapped_column(Date)
    address: Mapped[Optional[str]] = mapped_column(Text)
    board_university: Mapped[Optional[str]] = mapped_column(String(150))
    year_of_passing: Mapped[Optional[int]] = mapped_column(Integer)
    percentage_cgpa: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(5, 2))
    passport_photo: Mapped[Optional[str]] = mapped_column(String(255))
    id_proof: Mapped[Optional[str]] = mapped_column(String(255))
    academic_certificate: Mapped[Optional[str]] = mapped_column(String(255))
    application_fee: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2), server_default=text('50000'))
    utr_number: Mapped[Optional[str]] = mapped_column(String(20))
    payment_status: Mapped[Optional[str]] = mapped_column(String(30), server_default=text("'Pending'::character varying"))
    application_status: Mapped[Optional[str]] = mapped_column(String(30), server_default=text("'Payment Pending'::character varying"))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    course: Mapped['MasterCourses'] = relationship('MasterCourses', back_populates='applications')
    gender: Mapped['MasterGender'] = relationship('MasterGender', back_populates='applications')
    program_type: Mapped['MasterProgramTypes'] = relationship('MasterProgramTypes', back_populates='applications')
    qualification: Mapped['MasterQualifications'] = relationship('MasterQualifications', back_populates='applications')
