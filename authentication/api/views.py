from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        # user = request.data.get('user', {}) 를 했을 경우
        # 받은 json 값을 불러오지 못하고 있음. 이 부분을 reqest.data로 받아오면서 해결함
        user = request.data

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familier with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)