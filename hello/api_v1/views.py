from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_first_api_view(request):
    response = HttpResponse()
    response['Content-Type'] = 'application/json'