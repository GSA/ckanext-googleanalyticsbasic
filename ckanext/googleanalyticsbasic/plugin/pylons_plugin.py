"""
Mixin for Pylons-specific functionality. This aides the migration between Pylons and Flask.
"""
import logging
import ckan.lib.helpers as h
import ckan.plugins as p

log = logging.getLogger('ckanext.googleanalytics-basic')


class MixinPlugin(object):

    def configure(self, config):
        '''Load config settings for this extension from config file.

        See IConfigurable.

        '''
        self.googleanalytics_ids = []
        if 'googleanalytics.ids' not in config:
            msg = "Missing googleanalytics.ids in config"
            log.warn(msg)
            return
            # raise GoogleAnalyticsBasicException(msg)

        self.googleanalytics_ids = config['googleanalytics.ids'].split()

        self.googleanalytics_javascript_url = h.url_for_static(
            '/scripts/ckanext-googleanalytics.js')

    # IConfigurer
    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        p.toolkit.add_template_directory(config, '../templates/templates_2_8')
        p.toolkit.add_public_directory(config, '../public')
        p.toolkit.add_resource('../fanstatic', 'googleanalyticsbasic')
