from django.db import models
from django.contrib.auth.models import User


class TokenEmail(models.Model):
    key = models.CharField(max_length=20)
    id_user = models.IntegerField()

    object = models.Manager()

    def __str__(self):
        return self.key


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_confirm = models.BooleanField(default=False)

    object = models.Manager()

    def __str__(self):
        return str(self.user)
