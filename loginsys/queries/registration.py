from django.contrib.auth.models import User


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
