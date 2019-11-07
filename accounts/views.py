from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from arc_profile.models import Profile

# Create your views here.

def register(request):
    if requested.method == "POST":
        full_name = request.POST['full_name']
        photo_url = request.POST['photo_url']
        skills = request.POST['skills']
        bio = request.POST['bio']
        creditcard_info = request.POST['creditcard_info']
        address_form = request.POST['address']
        email_form = request.POST['email']
        username_form = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        is_staff = request.POST['is_staff']
        date_joined = request.POST['date_joined']
        is_superuser = request.POST['is_superuser']
        if password == password2:
            if User.objects.filter(username=username_form).exists():
                context = {'error': 'Username is already in use!'}
                return render(request, 'register.html', context)
            else:
                if User.objects.filter(email=email_form).exists():
                    context = {'error': 'That email already exists.'}
                    return render(request, 'register.html', context)
                else:
                    user = User.objects.create_user(
                        username=username_form, 
                        email=email_form, 
                        password=password, 
                        first_name=first_name, 
                        last_name=last_name)
                    user.save()
                    profile = Profile.objects.create_profile(
                        full_name=full_name,
                        photo_url=photo_url,
                        skills=skills,
                        bio=bio,
                        creditcard_info=creditcard_info,
                        address_form=address_form,
                        password2=password2,
                        is_staff=is_staff,
                        date_joined=date_joined,
                        is_superuser=is_superuser
                    )
                    profile.save()
                    #####need route
                    return redirect('')
        else:
            context = {'error':'Passwords do not match'}
            return render(request, 'register.html', context)
    else:
        return render(request, 'register.html')