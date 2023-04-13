import pytest

from django.core.management import call_command

from rest_framework.test import APIClient

from greetings.api.api_client import GreetingAPIClient
from greetings.management.commands.create_greetings_client_app import Command


@pytest.fixture
def authenticated_DRF_client(admin_user):
    client = APIClient()
    client.force_authenticate(user=admin_user)
    return client


@pytest.fixture
def greeting_api_client():
    call_command(Command())
    return GreetingAPIClient()
