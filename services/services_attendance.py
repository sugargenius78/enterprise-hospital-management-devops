from models.models_attendance import  Attendance
from models.db import db

def add_attendance_service(data):
    attendance = Attendance(
        employee_id=data["employee_id"],
        date=data["date"],
        status=data["status"]
    )
    db.session.add(attendance)
    db.session.commit()