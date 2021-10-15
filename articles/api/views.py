from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from articles.models import Article
from .renderers import ArticleJSONRenderer
from .serializers import ArticleSerializer


# CreateModelMixin  provides a ".create(request, *args, **kwargs)" method,
# that implements creating and saving a new model instance.
# If an object is created this returns a "201 Created" response, with a
# serialized representation of the object as the body of the reponse.
# If the representation contains a key named "url", then the "Location"
# header of the response will be populated with that value.
class ArticleViewSet(
    mixins.CreateModelMixin, 
    viewsets.GenericViewSet
    ):
    
    queryset = Article.objects.select_related('author', 'author__user')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (ArticleJSONRenderer,)
    serializer_class = ArticleSerializer

    def create(self, request):
        serializer_context = {'author': request.user.profile}
        serializer_data = request.data
        print('serializer_data:', serializer_data)
        
        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer_data, status=status.HTTP_201_CREATED)