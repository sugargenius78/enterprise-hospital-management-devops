from models.db import db

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)
    date = db.Column(db.String(50))
    status = db.Column(db.String(50))
    