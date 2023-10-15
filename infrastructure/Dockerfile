FROM python:3.10.11

# Set work directory
WORKDIR /backend

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY infrastructure/requirements.txt ./infrastructure/
RUN apt-get update && apt-get install -y sqlite3 && pip install --no-cache-dir --upgrade -r infrastructure/requirements.txt

# Copy project
COPY . /backend

CMD ["uvicorn", "interface.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]