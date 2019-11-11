from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import Course, Purchase
from .forms import CourseForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')


def course_list(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, 'course_list.html', context)

def course_detail(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    course_pk = course.pk
    purchases = Purchase.objects.filter(course = course_pk)
    context = {"course": course, "purchases": purchases}
    return render(request, "course_detail.html", context)

def api_courses(request):
    all_courses = Course.objects.all()
    data = []
    for course in all_courses:
      data.append({"title": course.title, "description": course.description,
      "start_date": course.start_date, "end_date": course.end_date})
    return JsonResponse({"data": data, "status": 200})

@login_required
def purchase_create(request, course_slug):
  course = Course.objects.get(slug=course_slug)
  purchase = Purchase(student=request.user, course=course)
  purchase.save()
  return redirect ('profile')

@login_required
def course_create(request):
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      course = form.save(commit=False)
      course.user = request.user
      course.save()
      return redirect('course_detail', course_slug=course.slug)
  else:
    form = CourseForm()
  context = {'form': form, 'header': "Add New Course"}
  return render (request, 'course_form.html', context)

@login_required
def course_edit(request, pk):
  course = Course.objects.get(id=pk)
  if request.method == 'POST':
    form = CourseForm(request.POST, instance=course)
    if form.is_valid():
      course = form.save()
      return redirect('course_detail', course_slug=course.slug)
  else:
    form = CourseForm(instance=course)
    context = {'form': form, "creator": course.user}
    return render(request, 'course_form_edit.html', context)

@login_required
def course_delete(request, course_slug):
  Course.objects.get(slug=course_slug).delete()
  return redirect('profile')

@login_required
def purchase_delete(request, course_slug, purchase_pk):
  Purchase.objects.get(id=purchase_pk).delete()
  return redirect ('profile')

def purchase_list(request, course_slug):
  purchases = Purchase.objects.all()
  context = {"purchases": purchases}
  return render(request, 'purchase_list.html', context)



  





