from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode


class SignUpSerializer(serializers.ModelSerializer):   
    password = serializers.CharField(write_only=True)
    password2 =serializers.CharField(write_only =True)
    class Meta:
        model = User
        fields = ("username","email","password","password2")

   
        extra_kwargs ={
            'username' :{'required' : True,'allow_blank':False},
            'email' : {'required': True,'allow_blank':False},
            'password' :{'required': True,'allow_blank':False},

        }    
    def validate(self, data):
        if data['password'] != data["password2"]:
                raise serializers.ValidationError("password do not match")
        return data


User = get_user_model()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        user = User.objects.filter(email=value).first()

        if not user:
            raise serializers.ValidationError(
                "No account found with this email."
            )

        return value


class ResetPasswordSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )
    password2 = serializers.CharField(
        write_only=True
    )

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({
                "password": "Passwords do not match."
            })

        try:
            uid = urlsafe_base64_decode(
                data["uid"]
            ).decode()

            user = User.objects.get(pk=uid)

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError({
                "uid": "Invalid user."
            })

        if not default_token_generator.check_token(
            user,
            data["token"]
        ):
            raise serializers.ValidationError({
                "token": "Invalid or expired reset token."
            })

        data["user"] = user

        return data