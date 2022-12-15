from pyexpat.errors import messages

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from pools.models import UserV


def index(request):
    return render(request, 'index.file.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                user1 = User.objects.get(user=user)
                if user1.type == "applicant":
                    login(request, user)
                    return redirect("/")
            else:
                thank = True
                return render(request, "about.html", {"thank": thank})
    return render(request, "about.html")


def signup(request, user=None):
    if request.method == "POST":

        if request.user.is_authenticated:
            return redirect("layout.html")




        return render(request, "about.html")
    return render(request, "Login.html")
