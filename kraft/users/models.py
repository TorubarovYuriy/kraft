from django.contrib.auth.models import AbstractUser
from django.db import models


class KraftUser(AbstractUser):
    bio = models.TextField('Биография', blank=True)
    
    class Meta:
        verbose_name = 'Полбзователь'
        verbose_name_plural = 'Пользователи'
