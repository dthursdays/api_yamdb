from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


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
