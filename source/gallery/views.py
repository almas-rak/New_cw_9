from django.views.generic import ListView

from gallery.models import GalleryPhoto


class PhotoListView(ListView):
    model = GalleryPhoto
    context_object_name = "photos"
    template_name = "index.html"

    def get_queryset(self):
        queryset = GalleryPhoto.objects.filter(is_deleted=False).order_by('-created_at')
        return queryset


