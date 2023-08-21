FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "es_setup.py"]
EXPOSE 5000

CMD ["python", "app.py"]
