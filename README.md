[![Github Actions](https://github.com/GSA/ckanext-googleanalyticsbasic/actions/workflows/test.yml/badge.svg)](https://github.com/GSA/ckanext-googleanalyticsbasic/actions)
[![CircleCI](https://circleci.com/gh/GSA/ckanext-googleanalyticsbasic.svg?style=svg)](https://circleci.com/gh/GSA/ckanext-googleanalyticsbasic)


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
<=2.7        | no
2.8          | yes
2.9          | [complete](https://github.com/GSA/datagov-ckan-multi/issues/570)

## Tests

All the tests live in the [/ckanext/geodatagov/tests](/ckanext/geodatagov/tests) folder. After each commit, via the [CircleCI config](https://github.com/GSA/ckanext-geodatagov/blob/master/.circleci/config.yml), this tests will [run in CircleCI](https://circleci.com/gh/GSA/ckanext-geodatagov) with CKAN 2.3 (custom GSA fork) and CKAN 2.8.  The CircleCI tests were not retained, but may be revisited in the future.

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
extensions](https://docs.ckan.org/en/2.8/extensions/testing-extensions.html#testing-extensions).

To run the extension tests, start the containers with `make up`, then:

    $ make test

Lint the code.

    $ make lint

### Matrix builds

The existing development environment assumes a full catalog.data.gov test setup. This makes
it difficult to develop and test against new versions of CKAN (or really any
dependency) because everything is tightly coupled and would require us to
upgrade everything at once which doesn't really work. A new make target
`test-new` is introduced with a new docker-compose file.

The "new" development environment drops as many dependencies as possible. It is
not meant to have feature parity with
[GSA/catalog.data.gov](https://github.com/GSA/catalog.data.gov/). Tests should
mock external dependencies where possible.

In order to support multiple versions of CKAN, or even upgrade to new versions
of CKAN, we support development and testing through the `CKAN_VERSION`
environment variable.

    $ make CKAN_VERSION=2.8 test
    $ make CKAN_VERSION=2.9 test
