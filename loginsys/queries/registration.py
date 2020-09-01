from django.contrib.auth.models import User
from ..models import UserProfile
from django.shortcuts import render, redirect
from django.contrib import auth
from .email import send_email


def registration_user(request, username, email, password1, password2):
    args = {}
    user = auth.authenticate(username=username, password=password1)

    if user is not None:
        args["register_error"] = "User already exist with this username"
    else:
        error_register = check_fields({"username": username, "email": email,
                                       "password1": password1, "password2": password2})
        if not error_register:
            user_profile = create_not_active_user({"username": username, "email": email,
                                                   "password": password1})

            send_email(email, user_profile.user.id)

            return render(request, 'success_register.html')
        else:
            args["register_error"] = error_register

    return render(request, "register.html", args)


def create_not_active_user(kwargs):
    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        email=kwargs['email']
    )
    user.save()

    user_profile = UserProfile.object.create(user=user)
    user_profile.save()

    return user_profile


def check_fields(kwargs):
    checks = [check_fill_in_fields, check_exist_username,
              check_exist_email, check_repeat_password]
    result = ""

    for check in checks:
        result = check(kwargs)

        if result:
            break

    return result


def check_fill_in_fields(kwargs):
    result = ""

    for i in kwargs.values():
        if not i:
            result = "Please, fill in all the fields"
            break

    return result


def check_exist_username(kwargs):
    result = ""

    try:
        User.objects.get(username=kwargs['username'])
        result = 'This username already exist'
    except User.DoesNotExist:
        pass

    return result


def check_exist_email(kwargs):
    result = ""

    try:
        User.objects.get(email=kwargs['email'])
        result = 'This email already exist'
    except User.DoesNotExist:
        pass

    return result


def check_repeat_password(kwargs):
    result = ""

    if kwargs['password1'] != kwargs['password2']:
        result = "New password not equal repeat password"

    return result
