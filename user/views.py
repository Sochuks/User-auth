from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
def index(request):
    return render(request, "index.html")

# Register user view
def register(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass_one']
        pass2 = request.POST['pass_two']

        myUser = User.objects.create_user(username, email, pass1)
        myUser.first_name = fname
        myUser.last_name = lname

        myUser.save()
        messages.success(request, f'Hi {username}, your account was created successfully.')
        return redirect('index')

    return render (request, "user/register.html")

# Signin function
def sign_in(request):
    if request.user.is_authenticated:
        return render (request, "user/user.html")
    else:
        messages.info(request, 'Kindly login to view this page')
        return HttpResponseRedirect('signin')

# Create User Sign In  view
def sign_in_user(request):
    if request == "POST":
        uname = request.POST['username']
        pass1 = request.POST['pass_one']

        user = authenticate(username=uname, passowrd=pass1)

        if user is not None:
            login(request, user)
            f_name = user.first_name
            return render (request, "user/user.html", {
                "fname":f_name
            })
        else:
            messages.error(request, "Invalid Account Credentials")
            return HttpResponseRedirect('signin')

    return render (request, "user/login.html")

# Create user admin view
def user_admin(request):
    return render (request, "user/admin.html")

# Create guest user view
def user_guest(request):
    return render(request, "user/user.html")
