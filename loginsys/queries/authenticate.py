from django.shortcuts import render, redirect
from django.contrib import auth
from loginsys.models import UserProfile


def authorization_user(request, username, password):
    user = auth.authenticate(username=username, password=password)

    args = check_user(user)
    if not args:
        auth.login(request, user)
        response = redirect("/")
    else:
        response = render(request, "login.html", args)

    return response


def authorization_social_network(request, user):
    args = check_user_social_network(user)
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


def check_user_social_network(user):
    args = check_user(user)

    if user.auth:
        args["login_error"] = "User wasn't auth"

    return args


def get_user_profile_by_name(user_name):
    try:
        user = UserProfile.object.get(user__username=user_name)
    except UserProfile.DoesNotExist:
        user = None

    return user
