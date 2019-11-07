from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Course
# from ..arc_profile.models import Profile

# import forms here

# Create your views here.

# def home(request):
#   return HttpResponse("Goodbye rocketship. Hello Home.")

def home(request):
    return render(request, 'index.html')

def about_us(request):
  return render(request, 'about_us.html')


def user_profile(request, pk, user_pk):
    user = User.objects.get(pk=user_pk)
    context = {"user": user}
    return render(request, "profile.html", context, pk)


def api_courses(request):
  all_courses = Course.objects.all()
  data = []
  for course in all_courses:
    data.append({"title": course.title, "description": course.description, "start_date": course.start_date, "end_date": course.end_date})
  return JsonResponse({"data": data, "status": 200})
