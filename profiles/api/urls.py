from django.urls import path, include

from .views import ProfileRetrieveAPIView

urlpatterns = [
    path('<int:pk>', ProfileRetrieveAPIView.as_view()),
]