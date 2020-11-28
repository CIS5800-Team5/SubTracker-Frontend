from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

#@login_required(login_url='/oauth/login/azuread-b2c-oauth2/')
#def subscriptions(request):
#    return render(request, 'subscriptions.html')

@login_required(login_url='/oauth/login/azuread-b2c-oauth2/')
def profile(request):
    return render(request, 'profile.html')

import json, requests
@login_required(login_url='/oauth/login/azuread-b2c-oauth2/')
def subscriptions(request):
    services = list()
    url = "https://subtrackerapi.azurewebsites.net/api/services/all"
    response = requests.get(url)
    data = json.loads(response.text)

    for i in range(0, len(data)):
        service = data[i]['service_name']
        services.append(service)
    return render(request,"subscriptions.html", {'services': sorted(services)})
