# Travel Planner 
## Overview
This is a backend application for managing travel projects and places. Built with Django and Django REST Framework.
## Features
- Create, update, delete travel projects
- Add places to projects with validation via the Art Institute of Chicago API
- Maximum 10 places per project
- Prevent deletion of projects if any place is visited
- Basic Swagger API documentation
## Swager
Swagger is available at: `http://127.0.0.1:8000/swagger/`
## Setup
1. Clone the repository:
```bash
git clone https://github.com/PapaRumskiy/travel_planer
cd travel_planer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
http://127.0.0.1:8000/swagger/
