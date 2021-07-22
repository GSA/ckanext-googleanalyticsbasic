__author__ = 'GSA'
import ckan.plugins as p

try:
    p.toolkit.requires_ckan_version("2.9")
except p.toolkit.CkanVersionException:
    from ckanext.googleanalyticsbasic.plugin.pylons_plugin import MixinPlugin
else:
    from ckanext.googleanalyticsbasic.plugin.flask_plugin import MixinPlugin


class GoogleAnalyticsBasicException(Exception):
    pass


class GoogleAnalyticsBasicPlugin(MixinPlugin, p.SingletonPlugin):
    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.ITemplateHelpers)

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
