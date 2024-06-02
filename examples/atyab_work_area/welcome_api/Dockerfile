FROM python:3.8-alpine

WORKDIR /app

COPY . .

RUN pip install CherryPy==18.9.0

EXPOSE 8080

CMD ["python", "main_api.py"]
