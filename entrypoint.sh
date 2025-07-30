#!/bin/sh
# A script to wait for DB service
set -e

until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" > /dev/null 2>&1; do
  >&2 echo "Postgres is not ready yet. Waiting..."
  sleep 3
done

uv run manage.py migrate
uv run manage.py collectstatic --noinput

exec "$@"
