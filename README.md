[![Github Actions](https://github.com/GSA/ckanext-googleanalyticsbasic/actions/workflows/test.yml/badge.svg)](https://github.com/GSA/ckanext-googleanalyticsbasic/actions)
[![PyPI version](https://badge.fury.io/py/ckanext-googleanalyticsbasic.svg)](https://badge.fury.io/py/ckanext-googleanalyticsbasic)


ckanext-googleanalyticsbasic
============================

Puts the Google Analytics asynchronous tracking code into your page headers for basic Google Analytics page tracking.

Installation
-------------
1. Install the extension as usual, e.g. (from an activated virtualenv)
		::
		
		$ pip install -e  git+https://github.com/GSA/ckanext-googleanalyticsbasic#egg=ckanext-googleanalyticsbasic

2. Edit your development.ini (or similar) to provide space separated list of google ids
		::
  	
		googleanalytics.ids = UA-1010101-1 UA-1010101-2

3. Edit again your configuration ini file to activate the plugin with:
		::
  	
		ckan.plugins = googleanalyticsbasic

### Compatibility

This extension is compatible with these versions of CKAN.

CKAN version | Compatibility
------------ | -------------
<=2.8        | no
2.9          | yes

## Tests

All the tests live in the [/ckanext/geodatagov/tests](/ckanext/geodatagov/tests) folder.

## Using the Docker Dev Environment

### Build Environment

To start environment, run:
```docker-compose build```
```docker-compose up```

CKAN will start at localhost:5000

To shut down environment, run:

```docker-compose down```

To docker exec into the CKAN image, run:

```docker-compose exec app /bin/bash```

### Testing

They follow the guidelines for [testing CKAN
extensions](https://docs.ckan.org/en/2.9/extensions/testing-extensions.html#testing-extensions).

To run the extension tests, start the containers with `make up`, then:

    $ make test

Lint the code.

    $ make lint

### Matrix builds

The development environment drops as many dependencies as possible. It is
not meant to have feature parity with
[GSA/catalog.data.gov](https://github.com/GSA/catalog.data.gov/). Tests should
mock external dependencies where possible.

In order to support multiple versions of CKAN, or even upgrade to new versions
of CKAN, we support development and testing through the `CKAN_VERSION`
environment variable.

    $ make CKAN_VERSION=2.9 test
