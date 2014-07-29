from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-googleanalyticsbasic',
    version=version,
    description="Basic extension to add google analytics tracking code in page header",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Yatin Khadilkar',
    author_email='ykhadilkar@reisys.com',
    url='data.gov',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.googleanalyticsbasic'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
        [ckan.plugins]
        googleanalyticsbasic=ckanext.googleanalyticsbasic.plugin:GoogleAnalyticsBasicPlugin

    """,
)
