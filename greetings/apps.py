"""
greetings Django application initialization.
"""
from edx_django_utils.plugins.constants import (
    PluginURLs, PluginSettings,
)

from django.apps import AppConfig


class GreetingsConfig(AppConfig):
    """
    Configuration for the greetings Django application.
    """

    name = 'greetings'

    plugin_app = {

        PluginURLs.CONFIG: {

            'lms.djangoapp': {

                # The namespace to provide to django's urls.include.
                PluginURLs.NAMESPACE: 'greetings',

                # The application namespace to provide to django's urls.include.
                # Optional; Defaults to None.
                PluginURLs.APP_NAME: 'greetings',

                # The regex to provide to django's urls.url.
                # Optional; Defaults to r''.
                PluginURLs.REGEX: r'^api/greetings/',

                # The python path (relative to this app) to the URLs module to be plugged into the project.
                # Optional; Defaults to 'urls'.
                PluginURLs.RELATIVE_PATH: 'api.routers',
            }
        },

        PluginSettings.CONFIG: {
            'lms.djangoapp': {
                'production': {
                    PluginSettings.RELATIVE_PATH: 'settings.production',
                },
                'common': {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
            }
        },
    }

    def ready(self):
        pass
