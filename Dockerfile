FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

RUN useradd --system --no-create-home bot
USER bot

CMD ["python", "main.py"]
