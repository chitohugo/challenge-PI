FROM python:3.10.11

# Set work directory
WORKDIR /app/

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y sqlite3 && pip install -r requirements.txt


# Copy project
COPY ./app /app