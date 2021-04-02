from django.contrib.auth.models import User
from ..models import UserProfile
from django.shortcuts import render, redirect
from django.contrib import auth
from .email import send_email_for_register


def registration_social_network(request, email, username):
    args = {}
    error_register = check_exist_email(email)

    if not error_register:
        user_profile = create_not_active_user_profile(username, email)
        send_email_for_register(email, user_profile.user.id)
        response = render(request, 'success_register.html', args)
    else:
        args["register_error"] = error_register
        response = render(request, "register_social_network.html", args)

    return response


def registration_user(request, username, email, password1, password2):
    args = {}
    user = auth.authenticate(username=username, password=password1)

    if user is not None:
        args["register_error"] = "User already exist with this username"
    else:
        error_register = check_fields(username, email, password1, password2)
        if not error_register:
            user_profile = create_not_active_user(username, email, password1)

            send_email_for_register(email, user_profile.user.id)

            responce = render(request, 'success_register.html')
            responce.delete_cookie("email")
            responce.delete_cookie("username")

            return responce
        else:
            args["register_error"] = error_register

    args["username"] = username
    args["email"] = email
    response = render(request, "register.html", args)
    response.set_cookie('email', email)
    response.set_cookie('username', username)
    return response


def create_not_active_user(username, email, password):
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )
    user.save()

    user_profile = UserProfile.object.create(user=user)
    user_profile.save()

    return user_profile


def create_not_active_user_profile(username, email):
    user = User.objects.get(username=username)
    user.email = email
    user.save()

    user_profile = UserProfile.object.create(user=user)
    user_profile.save()

    return user_profile


def check_fields(username, email, password1, password2):
    checks_func = [check_fill_in_fields,
                   check_exist_username,
                   check_exist_email,
                   check_repeat_password
                   ]
    checks_param = [[username, email, password1, password2],
                    [username],
                    [email],
                    [password1, password2]]
    result = ""

    for fun, param in zip(checks_func, checks_param):
        result = fun(*param)

        if result:
            break

    return result


def check_fill_in_fields(*fields):
    result = ""

    for i in fields:
        if not i:
            result = "Please, fill in all the fields"
            break

    return result


def check_exist_username(username):
    result = ""

    try:
        User.objects.get(username=username)
        result = 'This username already exist'
    except User.DoesNotExist:
        pass

    return result


def check_exist_email(email):
    result = ""

    try:
        User.objects.get(email=email)
        result = 'This email already exist'
    except User.DoesNotExist:
        pass

    return result


def check_repeat_password(password1, password2):
    result = ""

    if password1 != password2:
        result = "New password not equal repeat password"

    return result
