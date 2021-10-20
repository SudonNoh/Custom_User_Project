from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ArticleViewSet, CommentsListCreateAPIView, CommentsDestroyAPIView,
    ArticlesFavoriteAPIView,
)

# APPEND_SLASH=False : When use trailing_slash, you should put it in settings.
router = DefaultRouter(trailing_slash=False)
router.register(r'', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<slug:article_slug>/comments', CommentsListCreateAPIView.as_view()),
    path('<slug:article_slug>/comments/<int:comment_pk>', CommentsDestroyAPIView.as_view()),
    path('<slug:article_slug>/favorite', ArticlesFavoriteAPIView.as_view())
]