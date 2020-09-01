from django.core.mail import send_mail
from .token import get_token


def send_email(toEmail, id_user):
    header = "VideoClub registration"
    token = get_token(id_user)
    message = f"To complete registration, follow the link: http://127.0.0.1:8000/auth/confirm_token/?token={token}"
    fromEmail = 'videoclubapp@gmail.com'

    send_mail(header, message, fromEmail, [toEmail], fail_silently=False, )
