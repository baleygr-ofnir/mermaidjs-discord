FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    THEME_DB_PATH=/data/themes.db

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py theme_store.py ./

RUN useradd --system --no-create-home bot \
 && mkdir /data \
 && chown bot /data
USER bot

CMD ["python", "main.py"]
