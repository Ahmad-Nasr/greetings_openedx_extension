import logging
from urllib.parse import urljoin
from requests.exceptions import HTTPError, RequestException

from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status

from edx_rest_api_client.client import OAuthAPIClient
from oauth2_provider.models import get_application_model


logger = logging.getLogger(__name__)
ITEM_NOT_EXIST_LOG_MESSAGE = " '%s' does not exist, call the create_greetings_client_app command!"

User = get_user_model()
Application = get_application_model()


class GreetingAPIClient:
    """
    API client for calls to the greeting app endpoints
    """

    client = None

    def __init__(self) -> None:

        try:
            user = User.objects.get(
                username=settings.GREETING_SERVICE_USER_NAME,
                email=settings.GREETING_SERVICE_USER_EMAIL)
            oauth_client_app = Application.objects.get(
                user=user,
                name=settings.GREETING_SERVICE_CLIENT_APP_NAME,
                client_type=Application.CLIENT_CONFIDENTIAL,
                authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS,)

            GreetingAPIClient.client = OAuthAPIClient(
                settings.LMS_ROOT_URL,
                oauth_client_app.client_id,
                oauth_client_app.client_secret)

        except User.DoesNotExist:
            logger.error(ITEM_NOT_EXIST_LOG_MESSAGE, settings.GREETING_SERVICE_USER_NAME)
        except Application.DoesNotExist:
            logger.error(ITEM_NOT_EXIST_LOG_MESSAGE, settings.GREETING_SERVICE_CLIENT_APP_NAME)

    @ classmethod
    def submit_greeting(cls, greeting_msg):
        """
        Submit greeting message through an API call
        """
        greeting_endpoint_url = urljoin(settings.LMS_ROOT_URL, reverse("greetings:submit_greeting"))

        try:
            response = cls.client.post(greeting_endpoint_url, data={"greeting": greeting_msg})
            if response.status_code == status.HTTP_200_OK:
                return True
            return False
        except (HTTPError, RequestException) as exc:
            logger.warning(
                "Unable to sumbit the greeting message. " f"Exception: {exc}"
            )
            return False
