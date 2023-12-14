import random
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, ConfirmCodeSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ConfirmCode
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import UserCreateSerializer, UserLoginSerializer, ConfirmCodeSerializer
from rest_framework.views import APIView


class UserRegisterAPIView(APIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        # email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.create_user(username=username, password=password, is_active=False)
        confirm = ConfirmCode.objects.create(user=user, code=random.randint(100000, 999999))
        return Response({'success': 'User created successfully', 'code': confirm.code},
                        status=status.HTTP_201_CREATED)


class UserConfirmAPIView(APIView):
    serializer_class = ConfirmCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        confirmation = get_object_or_404(ConfirmCode, code=code)
        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete()
        return Response({'status': 'User activated'}, status=status.HTTP_200_OK)





# @api_view(['POST'])
# def confirm_user_api_view(request):
#     serializer = ConfirmCodeSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     code = serializer.validated_data.get('code')
#     confirm = get_object_or_404(ConfirmCode, code=code)
#     user = confirm.user
#     user.is_active = True
#     user.save()
#     return Response({'success': 'User confirmed successfully'},
#                     status=status.HTTP_200_OK)

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
