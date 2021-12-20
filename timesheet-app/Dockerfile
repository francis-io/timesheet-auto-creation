FROM python:3.10-alpine

# https://github.com/terraform-compliance/cli/issues/192#issuecomment-654309628
#RUN apk add --no-cache libxml2 libxslt libxml2-dev libxslt-dev #python3-dev gcc build-base

# https://github.com/FrederikP/python-poetry-alpine/blob/master/Dockerfile
#ARG POETRY_VERSION=1.1.12

# RUN apk add --no-cache \
#         libxml2 \
#         libxml2-dev \
#         libxslt \
#         libxslt-dev \
#         curl \
#         gcc \
#         libressl-dev \
#         musl-dev \
#         libffi-dev && \
#     curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile=minimal && \
#     source $HOME/.cargo/env && \
#     pip install --no-cache-dir poetry && \
#     apk del \
#         curl \
#         gcc \
#         libressl-dev \
#         musl-dev \
#         libffi-dev \
#         libxml2\
#         libxml2-dev \
#         libxslt \
#         libxslt-dev

# RUN apk add --no-cache \
#         libxml2 \
#         libxml2-dev \
#         libxslt \
#         libxslt-dev \
#         curl \
#         gcc \
#         libressl-dev \
#         musl-dev \
#         libffi-dev && \
#     curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile=minimal && \
#     source $HOME/.cargo/env && \
#     pip install --no-cache-dir poetry && \
#     apk del \
#         curl \
#         gcc \
#         libressl-dev \
#         musl-dev \
#         libffi-dev \
#         libxml2\
#         libxml2-dev \
#         libxslt \
#         libxslt-dev

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
#COPY pyproject.toml ./

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
        libxml2\
        libxml2-dev \
        libxslt \
        libxslt-dev

# # Project initialization:
# RUN poetry config virtualenvs.create false \
#   && poetry install --no-dev --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY ./ ./

#COPY timesheet-app/timesheet_app /web/


CMD [ "python", "main.py"]
