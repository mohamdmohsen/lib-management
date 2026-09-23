from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,generics

from .models import User
from .serializer import SignUpSerializer
from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['POST'])
def register(request):
   
    serializer = SignUpSerializer(data = request.data)

    if serializer.is_valid():   
        data = serializer.validated_data
        password = make_password(data['password'])   
       
        user = User.objects.create(
        username=data['username'],
        email=data['email'],
        password=password,
)
        return Response(serializer.data,status=status.HTTP_201_CREATED) 
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

