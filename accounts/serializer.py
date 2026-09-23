from rest_framework import serializers
from .models import User


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

