from django.shortcuts import render, redirect
from django.contrib import auth
from .queries.token import active_user, check_token_exist_for_refresh_password
from .queries.authenticate import authorization_user
from .queries.registration import registration_user, registration_social_network
from .queries.forgot_password import confirm_email, create_new_password
from business_logic.my_base_exception import base_view
from .queries.authenticate import get_user_profile_by_name, authorization_social_network


@base_view
def login_thought_social_network(request):
    user = request.user
    user_profile = get_user_profile_by_name(user)

    if user_profile:
        response = authorization_social_network(request, user_profile)
    else:
        response = render(request, "register_social_network.html", {'user': user})

    return response


@base_view
def register_thought_social_network(request):
    if request.POST:
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")

        response = registration_social_network(request, email, username)

        return response
    else:
        return render(request, "register_social_network.html")


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
