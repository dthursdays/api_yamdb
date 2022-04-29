
from django.contrib.auth.models import AbstractUser
from django.db import models

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
        return self.role == 'ADMIN' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'MODERATOR'


class Title(models.Model):
    pass


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


class Review(models.Model):
    pass


class Comment(models.Model):
    pass
