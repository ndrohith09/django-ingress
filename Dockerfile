FROM ubuntu:20.04 

RUN apt-get update && apt-get install -y tzdata && apt install -y python3.8 python3-pip

RUN apt install python3-dev libpq-dev nginx -y

RUN pip install django gunicorn psycopg2

ADD . /app

WORKDIR /app

EXPOSE 8001

CMD ["gunicorn", "--bind", ":8001", "--workers", "3", "djangokubernetesproject.wsgi"]