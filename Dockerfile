FROM python:3.12-slim

# evita pyc e buffer de log
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# deps primeiro (cache)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copia o código
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]