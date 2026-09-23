from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,generics

from .models import User
from .serializer import SignUpSerializer,ForgotPasswordSerializer ,ResetPasswordSerializer
from django.contrib.auth.hashers import make_password
from django_ratelimit.decorators import ratelimit
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# Create your views here.

@api_view(['POST'])
@ratelimit(key='ip', rate='5/m',method='POST',block=True)
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

User = get_user_model()
@api_view(["POST"])

def forgot_password(request):

    serializer = ForgotPasswordSerializer(
        data=request.data
    )

    serializer.is_valid(raise_exception=True)

    email = serializer.validated_data["email"]

    user = User.objects.get(email=email)

    uid = urlsafe_base64_encode(
        force_bytes(user.pk)
    )

    token = default_token_generator.make_token(user)

    reset_link = (
        f"http://127.0.0.1:3000/reset-password/"
        f"{uid}/{token}/"
    )

    send_mail(
        subject="Reset your password",
        message=(
            "You requested a password reset.\n\n"
            f"Reset your password using this link:\n"
            f"{reset_link}\n\n"
            "If you did not request this, ignore this email."
        ),
        from_email=None,
        recipient_list=[user.email],
        fail_silently=False,
    )

    return Response({
        "message": "Password reset email sent."
    })

@api_view(["POST"])

def reset_password(request):

    serializer = ResetPasswordSerializer(
        data=request.data
    )

    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data["user"]

    user.set_password(
        serializer.validated_data["password"]
    )

    user.save()

    return Response({
        "message": "Password has been reset successfully."
    })