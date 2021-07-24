WEB-app for defining completed forms.

    Stack:
        python 3.9
        Django 3.2.5
        DRF 3.12.4
        SQLite3

    Usage:
        1. clone repo
        2. Get dependecies: "pip install requirements.txt"
        3. Set environ variable: "set(win)/export(linux) DJANGO_SECRET_KEY="django-insecure-@8fik3ibepgr8as5$2n8$x1$2o8!fqnto8h)y8_-)!8=f&caa%"" 
        3. Migration: "python manage.py migrate"
        4. Populate db with initial data: "python manage.py loaddata FormChecker\fixture.json"
        5. Test app: "python FormChecker\test_script"
