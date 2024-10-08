FROM python:3.11
LABEL authors="BIRZHAN"

ENV PYTHONUNDUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY django_diploma . , diploma-frontend

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]

ENTRYPOINT ["top", "-b"]