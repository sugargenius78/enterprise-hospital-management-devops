from flask import Blueprint, render_template, request, redirect, url_for
from models.models_task import Task
from models.models_employee import Employee
from models.db import db
from services.services_task import add_task_service
from datetime import datetime, date

task_bp = Blueprint('task', __name__)


@task_bp.route('/add_task', methods=['GET', 'POST'])
def add_task():
    employees = Employee.query.all()
    current_date = date.today().strftime("%Y-%m-%d")

    if request.method == 'POST':
        data = {
            "employee_id": int(request.form['employee_id']),
            "status": request.form['status'],
            "description": request.form['description'],
            "due_date": request.form['due_date']
        }

        add_task_service(data)
        return redirect(url_for('task.view_update_task'))

    return render_template(
        'add_task.html',
        employees=employees,
        current_date=current_date
    )


@task_bp.route('/view_update_task')
def view_update_task():
    task_records = Task.query.all()
    return render_template(
        "view_update_task.html",
        tasks=task_records
    )


@task_bp.route('/edit_task/<int:id>', methods=["GET", "POST"])
def edit_task(id):
    task = Task.query.get(id)

    if not task:
        return "Task record not found"

    employees = Employee.query.all()

    if request.method == "POST":
        employee = Employee.query.get(int(request.form['employee_id']))

        task.employee_id = employee.id
        task.employee_name = employee.name
        task.status = request.form['status']
        task.description = request.form['description']
        task.due_date = datetime.strptime(request.form['due_date'], "%Y-%m-%d")

        db.session.commit()
        return redirect(url_for('task.view_update_task'))

    return render_template(
        "edit_task.html",
        task=task,
        employees=employees
    )