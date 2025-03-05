
md <project>
cd <project>
python -m venv .venv
.venv\Scripts\activate
pip install django
django-admin startproject <project> .

python manage.py startapp <app>

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

add urls.py and update <project> urls.py

settings.py -> app to installed    apps = ['<app>',]

