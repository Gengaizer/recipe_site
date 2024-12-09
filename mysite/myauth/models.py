from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


def create_path_to_upload_images(instance: 'Profile', name: str) -> str:
    return f'users_files/user_{instance.user.pk}/photos/img_{name}'


class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    age = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(120)])
    avatar = models.ImageField(null=False, blank=True, upload_to=create_path_to_upload_images)
