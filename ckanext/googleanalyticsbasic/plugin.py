__author__ = 'ykhadilkar'
import logging
import ckan.lib.helpers as h
import ckan.plugins as p
import paste.deploy.converters as converters

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
        if 'googleanalytics.ids' not in config:
            msg = "Missing googleanalytics.ids in config"
            raise GoogleAnalyticsBasicException(msg)

        self.googleanalytics_ids = config['googleanalytics.ids'].split()

        self.googleanalytics_javascript_url = h.url_for_static(
                    '/scripts/ckanext-googleanalytics.js')

    def update_config(self, config):
        '''Change the CKAN (Pylons) environment configuration.

        See IConfigurer.

        '''
        p.toolkit.add_template_directory(config, 'templates')

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

        '''
        data = {'googleanalytics_ids': self.googleanalytics_ids}
        return p.toolkit.render_snippet(
            'googleanalyticsbasic/snippets/googleanalyticsbasic_header.html', data)
