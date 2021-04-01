from django.shortcuts import render, redirect
from django.contrib import auth
from .queries.token import active_user, check_token_exist_for_refresh_password
from .queries.authenticate import authorization_user
from .queries.registration import registration_user
from .queries.forgot_password import confirm_email, create_new_password
from business_logic.my_base_exception import base_view


@base_view
def kyky(request):
    return redirect("/social/login/vk-oauth2/")

@base_view
def login(request):
    if request.POST:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        response = authorization_user(request, username, password)
    else:
        response = render(request, "login.html")

    return response


@base_view
def logout(request):
    auth.logout(request)
    return redirect("/")


@base_view
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


@base_view
def confirm_token(request):
    if request.GET:
        token = request.GET.get("token", "")
        response = active_user(request, token)
    else:
        response = render(request, "register.html")

    return response


@base_view
def forgot_password(request):
    if request.POST:
        email = request.POST.get("email", "")
        response = confirm_email(request, email)
    else:
        response = render(request, "forgot_password.html")

    return response


@base_view
def refresh_password(request):
    if request.POST:
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        token = request.GET.get("token", "")
        response = create_new_password(request, password1, password2, token)
    else:
        token = request.GET.get("token", "")
        response = check_token_exist_for_refresh_password(request, token)

    return response
