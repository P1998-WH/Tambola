FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY p6_2.py weather_data.csv /app/

CMD ["python", "p6_2.py"]
