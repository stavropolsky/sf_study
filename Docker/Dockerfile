FROM python:3.9-slim

RUN pip install requests

WORKDIR /app

COPY main.py .

# Аргумент для передачи SITE_URL при запуске контейнера
ARG SITE_URL

CMD ["python", "main.py"]

