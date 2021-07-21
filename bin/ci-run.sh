#!/bin/sh -e

echo "TESTING ckanext-googleanalyticsbasic"
nosetests --ckan --with-pylons=subdir/test.ini ckanext/googleanalyticsbasic/tests
