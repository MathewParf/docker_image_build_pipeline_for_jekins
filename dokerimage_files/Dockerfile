FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir psutil
COPY python.py .

EXPOSE 8080

CMD ["python", "python.py"]
