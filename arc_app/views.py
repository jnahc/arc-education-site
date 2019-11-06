from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers 
from django.contrib.auth.decorators import login_required

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

def api_profiles(request):
  all_profiles = Profile.objects.all()
  data = []
  for profile in all_profiles:
    data.append({"name": profile.full_name, "photo": profile.photo_url, "skills": profile.skills, "bio": profile.bio})
  return JsonResponse({"data": data, "status": 200})

def profile_create(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user
      profile.save()
      return redirect('profile_detail', pk=profile.pk)
  else:
    form = ProfileForm()
  context = {'from': form, 'header': "Create Profile"}
  return render(request, 'profile_form.html', context)

