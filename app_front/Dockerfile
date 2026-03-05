FROM python:3.11-slim

WORKDIR /app/app_front

COPY pyproject.toml uv.lock ./

RUN pip install --upgrade pip \
    && pip install uv streamlit requests python-dotenv

COPY . .

EXPOSE 8501

CMD ["uv", "run", "--active", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]