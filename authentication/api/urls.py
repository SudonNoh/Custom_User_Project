from django.urls import path, include
from rest_framework import routers
from .views import RegistrationAPIView


urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
]


