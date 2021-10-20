from functools import partial
from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from articles.models import Article, Comment
from .renderers import ArticleJSONRenderer, CommentJSONRenderer
from .serializers import ArticleSerializer, CommentSerializer


# CreateModelMixin  provides a ".create(request, *args, **kwargs)" method,
# that implements creating and saving a new model instance.
# If an object is created this returns a "201 Created" response, with a
# serialized representation of the object as the body of the reponse.
# If the representation contains a key named "url", then the "Location"
# header of the response will be populated with that value.
class ArticleViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin, 
    viewsets.GenericViewSet
    ):
    
    lookup_field = 'slug'
    queryset = Article.objects.select_related('author', 'author__user')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (ArticleJSONRenderer,)
    serializer_class = ArticleSerializer

    def create(self, request):
        serializer_context = {
            'author': request.user.profile,
            'request': request
            }
        print('article/api/views/articleviewset/create \n serializer_context:   ', serializer_context)
        
        serializer_data = request.data
        print('article/api/views/articleviewset/create \n serializer_data:   ', serializer_data)
        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        print('article/api/views/articleviewset/create \n serializer:   ', serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer_data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, slug):
        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Article.DoesNotExist:
            raise NotFound('An article with this slug does not exist.')
        
        serializer = self.serializer_class(serializer_instance)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, slug):
        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Article.DoesNotExist:
            raise NotFound('An article wth this slug does not exist.')
        
        serializer_data = request.data
        
        serializer = self.serializer_class(
            serializer_instance, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentsListCreateAPIView(generics.ListCreateAPIView):
    lookup_field = 'article__slug'
    lookup_url_kwarg = 'article_slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # select_related : select 할 객체가 역참조하는 single object(one-to-one or more-to-one)이거나
    # 또는 정참조 foreign key 일 때 사용
    # 여러 개의 parameter 를 가질 수 있음
    # ex) Comment.objects.filter(id=1).select_related('article', 'article__author').values(*fields)
    queryset = Comment.objects.select_related(
        'article', 'article__author', 'article__author__user',
        'author', 'author__user'
    )
    renderer_classes = (CommentJSONRenderer, )
    serializer_class = CommentSerializer
    
    def filter_queryset(self, queryset):
        # The built-in list function calls `filter_queryset`. Since we only
        # want comments for a specific article, this is a good place to do
        # that filtering.
        filters = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        
        return queryset.filter(**filters)
    
    def post(self, request, article_slug=None):
        data = request.data
        context = {'author': request.user.profile}
        
        try:
            context['article'] = Article.objects.get(slug=article_slug)
        except Article.DoesNotExist:
            raise NotFound('An article with this slug does not exist.')

        serializer = self.serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentsDestroyAPIView(generics.DestroyAPIView):
    lookup_url_kwarg = 'comment_pk'
    permisssion_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()
    
    def delete(self, request, article_slug=None, comment_pk=None):
        try:
            comment = Comment.objects.get(pk=comment_pk)
        except Comment.DoesNotExist:
            raise NotFound('A comment with this ID does not exist.')
        
        comment.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

