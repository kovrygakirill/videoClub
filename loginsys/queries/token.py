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


def active_user(request, key):
    try:
        token = TokenEmail.object.get(key=key)
        user = User.objects.get(id=token.id_user)
        user_profile = UserProfile.object.get(user_id=user.id)
        token.delete()
        user_profile.is_confirm = True
        user_profile.save()

        response = render(request, "login.html")
    except TokenEmail.DoesNotExist:
        pass
    except User.DoesNotExist:
        pass

    return response
