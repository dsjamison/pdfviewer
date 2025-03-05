venv\Scripts\activate.bat
pip install -r requirements.txt
py manage.py createsuperuser
py manage.py runserver