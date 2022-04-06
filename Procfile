web: python manage.py runserver 127.0.0.1:$PORT
web: gunicorn money_splitter.wsgi
web: python manage.py makemigrations
web: python manage.py migrate
