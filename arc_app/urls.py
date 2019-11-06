from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home),
    path('profiles/new/', views.profile_create, name='profile_create'),
    path('api/v1/profiles/', views.api_profiles)

]