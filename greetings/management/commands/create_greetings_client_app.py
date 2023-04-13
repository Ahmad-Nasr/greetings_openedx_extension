import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model
from oauth2_provider.models import get_application_model

logger = logging.getLogger(__name__)
ITEM_CREATION_LOG_MESSAGE = "'%s' has been created"

User = get_user_model()
Application = get_application_model()


class Command(BaseCommand):
    help = 'Creates a user and an OAuth2 application/client needed for the greetings service API client'

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(
            username=settings.GREETING_SERVICE_USER_NAME, email=settings.GREETING_SERVICE_USER_EMAIL)
        logger.info(ITEM_CREATION_LOG_MESSAGE, settings.GREETING_SERVICE_USER_NAME)

        oauth_client_app, created = Application.objects.get_or_create(
            user=user,
            name=settings.GREETING_SERVICE_CLIENT_APP_NAME,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS,
        )
        logger.info(ITEM_CREATION_LOG_MESSAGE, settings.GREETING_SERVICE_CLIENT_APP_NAME)
