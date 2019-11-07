from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from arc_app.models import Course

# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # skills = request.POST['skills']
        # bio = request.POST['bio']
        # creditcard_info = request.POST['creditcard_info']
        # address_form = request.POST['address']
        email_form = request.POST['email']
        username_form = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        # is_staff = request.POST['is_staff']
        # date_joined = request.POST['date_joined']
        # is_superuser = request.POST['is_superuser']
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
                    #####need route


                    return redirect('course_list')

        else:
            context = {'error':'Passwords do not match'}
            return render(request, 'register.html', context)
    else:
        return render(request, 'register.html')














































































































































































def login(request):
    if request.method == 'POST':
        username_form = request.POST['username']
        password_form = request.POST['password']
        #authentication
        user = auth.authenticate(username=username_form, password=password_form)

        if user is not None:
            #login
            auth.login(request,user)
            #redirect
            return redirect('profile')
        else:
            context = {'error':'Invalid Credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('user_list')


def profile(request):
    courses = Course.objects.filter(user=request.user)
    context = {'courses':courses}
    return render(request, 'profile.html',context)



