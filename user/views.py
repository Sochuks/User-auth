from django.shortcuts import render

from . models import createUser
from . forms import regForm

# Create your views here.
def index(request):
    return render(request, "index.html")

# Register user view
def register(request):
    return render (request, "user/register.html")

# Create user admin view
def user_admin(request):
    return render (request, "user/admin.html")

# Create guest user view
def user_guest(request):
    return render(request, "user/user.html")
