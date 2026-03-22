# Используем официальный Python 3.11 slim
FROM python:3.11-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY pyproject.toml uv.lock ./

# Устанавливаем pip-tools (uv)
RUN pip install --upgrade pip \
    && pip install uv uvicorn python-dotenv fastapi sqlalchemy pandas psycopg2-binary

# Копируем весь код приложения
COPY . .

# Экспорт порта
EXPOSE 8000

# Команда запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]