from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')


def logout_sys(request):
    logout(request)
    return redirect('home')
