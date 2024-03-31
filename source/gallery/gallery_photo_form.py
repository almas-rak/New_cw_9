from django import forms

from gallery.models import GalleryPhoto


class GalleryPhotoForm(forms.ModelForm):
    class Meta:
        model = GalleryPhoto
        fields = ("photo", "caption", "author")
