import pytest

from django.conf import settings
from django.core.management import call_command
from django.contrib.auth import get_user_model

from oauth2_provider.models import get_application_model

from greetings.management.commands.create_greetings_client_app import Command

User = get_user_model()
Application = get_application_model()


class TestCreateGreetingClientApp:
    """
    Test case for ``create_greetings_client_app`` management command.
    """
    @pytest.mark.django_db
    def test_create_greetings_client_app(self):
        call_command(Command())

        users = User.objects.filter(username=settings.GREETING_SERVICE_USER_NAME)
        assert len(users) == 1
        self.user = users[0]
        assert self.user.username == settings.GREETING_SERVICE_USER_NAME
        apps = Application.objects.filter(name=settings.GREETING_SERVICE_CLIENT_APP_NAME)
        assert len(apps) == 1
        application = apps[0]
        assert application.name == settings.GREETING_SERVICE_CLIENT_APP_NAME
        assert application.user == self.user
        assert application.authorization_grant_type == Application.GRANT_CLIENT_CREDENTIALS
        assert application.client_type == Application.CLIENT_CONFIDENTIAL
