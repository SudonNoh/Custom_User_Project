from re import search
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import (
    RegistrationSerializer, LoginSerializer, UserSerializer,
)
from authentication.renderers import UserJSONRenderer


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
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


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer
    
    def post(self, request):
        user = request.data
        
        # Notice here that we do not call 'serializer.save()' like we did for
        # the registration endpoint. This is because we don't actually have
        # anything to save. Instead, the 'validate' method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class UserRetriveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer
    
    def retrieve(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our 'User' object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)
        
        return Response(serializer.data, statu=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True 
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print("Seriaizer.data   :   ", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
