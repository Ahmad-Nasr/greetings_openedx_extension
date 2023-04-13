
def plugin_settings(settings):
    """
    Defines greetings app settings when app is used as a plugin to edx-platform.
    See: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """

    settings.GREETING_SERVICE_USER_NAME = getattr(settings, 'ENV_TOKENS', {}).get(
        'GREETING_SERVICE_USER_NAME',
        settings.GREETING_SERVICE_USER_NAME
    )
    settings.GREETING_SERVICE_USER_EMAIL = getattr(settings, 'ENV_TOKENS', {}).get(
        'GREETING_SERVICE_USER_EMAIL',
        settings.GREETING_SERVICE_USER_EMAIL
    )
    settings.GREETING_SERVICE_CLIENT_APP_NAME = getattr(settings, 'ENV_TOKENS', {}).get(
        'GREETING_SERVICE_CLIENT_APP_NAME',
        settings.GREETING_SERVICE_CLIENT_APP_NAME
    )
