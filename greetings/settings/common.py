"""
Common settings for greetings project.
"""


def plugin_settings(settings):
    """
    Backend settings
    """
    settings.GREETING_SERVICE_USER_NAME = "greetings_service_user"
    settings.GREETING_SERVICE_USER_EMAIL = "greetings_service_user@fake.email"
    settings.GREETING_SERVICE_CLIENT_APP_NAME = "greetings_service_oauth_client_app"
