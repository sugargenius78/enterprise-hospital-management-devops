from models.models_bed import Bed
from models.db import db

def add_bed_service(data):
    new_bed = Bed(
        bed_number=data["bed_number"],
        department=data["department"],
        is_occupied=data["is_occupied"]
    )
    db.session.add(new_bed)
    db.session.commit()