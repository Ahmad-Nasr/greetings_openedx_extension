import logging

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions

from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from drf_yasg.utils import swagger_auto_schema

from ..models import Greeting
from .serializers import GreetingSerializer
from .api_client import GreetingAPIClient

logger = logging.getLogger(__name__)
GREETING_SUBMISSION_LOG_MESSAGE = "User '%s' submitted '%s'"


class GreetingAPIView(GenericAPIView):
    authentication_classes = (JwtAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GreetingSerializer

    @swagger_auto_schema(operation_description="Sumbit student's greeting to admin dashboard")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        greeting_msg = serializer.validated_data["greeting"]
        logger.info(GREETING_SUBMISSION_LOG_MESSAGE, request.user, greeting_msg)
        Greeting.objects.create(greeting=greeting_msg, user=request.user)

        if greeting_msg.strip().lower() == "hello":
            api_client = GreetingAPIClient()
            success = api_client.submit_greeting("goodbye")
            return Response(status=status.HTTP_200_OK) if success else Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_200_OK)
