FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

# Note: webbrowser.open will not work inside a headless container unless configured specifically.
# This Dockerfile is primarily for packaging dependencies.
ENTRYPOINT ["python", "server.py"]
