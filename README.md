WEB-app for defining completed forms.

    Stack:
        python 3.9
        Django 3.2.5
        DRF 3.12.4
        SQLite3

    Usage:
        1. clone repo
        2. Venv init: "python -m venv venv"
        3. Activate venv: "venv\Scripts\activate"
        4. Get dependecies: "pip install -r requirements.txt"
        5. Migration: "python manage.py migrate"
        6. Populate db with initial data: "python manage.py loaddata FormChecker\fixture.json"
        7. Run local server: "python manage.py runserver"
        8. Test app in venv: "python FormChecker\test_script.py"
