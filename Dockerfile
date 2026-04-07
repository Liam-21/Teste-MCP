# FROM python:3.14.3 AS builder

# RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# ADD https://astral.sh/uv/0.5.31/install.sh /uv-installer.sh

# RUN sh /uv-installer.sh && rm /uv-installer.sh

# ENV PATH="/root/.local/bin/:$PATH"

# ENV UV_COMPILE_BYTECODE=1

# ENV UV_LINK_MODE=copy

# WORKDIR /app

# COPY pyproject.toml uv.lock ./

# RUN uv sync --frozen --no-install-project

# RUN uv run python -c "import logging; logging.basicConfig(level=logging.INFO); logging.info('Hello, world')"

# FROM python:3.14.3 AS runtime

# WORKDIR /app

# # Copy the environment that UV created in the builder stage
# COPY --from=builder /app/.venv /app/.venv

# ENV PATH="/app/.venv/bin:$PATH"

# ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# CMD ["uv", "run",  "webScraper_server.py"]


FROM python:3.14.3

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
COPY . /app

# Disable development dependencies
ENV UV_NO_DEV=1

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked

CMD ["uv", "run", "webScraper_server.py"]