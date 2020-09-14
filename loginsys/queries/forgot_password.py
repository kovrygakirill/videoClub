from django.shortcuts import render, redirect
from .registration import check_exist_email
from django.contrib.auth.models import User
from .email import send_email_for_refresh_password
from ..models import TokenEmail
from .registration import check_repeat_password


def confirm_email(request, email):
    args = {}
    try:
        user = User.objects.get(email=email)
        send_email_for_refresh_password(email, user.pk)
        return render(request, "success_confirm_email.html", args)

    except User.DoesNotExist:
        args["confirm_error"] = "This email not exist"
        return render(request, "forgot_password.html", args)


def create_new_password(request, password1, password2, key):
    args = {}
    try:
        token = TokenEmail.object.get(key=key)
        user = User.objects.get(id=token.id_user)
        check_passwords = check_repeat_password(password1, password2)

        if check_passwords:
            args["password_error"] = check_passwords
            args["token"] = token
            response = render(request, "refresh_password.html", args)
        else:
            user.set_password(password1)
            user.save()
            token.delete()
            response = render(request, "success_refresh_password.html")
    except TokenEmail.DoesNotExist:
        response = render(request, "404.html")
    except User.DoesNotExist:
        response = render(request, "404.html")

    return response
