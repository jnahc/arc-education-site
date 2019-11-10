from django.urls import path
from . import views



urlpatterns = [
    ### PUBLIC VIEWS
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),

    ### COURSE VIEWS
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('courses/<slug:course_slug>/delete/', views.course_delete, name='course_delete'),

    ### PURCHASE VIEWS
    path('courses/<slug:course_slug>/purchase/create', views.purchase_create, name="purchase_create"),
    path('course/<slug:course_slug>/purchase/<int:purchase_pk>/delete', views.purchase_delete, name="purchase_delete"),
    
    ### API
    # path('api/v1/users/', views.api_users)
    path('api/v1/courses/', views.api_courses),


    ### Search Test
    path('courses/search/',views.course_list, name='course_list_search'),

]
