ARG CKAN_VERSION=2.9
FROM openknowledge/ckan-dev:${CKAN_VERSION}

COPY . /app
WORKDIR /app

RUN pip install -r dev-requirements.txt -e .
