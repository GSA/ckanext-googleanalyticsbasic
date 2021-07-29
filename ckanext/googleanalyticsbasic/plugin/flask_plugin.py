"""
Mixin for Flask-specific functionality. This aides the migration between Pylons and Flask.
"""
import logging
import ckan.lib.helpers as h
import ckan.plugins as p
import flask

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

        app = flask.Flask(__name__)
        app.config['SERVER_NAME'] = "app"
        with app.app_context(), app.test_request_context():
            self.googleanalytics_javascript_url = h.url_for_static(
                '/scripts/ckanext-googleanalytics.js')

    # IConfigurer
    def update_config(self, config):
        # TODO remove template/templates_2_8 and move templates/templates_new
        # to templates once we're off of CKAN 2.8.
        #
        # Using a separate dir for templates avoids having to maintain
        # backwards compatibility using a sprinkling of conditionals. We don't
        # anticipate adding new features to the existing 2.8 templates.
        p.toolkit.add_template_directory(config, '../templates/templates_new')
        p.toolkit.add_public_directory(config, '../public')
        p.toolkit.add_resource('../fanstatic', 'googleanalyticsbasic')
