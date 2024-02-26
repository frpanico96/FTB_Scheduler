from django.core.exceptions import ViewDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

import json


# Create your views here.


def ping(request):
    return HttpResponse("Ping succesfully")


def register(request):
    if request.method == 'POST':
        userdata = json.loads(request.body)
        print(userdata)
        print(userdata['username'] + ' ' + userdata['password'])
        user = User.objects.create_user(username=userdata['username'], password=userdata['password'])
        tokenr = TokenObtainPairSerializer().get_token(user)
        tokena = AccessToken().for_user(user)
        responseObj = {"refresh": str(tokenr),
                       "access": str(tokena),
                       }
        return HttpResponse(json.dumps(responseObj))
    else:
        raise ViewDoesNotExist
