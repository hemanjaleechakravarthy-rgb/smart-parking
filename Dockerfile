FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pytest hypothesis pytest-cov mypy ruff matplotlib

ENV PYTHONPATH=/app

CMD ["python", "main.py"]