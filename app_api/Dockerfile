FROM python:3.11

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv
RUN uv pip install --system -r pyproject.toml

COPY . .

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]