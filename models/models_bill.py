from models.db import db
from datetime import datetime
class Bill(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    bill_number = db.Column(db.String(50))
    patient_id = db.Column(db.Integer)
    patient_name = db.Column(db.String(100))
    bill_type = db.Column(db.String(50))
    amount = db.Column(db.Float)
    status = db.Column(db.String(20))
    payment_method = db.Column(db.String(50))
    description = db.Column(db.String(500))
    created_date = db.Column(db.DateTime)
    paid_date = db.Column(db.DateTime)