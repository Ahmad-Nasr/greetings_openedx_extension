import pytest

from rest_framework.test import APIClient


@pytest.fixture
def authenticated_DRF_client(admin_user):
    client = APIClient()
    client.force_authenticate(user=admin_user)
    return client
