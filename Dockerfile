FROM python:3.12-slim

RUN apt-get update && apt-get install -y nut-client && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app.py .
CMD ["python", "-u", "app.py"]
