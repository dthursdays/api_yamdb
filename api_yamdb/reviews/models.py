from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

ROLE_CHOICES = [
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
    ('user', 'Авторизованный пользователь'),
]


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )
    confirmation_code = models.CharField(verbose_name='Код подтверждения',
                                         max_length=100)
    first_name = models.CharField(verbose_name='Имя', max_length=150,
                                  blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150,
                                 blank=True)
    bio = models.TextField(verbose_name='Биография', blank=True)
    role = models.CharField(
        verbose_name='Роль',
        max_length=10,
        default='user',
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return self.name

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'moderator'


class Category(models.Model):
    name = models.CharField(max_length=256, unique=True,)
    slug = models.SlugField(max_length=50, unique=True,)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256, unique=True,)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=300,)
    year = models.IntegerField(
        validators=[
            MinValueValidator(100),
            MaxValueValidator(datetime.now().year)
        ]
    )
    description = models.TextField(max_length=256)
    genre = models.ManyToManyField(Genre)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
    )
