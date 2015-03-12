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

