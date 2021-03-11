from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("", views.home, name="home"),
    path("testing", views.testing, name="testing"),
    path("logout", views.logout, name="logout"),
    path("registration", views.registration, name="registration"),
]
