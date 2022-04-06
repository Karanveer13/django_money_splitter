release: python manage.py makemigrations
release: python manage.py migrate
web: python manage.py runserver 127.0.0.1:$PORT
web: gunicorn money_splitter.wsgi
