from django.urls import path, include
from rest_framework import routers
from .views import (
    RegistrationAPIView, LoginAPIView, UserRetriveUpdateAPIView
)


urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('update', UserRetriveUpdateAPIView.as_view()),
]


