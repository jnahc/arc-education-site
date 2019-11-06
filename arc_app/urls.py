from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
  path('', views.home,name='home'),
  path('about_us', views.about_us, name='about_us')
  ]