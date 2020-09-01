from django.shortcuts import render, redirect
from django.contrib import auth
from .queries.token import active_user
from .queries.authenticate import authorization_user
from .queries.registration import registration_user


def login(request):
    if request.POST:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        response = authorization_user(request, username, password)
    else:
        response = render(request, "login.html")

    return response


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    if request.POST:
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        response = registration_user(request, username, email, password1, password2)

        return response
    else:
        return render(request, "register.html")


def confirm_token(request):
    if request.GET:
        token = request.GET.get("token", "")
        response = active_user(request, token)
    else:
        response = render(request, "register.html")

    return response
