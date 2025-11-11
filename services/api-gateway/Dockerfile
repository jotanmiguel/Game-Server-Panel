FROM python:3.11-slim

ARG ENV=dev

ENV PYTHONPATH="${PYTHONPATH}:/app"

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "if [ '$ENV' = 'dev' ]; then uvicorn main:app --host 0.0.0.0 --port 8080 --reload --reload-dir /app; else uvicorn main:app --host 0.0.0.0 --port 8080; fi"]

