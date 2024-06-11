from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    """ Модель пользователя """
    phone = models.CharField(max_length=20, unique=True, verbose_name='телефон', **NULLABLE)
    city = models.TextField(max_length=50, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='аватар', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    telegram_chat_id = models.CharField(max_length=100, verbose_name='telegram chat ID', blank=True)

    # Смена авторизации с имени пользователя на электронную почту
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'telegram_chat_id']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'