from django.urls import path
from . import views

urlpatterns = [
    ### HOME NAV
    path('', views.home,name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('courses/create/', views.course_create, name='course_create'),
    # path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    # path('courses/<int:pk>/edit/', views.course_edit, name='course_edit'),
    # path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
    





    ### API
    # path('api/v1/users/', views.api_users)
    path('api/v1/courses/', views.api_courses),







    ### CREATE 
    # path('users/create/', views.user_create, name='user_create'),


]
