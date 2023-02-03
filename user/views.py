from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

# Register user view
def register(request):
    if request.method == "POST":
        fname = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass_one']
        pass2 = request.POST['pass_two']

        myUser = User.objects.create_user(fname, email, pass1)
        username = myUser.username

        myUser.save()
        
        messages.success(request, f'Hi {username}, your account was created successfully.')
        return redirect('index')

    return render (request, "user/register.html")

# Create user admin view
def user_admin(request):
    return render (request, "user/admin.html")

# Create guest user view
def user_guest(request):
    return render(request, "user/user.html")
