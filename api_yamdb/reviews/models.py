from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

MODERATOR = 'moderator'
ADMIN = 'admin'
AUTH_USER = 'user'

ROLE_CHOICES = [
    ('MODERATOR', 'Модератор'),
    ('ADMIN', 'Администратор'),
    ('AUTH_USER', 'Авторизованный пользователь'),
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
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(verbose_name='Биография', blank=True,)
    role = models.CharField(
        verbose_name='Роль',
        max_length=10,
        default='AUTH_USER',
        choices=ROLE_CHOICES
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_user'
            )
        ]

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR


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

    def __str__(self):
        return self.name


class Review(models.Model):
    pass


class Comment(models.Model):
    pass
