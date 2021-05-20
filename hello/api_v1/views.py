from django.http.response import HttpResponse, JsonResponse
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def add(request):
    num = request.body
    if num:
        nums = json.loads(num)
        try:
            nums['A'] = int(nums['A'])
            nums['B'] = int(nums['B'])
            total = nums['A'] + nums['B']
            response_data = {
                'result': str(total)
            }
            response = JsonResponse(response_data)
        except:
            respnse_data = {
                'result': 'Enter whole numbers'
            }
            response = JsonResponse(response_data)
            response.status_code = 400

def subtract(request):
    num = request.body
    if num:
        nums = json.loads(num)
        try:
            nums['A'] = int(nums['A'])
            nums['B'] = int(nums['B'])
            total = nums['A'] - nums['B']
            response_data = {
                'result': str(total)
            }
            response = JsonResponse(response_data)
        except:
            respnse_data = {
                'result': 'Enter whole numbers'
            }
            response = JsonResponse(response_data)
            response.status_code = 400

def multiply(request):
    num = request.body
    if num:
        nums = json.loads(num)
        try:
            nums['A'] = int(nums['A'])
            nums['B'] = int(nums['B'])
            total = nums['A'] * nums['B']
            response_data = {
                'result': str(total)
            }
            response = JsonResponse(response_data)
        except:
            respnse_data = {
                'result': 'Enter whole numbers'
            }
            response = JsonResponse(response_data)
            response.status_code = 400

def divide(request):
    num = request.body
    if num:
        nums = json.loads(num)
        try:
            nums['A'] = int(nums['A'])
            nums['B'] = int(nums['B'])
            total = nums['A'] // nums['B']
            response_data = {
                'result': str(total)
            }
            response = JsonResponse(response_data)
        except:
            respnse_data = {
                'result': 'Enter whole numbers'
            }
            response = JsonResponse(response_data)
            response.status_code = 400


