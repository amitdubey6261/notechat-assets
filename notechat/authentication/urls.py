from django import views
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.login , name = 'loginpage'),
    path('signup/' , views.signup  , name = 'sigiuppage'),
]
