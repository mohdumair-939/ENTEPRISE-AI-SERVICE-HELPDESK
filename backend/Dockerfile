# -------------------------------------------------------
# Enterprise AI Service Desk Backend
# Production FastAPI Container
# -------------------------------------------------------

FROM python:3.12-slim


# Prevent Python from writing pyc files
# and enable immediate logging output

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


COPY app ./app


EXPOSE 8000


CMD [
    "uvicorn",
    "app.main:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8000"
]