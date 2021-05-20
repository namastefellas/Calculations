import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def add(request, *args, **kwagrs):
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
            response_data = {
                'result': 'Enter whole numbers'
            }
            response = JsonResponse(response_data)
            response.status_code = 400

    return response

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
            response_data = {
                'result': 'Enter whole numbers'
            }
            response = JsonResponse(response_data)
            response.status_code = 400

    return response
    

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
            response_data = {
                'result': 'Enter whole numbers'
            }
            response = JsonResponse(response_data)
            response.status_code = 400

    return response

def divide(request):
    num = request.body
    if num:
        nums = json.loads(num)
        try:
            nums['A'] = int(nums['A'])
            nums['B'] = int(nums['B'])
            if nums['B'] == 0:
                response_data = {
                    'result': 'Divided by zero!'
                }
                response = JsonResponse(response_data)
                response.status_code = 400
            else:
                total = nums['A'] // nums['B']
                response_data = {
                    'result': str(total)
                }
                response = JsonResponse(response_data)
        except:
            response_data = {
                'result': 'Enter whole numbers'
            }
            response = JsonResponse(response_data)
            response.status_code = 400

    return response


