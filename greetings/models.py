"""
Database models for greetings application.
"""
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

User = get_user_model()


class Greeting(TimeStampedModel):
    """
    Greeting model stores students' greetings
    """

    greeting = models.CharField(_('Greeting'), max_length=128)
    user = models.ForeignKey(User, related_name='greetings', on_delete=models.CASCADE)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return f"Greetings: {self.greeting}, ID: {self.id}, from: {self.user}>"
