WEB-app for defining completed forms.

    Stack:
        python 3.9
        Django 3.2.5
        DRF 3.12.4
        SQLite3

    Usage:
        1. clone repo
        2. Get dependecies: "pip install requirements.txt"
        3. Migration: "python manage.py migrate"
        4. Populate db with initial data: "python manage.py loaddata FormChecker\fixture.json"
        5. Test app: "python FormChecker\test_script"
