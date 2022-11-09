from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.contrib.auth.models import AbstractUser

from hollywood.settings import AUTH_USER_MODEL


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Staff(AbstractUser):
    role = models.ManyToManyField(Role, related_name="staff")

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Genre(models.Model):
    genre = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["genre"]

    def __str__(self):
        return f"{self.genre}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    genres = models.ManyToManyField(Genre)
    staff = models.ManyToManyField(AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.title} "
