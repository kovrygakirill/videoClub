from django.shortcuts import render, redirect
from django.contrib import auth


def authorization_user(request, username, password):
    user = auth.authenticate(username=username, password=password)

    args = check_user(user)
    if not args:
        auth.login(request, user)
        response = redirect("/")
    else:
        response = render(request, "login.html", args)

    return response


def check_user(user):
    args = {}

    if user is None:
        args["login_error"] = "User wasn't found"
    elif not user.userprofile.is_confirm:
        args["login_error"] = "Confirm registration(email)"

    return args
