from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('backend/', views.user_admin, name = "backend"),
    path('frontend/', views.user_guest, name = "frontend"),

    # User SignUp, SignIn & SignOut
    path('register', views.register, name = "register")
]