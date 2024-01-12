from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)

            return redirect('form')

        else:
            messages.info(request, 'invalid user')
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')

    return render(request, 'register.html')


def form(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.create_user(username=username,email=email)
        user.save()
        print('application is confirmed')
        return redirect('index')
    else:
        print('complete the form')
    return render(request, 'form.html')