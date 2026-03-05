FROM python:3.11

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv
RUN uv pip install --system -r pyproject.toml

COPY . .

CMD ["streamlit","run","main.py","--server.port=8501","--server.address=0.0.0.0"]