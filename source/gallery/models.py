import os

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


def directory_path(instance, filename):
    username = instance.author.username.lower()
    return os.path.join(f'gallery/photo_galleries/{username}', f'{username}_image_{filename}')


class GalleryPhoto(models.Model):
    photo = models.ImageField(
        upload_to=directory_path,
        verbose_name='Фото'
    )
    caption = models.CharField(
        max_length=100,
        verbose_name="Подпись"
    )

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='gallery_photos',
        verbose_name='Автор'
    )

    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        blank=True,
        null=True,
        default=None
    )

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'deleted_at'])

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.caption}  Автор: {self.author}'
