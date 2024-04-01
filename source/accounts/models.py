import os

from django.contrib.auth import get_user_model
from django.db import models


def directory_path(instance, filename):
    username = instance.author.username.lower()
    return os.path.join(f'accounts/avatars/{username}', f'{username}_image_{filename}')


class AccountProfile(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )

    avatar = models.ImageField(
        upload_to=directory_path,
        default="accounts/avatars/default/default_avatar_photo_profile.jpg",
        null=False,
        blank=True
    )
