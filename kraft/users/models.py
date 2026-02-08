from django.contrib.auth.models import AbstractUser
from django.db import models


class KraftUser(AbstractUser):
    bio = models.TextField('Биография', blank=True)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.username
