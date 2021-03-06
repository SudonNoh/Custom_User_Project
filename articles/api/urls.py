from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ArticleViewSet, CommentsListCreateAPIView, CommentsDestroyAPIView,
    ArticlesFavoriteAPIView, TagListAPIView, ArticlesFeedAPIView
)

# APPEND_SLASH=False : When use trailing_slash, you should put it in settings.
router = DefaultRouter(trailing_slash=False)
router.register(r'title', ArticleViewSet)

urlpatterns = [
    path('feed', ArticlesFeedAPIView.as_view()),
    path('', include(router.urls)),
    path('title/<slug:article_slug>/comments', CommentsListCreateAPIView.as_view()),
    path('title/<slug:article_slug>/comments/<int:comment_pk>', CommentsDestroyAPIView.as_view()),
    path('title/<slug:article_slug>/favorite', ArticlesFavoriteAPIView.as_view()),
    path('tags', TagListAPIView.as_view()),
]