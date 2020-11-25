from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'index.html')
def login(request):
    #return render(request, 'login.html')
    if request.user.is_authenticated:
        return redirect('../accounts/subscriptions')
    else:
        return redirect('http://localhost:8000/oauth/login/azuread-tenant-oauth2/')
def logout(request):
    auth.logout(request)
    #return render(request, 'logout.html')
    return redirect('index')
def subscriptions(request):
    if request.user.is_authenticated:
        return render(request, 'subscriptions.html')
    else:
        return redirect('http://localhost:8000/oauth/login/azuread-tenant-oauth2/')
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('http://localhost:8000/oauth/login/azuread-tenant-oauth2/')
