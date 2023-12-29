FROM python:3.10-slim

RUN mkdir app/
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt


COPY app .
COPY .env .
COPY run-backend.sh run-backend.sh
COPY run-parser.sh run-parser.sh
RUN chmod +x run-backend.sh run-parser.sh 
