from flask import Flask, render_template
from models.db import db
from routes.routes_patient import patient_bp
from routes.routes_employee import employee_bp
from routes.routes_medicine import medicine_bp
from routes.routes_bill import bill_bp          
from routes.routes_bed import bed_bp            
from routes.routes_attendance import attendance_bp
from routes.routes_task import task_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
db.init_app(app)

with app.app_context():
    db.create_all()

#==============================================================#
#                    Blueprint Registration                    #
#==============================================================#

app.register_blueprint(patient_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(medicine_bp)
app.register_blueprint(bill_bp)     
app.register_blueprint(bed_bp)       
app.register_blueprint(attendance_bp)
app.register_blueprint(task_bp)


#==============================================================#
#                    Home Page Routing                         #
#==============================================================#

@app.route('/')
def base():
    return render_template("base.html")

#==============================================================#
#                           Main                               #
#==============================================================#

if __name__ == '__main__':
    app.run(debug=True)