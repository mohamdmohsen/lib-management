from django.urls import path , include
from .views import register,  forgot_password,reset_password
urlpatterns = [
    path("register/",register,name="register" ),
    path("forgot-password/",forgot_password,name="forgot-password"),
    path("reset-password/",reset_password,name="reset-password"),
      
]
