from flask import Blueprint, render_template, request
from models.models_attendance import Attendance
from models.models_employee import Employee
from models.db import db
from services.services_attendance import add_attendance_service
from datetime import date

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/add_attendance', methods=['GET', 'POST'])
def add_attendance():
    employees = Employee.query.all()
    current_date = date.today().strftime("%Y-%m-%d")
    
    if request.method == 'POST':
        data = {
            "employee_id": int(request.form['employee_id']),
            "date": request.form['date'],
            "status": request.form['status']
        }

        add_attendance_service(data)
        return "Data added successfully"

    return render_template('add_attendance.html', employees=employees, current_date=current_date)


@attendance_bp.route('/view_update_attendance')
def view_update_attendance():
    attendance_records = Attendance.query.all()
    employees = Employee.query.all()
    return render_template("view_update_attendance.html", attendance=attendance_records, employees=employees)


@attendance_bp.route('/edit_attendance/<int:id>', methods=["GET", "POST"])
def edit_attendance(id):
    attendance = Attendance.query.get(id)

    if not attendance:
        return "Attendance record not found"

    if request.method == "POST":
        attendance.employee_id = int(request.form['employee_id'])
        attendance.date = request.form['date']
        attendance.status = request.form['status']

        db.session.commit()
        return "UPDATED SUCCESSFULLY"

    employees = Employee.query.all()
    return render_template("edit_attendance.html", attendance=attendance, employees=employees)