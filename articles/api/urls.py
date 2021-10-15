from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet

# APPEND_SLASH=False : When use trailing_slash, you should put it in settings.
router = DefaultRouter(trailing_slash=False)
router.register(r'create', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]