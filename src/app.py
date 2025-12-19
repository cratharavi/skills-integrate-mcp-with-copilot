"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# Database-backed persistence
from .db import create_db_and_tables, get_session
from .models import Activity, Student, Participation
from sqlmodel import select
import json
from pathlib import Path

# Create DB and tables on startup
create_db_and_tables()

# Seed data from activities.json if DB is empty
seed_file = Path(__file__).parent / "activities.json"

with get_session() as session:
    # If no activities exist, seed from file
    if not session.exec(select(Activity)).first():
        if seed_file.exists():
            data = json.loads(seed_file.read_text())
            for a in data:
                act = Activity(
                    name=a["name"],
                    description=a.get("description"),
                    schedule=a.get("schedule"),
                    max_participants=a.get("max_participants", 0),
                )
                session.add(act)
                # add students and participations
                for p in a.get("participants", []):
                    if not session.get(Student, p):
                        session.add(Student(email=p))
                    session.add(Participation(student_email=p, activity_name=a["name"]))
            session.commit()


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    """Return all activities with details and participant lists"""
    with get_session() as session:
        results = {}
        activities = session.exec(select(Activity)).all()
        for a in activities:
            participants = [p.student_email for p in session.exec(select(Participation).where(Participation.activity_name == a.name)).all()]
            results[a.name] = {
                "description": a.description,
                "schedule": a.schedule,
                "max_participants": a.max_participants,
                "participants": participants,
            }
        return results


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity (persists to DB)"""
    with get_session() as session:
        activity = session.get(Activity, activity_name)
        if not activity:
            raise HTTPException(status_code=404, detail="Activity not found")

        # create student if needed
        student = session.get(Student, email)
        if not student:
            student = Student(email=email)
            session.add(student)
            session.commit()

        # check if already signed up
        existing = session.exec(select(Participation).where(
            (Participation.activity_name == activity_name) & (Participation.student_email == email)
        )).first()
        if existing:
            raise HTTPException(status_code=400, detail="Student is already signed up")

        # enforce capacity
        current_count = len(session.exec(select(Participation).where(Participation.activity_name == activity_name)).all())
        if current_count >= activity.max_participants:
            raise HTTPException(status_code=409, detail="Activity is full")

        session.add(Participation(student_email=email, activity_name=activity_name))
        session.commit()
        return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str):
    """Unregister a student from an activity"""
    with get_session() as session:
        activity = session.get(Activity, activity_name)
        if not activity:
            raise HTTPException(status_code=404, detail="Activity not found")

        existing = session.exec(select(Participation).where(
            (Participation.activity_name == activity_name) & (Participation.student_email == email)
        )).first()
        if not existing:
            raise HTTPException(status_code=400, detail="Student is not signed up for this activity")

        session.delete(existing)
        session.commit()
        return {"message": f"Unregistered {email} from {activity_name}"}


