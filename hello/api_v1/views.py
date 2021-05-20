from django.http.response import HttpResponse
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.

def add(request):
    num = json.loads(request.body)
    if num['A'] and num['B']:
        total = num['A'] + num['B']
        response_data = {
            'result': str(total),
            'method': request.method
        }

    response = HttpResponse(json.dumps(response_data))
    response['Content-Type'] = 'application/json'
    return response

def subtract(request):
    num = json.loads(request.body)
    if num['A'] and num['B']:
        total = num['A'] - num['B']
        response_data = {
            'result': str(total),
            'method': request.method
        }

    response = HttpResponse(json.dumps(response_data))
    response['Content-Type'] = 'application/json'
    return response

def multiply(request):
    num = json.loads(request.body)
    if num['A'] and num['B']:
        total = num['A'] * num['B']
        response_data = {
            'result': str(total),
            'method': request.method
        }
    

    response = HttpResponse(json.dumps(response_data))
    response['Content-Type'] = 'application/json'
    return response

def divide(request):
    try:
        num = json.loads(request.body)
        if num['A'] and num['B']:
            total = num['A'] // num['B']
            response_data = {
                'result': str(total),
                'method': request.method
            }
    except:
        if num['A'] or num['B'] == 0:
            response_data = {
                'result': 'Division by zero!',
                'method': request.method
            }

    response = HttpResponse(json.dumps(response_data))
    response['Content-Type'] = 'application/json'
    return response