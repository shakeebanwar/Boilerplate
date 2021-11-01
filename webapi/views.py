from django.shortcuts import render
from django.conf import settings
from passlib.hash import django_pbkdf2_sha256 as handler
import re
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class registration(APIView):
    def get(self,request):
        return Response("okay")

