FROM python:3.8-slim-buster

EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app 

RUN pip install -r requirements.txt 

COPY . .

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]