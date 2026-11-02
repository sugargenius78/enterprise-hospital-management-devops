from models.models_medicine import Medicine 
from models.db import db
def add_medicine_service(data):
    new_medicine = Medicine(
        name=data["name"],
        quantity=data["quantity"],
        price=data["price"]
    )
    db.session.add(new_medicine)
    db.session.commit()