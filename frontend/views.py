from django.http import HttpResponse
from django.shortcuts import render
import requests


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'index.html')
def signin(request):
    return render(request, 'signin.html')
