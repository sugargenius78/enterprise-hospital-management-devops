from models.db import db
from datetime import datetime
class Task(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    task_number = db.Column(db.String(50))
    employee_id = db.Column(db.Integer)
    employee_name = db.Column(db.String(100))
    status = db.Column(db.String(20))
    description = db.Column(db.String(500))
    created_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)