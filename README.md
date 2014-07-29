ckanext-googleanalyticsbasic
============================

Puts the Google Analytics asynchronous tracking code into your page headers for basic Google Analytics page tracking.

Install the extension as usual, e.g. (from an activated virtualenv):

  $ pip install -e  git+https://github.com/ykhadilkar-rei/ckanext-googleanalyticsbasic#egg=ckanext-googleanalyticsbasic

Edit your development.ini (or similar) to provide these necessary parameters (you can provide up to 2 ids)

  googleanalytics.id_1 = UA-1010101-1
  googleanalytics.id_2 = UA-1010101-1

Edit again your configuration ini file to activate the plugin with:

  ckan.plugins = googleanalyticsbasic

TODO: Check if second id exist then add ... should not be required field 
