#!/bin/sh -e

echo "TESTING ckanext-googleanalyticsbasic"
nosetests --ckan --with-pylons=subdir/test-legacy.ini ckanext/googleanalyticsbasic/tests/nose
