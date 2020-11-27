from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'index.html')
def user(request):
    return render(request, 'user.html')
def login(request):
    #return render(request, 'login.html')
    if request.user.is_authenticated:
        return redirect('subscriptions')
    else:
        return redirect('http://localhost:8000/oauth/login/azuread-b2c-oauth2/')
def logout(request):
    auth.logout(request)
    #return render(request, 'logout.html')
    return redirect('index')
@login_required(login_url='http://localhost:8000/oauth/login/azuread-b2c-oauth2/')
def subscriptions(request):
    return render(request, 'subscriptions.html')
@login_required(login_url='http://localhost:8000/oauth/login/azuread-b2c-oauth2/')
def profile(request):
    return render(request, 'profile.html')
