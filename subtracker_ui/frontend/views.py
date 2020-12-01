from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings

import logging
# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)





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
            logger.debug(subscriptions_response.text)
            subscriptions_data = json.loads(subscriptions_response.text)

        if subscriptions_data:
            return render(request,"subscriptions.html", {'services': services_sorted, 'subscriptions_data':subscriptions_data})
        else:
            return render(request,"subscriptions.html", {'services': services_sorted})

def index(request):
	if request.method == "POST":
		message_name = request.POST['name']
		message_email = request.POST['email']
		message_subject = request.POST['subject']
		message = request.POST['message']
		
		send_mail(
		'Message from' + message_name + ':' + message_subject,
		message,
		message_email,
		['subtrackertest@gmail.com'],
		fail_silently=False)
	else:
		return render(request,"index.html")
		
