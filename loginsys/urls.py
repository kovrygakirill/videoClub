from django.conf.urls import url
from .views import login, logout
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^login/$', csrf_exempt(login), name="login"),
    url(r'^logout/$', csrf_exempt(logout), name="logout"),
]
