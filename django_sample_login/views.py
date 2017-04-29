from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login(request):
    return render(request, 'login.html', {})
