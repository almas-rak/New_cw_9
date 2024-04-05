from django import forms

from gallery.models.photo_model import GalleryPhoto


class GalleryPhotoForm(forms.ModelForm):
    class Meta:
        model = GalleryPhoto
        fields = ("photo", "caption",)
