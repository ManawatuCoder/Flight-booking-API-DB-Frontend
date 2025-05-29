FROM python:latest
COPY . /app
WORKDIR /app
run pip install django
run pip install django-cors-headers
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]