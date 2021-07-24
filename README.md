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
        5. Set env var: "set(win)/export(linux) DJANGO_SECRET_KEY="django-insecure-@8fik3ibepgr8as5$2n8$x1$2o8!fqnto8h)y8_-)!8=f&caa%""
        6. Migration: "python manage.py migrate"
        7. Populate db with initial data: "python manage.py loaddata FormChecker\fixture.json"
        8. Run local server: "python manage.py runserver"
        9. Test app in venv: "python FormChecker\test_script.py"
