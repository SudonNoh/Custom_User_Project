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
        print('authentication/api/viws.py request        ', request)
        print('authentication/api/viws.py reqeust.data.get()       ', request.data.get())
        user = request.data.get('user', {})

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familier with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)