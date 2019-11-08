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


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    context = {"course": course}
    return render(request, "course_detail.html", context)


def api_courses(request):
    all_courses = Course.objects.all()
    data = []
    for course in all_courses:
        data.append({"title": course.title, "description": course.description,
                     "start_date": course.start_date, "end_date": course.end_date})
    return JsonResponse({"data": data, "status": 200})


def course_create(request):

  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      course = form.save(commit=False)
      course.user = request.user
      course.save()
      return redirect('profile')
  else:
    form = CourseForm()
  context = {'form': form, 'header': "Add New Course"}
  return render (request, 'course_form.html', context)

def purchase_create(request, pk):
  course = Course.objects.get(id=pk)
  purchase = Purchase(student=request.user, course=course)
  purchase.save()
  return redirect ('profile')
    # course = Course.objects.get(id=pk)
    # if request.method == 'POST':
    #     form = PurchaseForm(request.POST)
    #     if form.is_valid():
    #         purchase = form.save(commit=False)
    #         purchase.student=request.user
    #         purchase.course=course
    #         purchase.save()
    #         return redirect ('profile')
    # else:
    #     return redirect ('home')
































































def course_edit(request, pk):
  course = Course.objects.get(id=pk)
  if request.method == 'POST':
    form = CourseForm(request.POST, instance=course)
    if form.is_valid():
      course = form.save()
      return redirect('course_detail', pk=course.pk)
  else:
    form = CourseForm(instance=course)
    context = {'form': form}
    return render(request, 'course_form.html', context)

def course_delete(request, pk):
  Course.objects.get(id=pk).delete()
  return redirect('profile')

