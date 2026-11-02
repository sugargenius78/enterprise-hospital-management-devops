from models.models_bill import Bill
from models.db import db
from datetime import datetime

def generate_bill_number():
    last_bill = Bill.query.order_by(Bill.id.desc()).first()
    if last_bill:
        num = int(last_bill.bill_number.split('-')[1]) + 1
    else:
        num = 1
    return f"BILL-{num:06d}"

def add_bill_service(data):
    new_bill = Bill(
        bill_number=generate_bill_number(),
        patient_id=data["patient_id"],
        patient_name=data["patient_name"],
        bill_type=data["bill_type"],
        amount=data["amount"],
        status=data["status"],
        payment_method=data["payment_method"],
        description=data["description"],
    )
    db.session.add(new_bill)
    db.session.commit()