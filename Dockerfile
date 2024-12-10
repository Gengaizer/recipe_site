FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./mysite .


CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]