from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from greetings.models import Greeting


class GreetingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Greeting
        fields = ('user', 'greeting',)

        extra_kwargs = {
            'greeting': {'required': True},
        }
