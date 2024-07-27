from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
import requests
import json

@csrf_exempt
def consumeApiGet(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    return render(request, "api-get.html", {'data': data})

@csrf_exempt
def consumeApiPost(request):
    if request.method == 'POST':
        payload = {
            'name': request.POST.get('name'),
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
        }
        response = requests.post("https://jsonplaceholder.typicode.com/users", data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        return JsonResponse(response.json(), status=response.status_code)

@csrf_exempt
def consumeApiPut(request, id):
    if request.method == 'POST':
        payload = {
            'name': request.POST.get('name'),
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
        }
        response = requests.put(f"https://jsonplaceholder.typicode.com/users/{id}", data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        return JsonResponse(response.json(), status=response.status_code)
