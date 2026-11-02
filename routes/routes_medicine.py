from flask import Blueprint, render_template, request
from models.models_medicine import Medicine
from models.db import db
from services.services_medicine import add_medicine_service

medicine_bp = Blueprint('medicine', __name__)

@medicine_bp.route('/add_medicine', methods=['GET', 'POST'])
def add_medicine():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "quantity": request.form['quantity'],
            "price": request.form['price']
        }

        add_medicine_service(data)
        return "Data added successfully"

    return render_template('add_medicine.html')


@medicine_bp.route('/view_update_medicine')
def view_update_medicine():
    medicines = Medicine.query.all()
    return render_template("view_update_medicine.html", medicines=medicines)


@medicine_bp.route('/edit_medicine/<int:id>', methods=["GET", "POST"])
def edit_medicine(id):
    medicine = Medicine.query.get(id)

    if not medicine:
        return "Medicine not found"

    if request.method == "POST":
        medicine.name = request.form["name"]
        medicine.quantity = int(request.form["quantity"])
        medicine.price = float(request.form["price"])

        db.session.commit()
        return "UPDATED SUCCESSFULLY"

    return render_template("edit_medicine.html", medicine=medicine)