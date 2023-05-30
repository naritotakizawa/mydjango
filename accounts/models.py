from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.ImageField('プロフィール画像', blank=True, null=True)
    profile = models.TextField('プロフィール', blank=True, null=True)
    follow = models.ManyToManyField('CustomUser', blank=True)

    def __str__(self):
        return self.username