FROM python:3.11-slim

# install ffmpeg and dependencies
RUN apt-get update && apt-get install -y ffmpeg gcc libssl-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ensure non-root runs (optional)
ENV PYTHONUNBUFFERED=1

CMD ["python3", "main.py"]
