from .views import GreetingAPIView
from django.urls import path
from rest_framework.routers import DefaultRouter


router_v1 = DefaultRouter('v1')

app_name = "greetings"
urlpatterns = [
    path('submit-greeting', GreetingAPIView.as_view(), name="submit_greeting"),
] + router_v1.urls
