from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
import logging

def json_parse(request_body):
    return json.loads(request_body.decode("utf-8"))

def signup(request):
    data = json_parse(request.body)
    User.objects.create_user(
        username=data.get('username'), 
        password=data.get('password')
    )
    return HttpResponse(status=201)

def login(request):
    data = json_parse(request.body)
    user = authenticate(
        username=data.get('username'), 
        password=data.get('password')
    )
    if user is not None:
        auth.login(request, user)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)

def logout(request):
    auth.logout(request.user)
    return HttpResponse(status=200)
