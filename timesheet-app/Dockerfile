FROM python:3.10-alpine

RUN apk add --no-cache \
        libxml2 \
        libxml2-dev \
        libxslt \
        libxslt-dev \
        curl \
        gcc \
        libressl-dev \
        musl-dev \
        musl \
        libffi-dev && \
    pip install --no-cache-dir poetry

WORKDIR /web

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml ./

#RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

RUN apk del \
        curl \
        gcc \
        libressl-dev \
        musl-dev \
        musl \
        libffi-dev \
        libxml2 \
        libxml2-dev \
        libxslt-dev
        # libxslt-dev

# Creating folders, and files for a project:
COPY ./ ./

CMD [ "python", "main.py"]
