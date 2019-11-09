from django.urls import path
from . import views

urlpatterns = [

  ### USER
  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('profile/', views.profile, name='profile'),
  # path('profile/edit', views.profile_edit, name='profile_edit'),

  ### PURCHASES
  path('profile/purchase_list', views.purchase_list, name='purchase_list'),
  


]

