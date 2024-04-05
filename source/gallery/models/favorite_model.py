from django.contrib.auth import get_user_model
from django.db import models

from gallery.models.photo_model import GalleryPhoto


class FavoriteModel(models.Model):
    us_pk = models.ForeignKey(
        to=get_user_model(),
        related_name="fav_to_user",
        on_delete=models.CASCADE
    )

    ph_pk = models.ForeignKey(
        to=GalleryPhoto,
        related_name="fav_photo",
        on_delete=models.CASCADE
    )
