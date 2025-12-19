from typing import Optional

from sqlmodel import SQLModel, Field


class Activity(SQLModel, table=True):
    name: str = Field(primary_key=True)
    description: Optional[str]
    schedule: Optional[str]
    max_participants: int = 0


class Student(SQLModel, table=True):
    email: str = Field(primary_key=True)
    name: Optional[str] = None
    grade: Optional[int] = None


class Participation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_email: str = Field(foreign_key="student.email")
    activity_name: str = Field(foreign_key="activity.name")
