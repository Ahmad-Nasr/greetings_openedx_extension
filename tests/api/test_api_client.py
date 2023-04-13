import pytest
from unittest.mock import Mock

from rest_framework import status, response


class TestAPIClient:

    @pytest.mark.parametrize("greeting_msg", ["goodbye"])
    @pytest.mark.django_db
    def test_submit_greeting(self, greeting_api_client, greeting_msg):
        """
        Test case submit_greeting method of the greetings API client.
        """
        SUCCESSFUL_RESPONSE = Mock(spec=response.Response)
        SUCCESSFUL_RESPONSE.status_code = status.HTTP_200_OK
        mocked_post = Mock(return_value=SUCCESSFUL_RESPONSE)
        greeting_api_client.client.post = mocked_post

        success = greeting_api_client.submit_greeting(greeting_msg)

        assert success
