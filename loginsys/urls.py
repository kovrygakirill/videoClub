from django.conf.urls import url
from django.urls import include

from .views import login, logout, register, confirm_token, forgot_password, refresh_password, \
    login_thought_social_network, register_thought_social_network
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^login/$', csrf_exempt(login), name="login"),
    url(r'^logout/$', csrf_exempt(logout), name="logout"),
    url(r'^social_network/$', csrf_exempt(login_thought_social_network), name="sn"),
    url(r'^confirm_token/$', csrf_exempt(confirm_token), name="confirm_token"),
    url(r'^register/social_network/$', csrf_exempt(register_thought_social_network), name="register_sn"),
    url(r'^register/$', csrf_exempt(register), name="register"),
    url(r'^forgot_password/refresh_password/$', csrf_exempt(refresh_password), name="refresh_password"),
    url(r'^forgot_password/$', csrf_exempt(forgot_password), name="forgot_password"),
    url(r'^social/', include('social_django.urls')),
]
