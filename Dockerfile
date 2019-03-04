FROM python:3.6-alpine

LABEL maintainer = "Felix Fennell <felnne@bas.ac.uk>"

# Setup project
WORKDIR /usr/src/app

ENV PYTHONPATH /usr/src/app
ENV FLASK_APP manage.py
ENV FLASK_ENV development

# Setup project dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

# Setup runtime
ENTRYPOINT []
