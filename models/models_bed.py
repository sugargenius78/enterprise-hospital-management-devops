from models.db import db

class Bed(db.Model):
    __tablename__ = 'beds'
    
    id = db.Column(db.Integer, primary_key=True)
    bed_number = db.Column(db.String(50), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)  
    is_occupied = db.Column(db.Boolean, default=False, nullable=False)