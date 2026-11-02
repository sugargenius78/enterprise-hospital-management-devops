from flask import Blueprint, render_template, request
from models.models_bed import Bed
from models.db import db
from services.services_bed import add_bed_service

bed_bp = Blueprint('bed', __name__)

@bed_bp.route('/add_bed', methods=['GET', 'POST'])
def add_bed():
    if request.method == 'POST':
        is_occupied_val = True if request.form.get('is_occupied') == 'true' else False
        
        data = {
            "bed_number": request.form['bed_number'],
            "department": request.form['department'],
            "is_occupied": is_occupied_val
        }

        add_bed_service(data)
        return "Data added successfully"

    return render_template('add_bed.html')


@bed_bp.route('/view_update_bed')
def view_update_bed():
    beds = Bed.query.all()
    return render_template("view_update_bed.html", beds=beds)


@bed_bp.route('/edit_bed/<int:id>', methods=["GET", "POST"])
def edit_bed(id):
    bed = Bed.query.get(id)

    if not bed:
        return "Bed not found"

    if request.method == "POST":
        is_occupied_val = True if request.form.get('is_occupied') == 'true' else False

        bed.bed_number = request.form["bed_number"]
        bed.department = request.form["department"]
        bed.is_occupied = is_occupied_val

        db.session.commit()
        return "UPDATED SUCCESSFULLY"

    return render_template("edit_bed.html", bed=bed)