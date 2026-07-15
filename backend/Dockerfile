FROM python:3.12-slim AS th-kiforum-backend

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


RUN apt update && \
	apt install -y \
		python3-dev \
		libc-dev \
		pkg-config \
		gcc \
		g++

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir uwsgi
RUN pip install --no-cache-dir -r requirements.txt

COPY ./th-kiforum/ ./
COPY uwsgi.ini ./

# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
