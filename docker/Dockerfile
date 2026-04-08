FROM python:3.14.3

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
COPY . /app

# Disable development dependencies
ENV UV_NO_DEV=1

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked

ENV PYTHONPATH="/app/src:${PYTHONPATH}"

CMD ["uv", "run", "src/webscraper/main.py"]