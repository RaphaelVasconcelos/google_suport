FROM python:3.10.0-slim as builder

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade setuptools wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10.0-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    locales-all \
    locales && \
    rm -rf /var/lib/apt/lists/* && \
    localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8

RUN locale-gen pt_BR.UTF-8

# Allow statements and log messages to immediately appear in the Cloud Run logs
ENV PYTHONUNBUFFERED=1

RUN echo "America/Sao_Paulo" > /etc/timezone

WORKDIR /app

ENV PATH="/opt/venv/bin:$PATH"


# The default number of CPU cores is 1, so workers is set to 1.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

ARG GIT_HASH
ENV GIT_HASH=$GIT_HASH

COPY --from=builder /opt/venv /opt/venv
COPY . .
