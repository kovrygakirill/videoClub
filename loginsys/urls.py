from django.conf.urls import url
from .views import login, logout, register
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^login/$', csrf_exempt(login), name="login"),
    url(r'^logout/$', csrf_exempt(logout), name="logout"),
    url(r'^register/$', csrf_exempt(register), name="register"),
]
