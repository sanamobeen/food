from django.shortcuts import render
from django.urls import path
from customer import views
from .views import RegistrationView
from .views import LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)  
urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("customer/RegistrationView/", RegistrationView.as_view(), name="registration"),
    path("customer/LoginView/", LoginView.as_view(), name="login"),
]
