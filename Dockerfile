FROM python:3.9.20-alpine3.19

RUN pip install "fastapi[standard]"
RUN pip install redis

WORKDIR /app

COPY main.py main.py

CMD [ "fastapi", "dev", "main.py", "--host=0.0.0.0" ]