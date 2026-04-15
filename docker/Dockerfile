FROM python:3.12

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

# Copy the project into the image
COPY . /app

# Disable development dependencies
ENV UV_NO_DEV=1

ENV PYTHONPATH="/app/src"

CMD ["uv", "run", "--python", "3.12", "src/webscraper/main.py"]