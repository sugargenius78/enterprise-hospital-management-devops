from flask import Blueprint, render_template, request
from models.models_bill import Bill
from models.db import db
from services.services_bill import add_bill_service
from datetime import datetime

bill_bp = Blueprint('bill', __name__)  # ← CHANGED from billing_bp to bill_bp

@bill_bp.route('/add_bill', methods=['GET', 'POST'])
def add_bill():
    if request.method == 'POST':
        data = {
            "patient_id": int(request.form['patient_id']),
            "patient_name": request.form['patient_name'],
            "bill_type": request.form['bill_type'],
            "amount": float(request.form['amount']),
            "status": request.form.get('status', 'Pending'),
            "payment_method": request.form.get('payment_method'),
            "description": request.form.get('description')
        }

        add_bill_service(data)
        return "Data added successfully"

    return render_template('add_bill.html')


@bill_bp.route('/view_update_bill')
def view_update_bill():
    bills = Bill.query.all()
    return render_template("view_update_bill.html", bills=bills)


@bill_bp.route('/edit_bill/<int:id>', methods=["GET", "POST"])
def edit_bill(id):
    bill = Bill.query.get(id)

    if not bill:
        return "Bill not found"

    if request.method == "POST":
        bill.bill_type = request.form["bill_type"]
        bill.amount = float(request.form["amount"])
        bill.description = request.form.get("description")

        db.session.commit()
        return "UPDATED SUCCESSFULLY"

    return render_template("edit_bill.html", bill=bill)


@bill_bp.route('/pay_bill/<int:id>', methods=["GET", "POST"])
def pay_bill(id):
    bill = Bill.query.get(id)

    if not bill:
        return "Bill not found"

    if request.method == "POST":
        bill.status = "Paid"
        bill.payment_method = request.form["payment_method"]
        bill.paid_date = datetime.utcnow()

        db.session.commit()
        return "PAYMENT PROCESSED SUCCESSFULLY"

    return render_template("pay_bill.html", bill=bill)