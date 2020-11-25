from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'index.html')
def signin(request):
    return render(request, 'signin.html')
def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')
    return redirect('index')
@login_required
def subscriptions(request):
    return render(request, 'subscriptions.html')
@login_required
def profile(request):
    return render(request, 'profile.html')
