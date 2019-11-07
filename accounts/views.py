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
                    user = User.objects.create_profile()


def logout(request):
    auth.logout(request)
    return redirect('home')











































































































































































# pouyesh jeff code 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authentication
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            #login
            auth.login(request,user)
            #redirect
            return redirect('home')
        else:
            context = {'error':'Invalid Credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

# def profile(request):
#     profile = Profile.objects.filter(user=request.user)
#     context = {'profiles':profiles}
#     return render(request, "profile.html", context)

# pouyesh jeff code 
