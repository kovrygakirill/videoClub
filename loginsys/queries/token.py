from random import choice
from string import ascii_uppercase
from ..models import TokenEmail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from ..models import UserProfile


def get_token(id_user):
    key = ''.join(choice(ascii_uppercase) for i in range(16))
    token = TokenEmail.object.create(key=key, id_user=id_user)
    token.save()

    return key


def check_token_exist_for_refresh_password(request, key):
    args = {}
    try:
        token = TokenEmail.object.get(key=key)
        args["token"] = token
        response = render(request, "refresh_password.html", args)
    except TokenEmail.DoesNotExist:
        response = render(request, "404.html")

    return response


def active_user(request, key):
    try:
        token = TokenEmail.object.get(key=key)
        user = User.objects.get(id=token.id_user)
        user_profile = UserProfile.object.get(user_id=user.id)
        token.delete()
        user_profile.is_confirm = True
        user_profile.save()

        response = redirect("/auth/login/")
    except TokenEmail.DoesNotExist:
        response = render(request, "404.html")
    except User.DoesNotExist:
        response = render(request, "404.html")

    return response
