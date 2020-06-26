from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .queries.registration import check_fields


def login(request):
    args = {}
    if request.POST:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            args["login_error"] = "User wasn't found"
            return render(request, "login.html", args)
    else:
        return render(request, "login.html", args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    # args["register_error"] = "Please, fill in all the fields"
    if request.POST:
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            args["register_error"] = "User already exist with this username"
        else:
            error_register = check_fields({"username": username, "email": email,
                                           "password1": password1, "password2": password2})
            if not error_register:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email
                )
                user.save()
                auth.login(request, user)
                return redirect("/")
            else:
                args["register_error"] = error_register

    return render(request, "register.html", args)
