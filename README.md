# Test task
This is a site for storing users and books.

# Instructions
- Install Python 3.6+ and pip ;
- ```(pip install -r requirements.txt)```;
- Configure PostgreSQL server;
- Configure connection to the database with your own or existing settings:
```$xslt
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'task1',
'USER': 'library1',
'PASSWORD': '123',
'HOST': 'localhost',
'PORT': ''
```
- Make migrate:
```$xslt
python manage.py migrate
python manage.py makemigrations library
python manage.py migrate
```
- If you need to use fixtures:
```$xslt
python manage.py loaddata base
```
- Start server:
```$xslt
python manage.py runserver
```