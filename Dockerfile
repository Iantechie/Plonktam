FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir app

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY . /app/

RUN pip3 install -r requirements.txt

EXPOSE 8000

# RUN python manage.py collectstatic

RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]

