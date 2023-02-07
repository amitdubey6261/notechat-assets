from email import message
from pickle import FROZENSET
from telnetlib import LOGOUT
from turtle import home
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.core.mail import send_mail


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        pass1 = request.POST['pass1']
        
    return render(request , 'authentication/login.html' , {})

def signup(request):
    return render(request , 'authentication/signup.html' , {} )
