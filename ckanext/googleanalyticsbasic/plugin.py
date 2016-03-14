__author__ = 'GSA'
import logging
import ckan.lib.helpers as h
import ckan.plugins as p

log = logging.getLogger('ckanext.googleanalytics-basic')


class GoogleAnalyticsBasicException(Exception):
    pass


class GoogleAnalyticsBasicPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.ITemplateHelpers)

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

    def update_config(self, config):
        '''Change the CKAN (Pylons) environment configuration.

        See IConfigurer.

        '''
        p.toolkit.add_template_directory(config, 'templates')

        p.toolkit.add_resource('fanstatic', 'googleanalyticsbasic')

    def get_helpers(self):
        '''Return the CKAN 2.0 template helper functions this plugin provides.

        See ITemplateHelpers.

        '''
        return {'googleanalyticsbasic_header': self.googleanalyticsbasic_header}

    def googleanalyticsbasic_header(self):
        '''Render the googleanalytics_header snippet for CKAN 2.0 templates.

        This is a template helper function that renders the
        googleanalytics_header jinja snippet. To be called from the jinja
        templates in this extension, see ITemplateHelpers.

        Using enumerate() to implement multiple trackers support
        https://developers.google.com/analytics/devguides/collection/analyticsjs/advanced#multipletrackers

        '''
        data = {
            'googleanalytics_ids': enumerate(self.googleanalytics_ids, start=1)
        }

        return p.toolkit.render_snippet(
            'snippets/googleanalyticsbasic_header.html', data)
