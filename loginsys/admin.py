from django.contrib import admin
from .models import TokenEmail, UserProfile

admin.site.register(TokenEmail)
admin.site.register(UserProfile)
