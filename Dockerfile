FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv
RUN uv sync

COPY . .

CMD ["uv", "run", "python", "-m", "app.main"]