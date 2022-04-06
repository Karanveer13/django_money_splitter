release: python manage.py makemigrations
release: python manage.py migrate
web: run-program waitress-serve --port=$PORT settings.wsgi:application
web: python manage.py runserver 127.0.0.1:$PORT
web: gunicorn money_splitter.wsgi
