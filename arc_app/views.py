from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers 
from django.contrib.auth.decorators import login_required

from .models import Course
# from ..arc_profile.models import Profile

# import forms here

# Create your views here.

def home(request):
  return HttpResponse("Goodbye rocketship. Hello Home.")