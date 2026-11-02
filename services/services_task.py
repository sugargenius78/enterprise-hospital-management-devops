from models.models_task import Task
from models.models_employee import Employee
from models.db import db
from datetime import datetime


def generate_task_number():
    last_task = Task.query.order_by(Task.id.desc()).first()

    if last_task:
        num = int(last_task.task_number.split('-')[1]) + 1
    else:
        num = 1

    return f"TASK-{num:06d}"


def add_task_service(data):
    employee = Employee.query.get(data["employee_id"])

    new_task = Task(
        task_number=generate_task_number(),
        employee_id=employee.id,
        employee_name=employee.name,
        status=data["status"],
        description=data["description"],
        created_date=datetime.now(),
        due_date=datetime.strptime(data["due_date"], "%Y-%m-%d")
    )

    db.session.add(new_task)
    db.session.commit()