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

@login_required(login_url='/oauth/login/azuread-b2c-oauth2/')
def profile(request):
    return render(request, 'profile.html')

import json, requests
@login_required(login_url='/oauth/login/azuread-b2c-oauth2/')
def subscriptions(request):
    if request.method == "POST":
        pass
    else:
        services = {}
        services_url = "https://subtrackerapi.azurewebsites.net/api/services/all"
        services_response = requests.get(services_url)
        services_data = json.loads(services_response.text)

        for i in range(0, len(services_data)):
            services[i] = services_data[i]['service_name']
        services_sorted = dict(sorted(services.items(), key = lambda kv:kv[1]))

        subscriptions_service_name = {}
        subscriptions_cost = {}
        subscriptions_renewal = {}
        subscriptions_id = {}
        subscriptions_url = "https://subtrackerapi.azurewebsites.net/api/customers/getsubscriptions?customer_email=" + request.user.email
        subscriptions_response = requests.get(subscriptions_url)
        if subscriptions_response.text == "No data returned":
            pass
        else:
            subscriptions_data = json.loads(subscriptions_response.text)

        return render(request,"subscriptions.html", {'services': services_sorted, 'subscriptions_data':subscriptions_data})

