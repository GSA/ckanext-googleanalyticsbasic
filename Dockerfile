ARG CKAN_VERSION=2.8
FROM openknowledge/ckan-dev:${CKAN_VERSION}

# RUN apk add geos-dev proj proj-util proj-dev

COPY . /app
WORKDIR /app

RUN pip install -r dev-requirements.txt -e .
