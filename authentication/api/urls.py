from django.urls import path, include
from rest_framework import routers
from .views import (
    RegistrationAPIView, LoginAPIView
)


urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]


