from django.shortcuts import render
from django.urls import path
from customer import views
from .views import registration
from .views import login

urlpatterns = [
    path("customer/registration/", registration.as_view(), name="registration"),
    path("customer/login/", login.as_view(), name="login"),
]
