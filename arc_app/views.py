from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers 

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Course
from .forms import CourseForm



# Create your views here.


def home(request):
  return render(request, 'index.html')

def about_us(request):
  return render(request, 'about_us.html')


def course_create(request):
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      course = form.save(commit=False)
      course.user = request.user
      course.save()
      return redirect('course_detail', pk=course.pk)
  else:
    form = CourseForm()
  context = {'from': form, 'header': "Create Course"}
  return render(request, 'course_form.html', context)






































































































































def api_courses(request):
  all_courses = Course.objects.all()
  data = []
  for course in all_courses:
    data.append({"title": course.title, "description": course.description, "start_date": course.start_date, "end_date": course.end_date})
  return JsonResponse({"data": data, "status": 200})
















































































































































































def course_create(request):
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      course = form.save()
      # course.profile = request.profile
      # course.save()
      return redirect('profile')
  else:
    form = CourseForm()
  context = {'form': form, 'header': "Add New Course"}
  return render (request, 'course_form.html', context)


