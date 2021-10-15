from rest_framework import serializers

from profiles.api.serializers import ProfileSerializer

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    