FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y gcc python3-dev && \
    apt-get install -y --no-install-recommends gnupg wget && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && \
    apt-get install -y --no-install-recommends postgresql-client && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd -r responder-app && \
    useradd -r -g responder-app responder-app

COPY requirements.txt /tmp/
RUN pip install --upgrade setuptools && \
    pip install -r /tmp/requirements.txt --cache-dir /pip-cache && \
    rm -rf /pip-cache

WORKDIR /app
COPY --chown=responder-app:responder-app . .
USER responder-app
CMD gunicorn -b :$PORT main:app
