# Enterprise Hospital Management System (HMS) & DevOps Pipeline

## Overview
A modular, multi-tier web application engineered to digitize hospital workflows, secure electronic health records (EHR), and manage clinical resource allocations[cite: 172]. Built following Agile (Scrum) principles and DevOps deployment workflows for the Agile Development and DevOps module (SEN5002) under the Cardiff Metropolitan University curriculum[cite: 12, 171, 173, 186]. Grade Achieved: 71% (First-Class Honours / Distinction)[cite: 12].

## Core Modules & Functionality
- **Patient & Ward Management:** Inpatient profiling, real-time bed allocation lifecycles, and occupancy tracking[cite: 172, 177, 178].
- **Staff & Task Delegation:** Multi-role user privilege enforcement, shift attendance monitoring, and internal task distribution pipelines[cite: 172, 177, 178].
- **Pharmacy & Billing Automation:** Dynamic medicine inventory tracking with stock-level alerts and automated medical invoice generation[cite: 172, 177, 178].
- **Role-Based Access Control (RBAC):** Strict operational boundaries separating Administrative Staff, Doctors, Nurses, Pharmacy, and Finance personnel[cite: 172, 178, 179].

## Software Engineering & DevOps Practices
- **Agile Scrum Execution:** Iterative 12-week development lifecycle using CPM (Critical Path Method) scheduling and formal risk logs[cite: 173, 174, 175, 176].
- **3-Tier Architecture:** Decoupled layout strictly isolating Presentation (Jinja2/Bootstrap), Application Services (Flask), and Data Persistence (SQLAlchemy/SQLite)[cite: 176, 184, 186].
- **Architectural Modeling:** System validated through formal UML Use Case, Class, Sequence, and Component Diagrams[cite: 173, 179, 180, 181, 182, 183, 184, 185, 186].
- **Git Feature Branching:** Feature-isolated branching strategy (`feature/bed-management`, `module-medicine`) preventing merge conflicts across distributed team workflows[cite: 175, 186, 187].

## Technology Stack
- **Backend:** Python (Flask Framework)[cite: 173, 184, 186]
- **ORM & Database:** SQLAlchemy, SQLite[cite: 175, 178, 181, 184, 186]
- **Frontend:** HTML5, CSS3, Bootstrap, Jinja2 Template Inheritance[cite: 176, 185]
- **Tools & Methodologies:** Git, GitHub, VS Code, Agile/Scrum, CPM Network Analysis[cite: 173, 174, 175, 176, 186, 187]

## Project Structure
- `app.py` - Core application kernel and Flask blueprint registration[cite: 185, 187, 191]
- `routes/` - Presentation layer handling HTTP endpoint routing[cite: 185, 187, 191]
- `services/` - Business logic and transaction validation layer[cite: 185, 187, 191]
- `models/` - SQLAlchemy relational database entities and schema constraints[cite: 181, 187, 191]
- `templates/` - Modular Jinja2 frontend views and master layout[cite: 176, 185, 187, 191]
- `requirements.txt` - Project environment dependencies[cite: 187, 191]
- `st20320120 SEN5002 PORT1 (1).pdf` - Full engineering portfolio and architectural diagrams[cite: 171, 173, 180, 182, 183, 185, 186]

## How to Run
```bash
# Clone the repository
git clone [https://github.com/sugargenius78/enterprise-hospital-management-devops.git](https://github.com/sugargenius78/enterprise-hospital-management-devops.git)

# Install dependencies
pip install -r requirements.txt

# Launch application
python app.py
