from django.urls import path
from rest_framework.routers import DefaultRouter


router_v1 = DefaultRouter('v1')

app_name = "greetings"
urlpatterns = [

] + router_v1.urls
