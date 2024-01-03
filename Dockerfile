FROM python:3.9

RUN mkdir app/
WORKDIR /app
COPY app .
COPY .env .

RUN pip install --upgrade pip 
RUN pip install poetry
RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi -vvv
RUN poetry config virtualenvs.create false \
  && poetry install
