from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    ### HOME NAV
    path('', views.home,name='home'),
    path('about_us/', views.about_us, name='about_us'),
    





    ### API
    path('api/v1/profiles/', views.api_profiles),
    path('api/v1/courses/', views.api_courses),







    ### CREATE 
    path('profiles/create/', views.profile_create, name='profile_create'),


]
