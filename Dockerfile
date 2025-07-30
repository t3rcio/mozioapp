# syntax=docker/dockerfile:1

FROM python:3.11-slim
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    yes | apt-get install nano curl ca-certificates build-essential python3 python3-dev python3-pip postgresql-server-dev-all libpq-dev libnss3-dev libgdk-pixbuf2.0-dev libgtk-3-dev libxss-dev binutils libproj-dev gdal-bin postgis && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY / .
COPY .env .env

RUN [ -d "_logs" ] || mkdir -p "_logs"
RUN [ -d "static" ] || mkdir -p "static"

# UV
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"
COPY --from=ghcr.io/astral-sh/uv:0.8.3 /uv /uvx /bin/

RUN uv sync --locked
RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["uv", "run", "gunicorn", "-w", "20", "-b", "0.0.0.0:5000", "mozioapp.wsgi"]

