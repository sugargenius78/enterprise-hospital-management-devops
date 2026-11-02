from models.models_patient import Patient
from models.db import db

def add_patient_services(data):
    patient = Patient(
        name=data["name"],
        age=data["age"],
        phone=data["phone"],
        address=data["address"]
    )

    db.session.add(patient)
    db.session.commit()
