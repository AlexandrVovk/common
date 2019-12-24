FROM python:3.7

RUN pip install django

RUN pip install requests

COPY . /app

WORKDIR /app

RUN ls -la

EXPOSE 8000

CMD python manage.py runserver 0:8000
