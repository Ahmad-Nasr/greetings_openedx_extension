import logging
import pytest
from urllib.parse import urljoin
from unittest.mock import Mock

from django.conf import settings
from django.urls import reverse

from rest_framework import status

from greetings.models import Greeting
from greetings.api.views import GREETING_SUBMISSION_LOG_MESSAGE
from greetings.api.api_client import GreetingAPIClient


class TestGreetingsAPIView:

    @pytest.mark.django_db
    def test_unauthenticated_access_denied(self, client):
        """
        Test case for unauthorized access denial.
        """
        greeting_endpoint_url = urljoin(settings.LMS_ROOT_URL, reverse("greetings:submit_greeting"))
        data = {'greetings': 'Hi'}

        response = client.post(greeting_endpoint_url, data, format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize("greeting_msg", ["non-Hello", "Hello"],
                             ids=['Case1: non-Hello message case', 'Case2: Hello message case'])
    @pytest.mark.django_db
    def test_submitting_message(self, authenticated_DRF_client, caplog, greeting_msg):
        """
        Test cases for submitting message with authorized access 
        """
        greeting_endpoint_url = urljoin(settings.LMS_ROOT_URL, reverse("greetings:submit_greeting"))

        mocked_submit_greeting = Mock(return_value=True)
        if greeting_msg == "Hello":
            GreetingAPIClient.submit_greeting = mocked_submit_greeting

        with caplog.at_level(logging.INFO):
            response = authenticated_DRF_client.post(greeting_endpoint_url, {'greeting': greeting_msg}, format='json')

        assert response.status_code == status.HTTP_200_OK
        query_set = Greeting.objects.filter(greeting=greeting_msg)
        assert len(query_set) == 1
        greeting_instance = query_set.first()
        assert greeting_instance.greeting == greeting_msg
        log_message = GREETING_SUBMISSION_LOG_MESSAGE % (
            greeting_instance.user, greeting_instance.greeting)
        assert log_message in caplog.text
        if greeting_msg == "Hello":
            mocked_submit_greeting.assert_called_once()
