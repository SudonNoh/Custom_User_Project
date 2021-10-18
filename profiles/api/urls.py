from django.urls import path, include

from .views import ProfileRetrieveAPIView

urlpatterns = [
    path('<str:username>', ProfileRetrieveAPIView.as_view()),
]