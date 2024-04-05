from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from gallery.gallery_photo_form import GalleryPhotoForm
from gallery.models.photo_model import GalleryPhoto


class PhotoListView(ListView):
    model = GalleryPhoto
    context_object_name = "photos"
    template_name = "index.html"

    def get_queryset(self):
        queryset = GalleryPhoto.objects.filter(is_deleted=False).order_by('-created_at')
        return queryset


class CreatePhotoView(CreateView):
    form_class = GalleryPhotoForm
    template_name = "add_photo.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail_photo", kwargs={"pk": self.object.pk})


class DetailPhotoView(DetailView):
    model = GalleryPhoto
    template_name = "detail_photo.html"
    context_object_name = "photo"


class UpdatePhotoView(UpdateView):
    model = GalleryPhoto
    template_name = "update_photo.html"
    form_class = GalleryPhotoForm
    context_object_name = "photo"

    def get_success_url(self):
        return reverse("detail_photo", kwargs={"pk": self.object.pk})


class DeletePhotoview(DeleteView):
    model = GalleryPhoto
    template_name = "detail_photo.html"
    extra_context = {"delete": "delete"}
    context_object_name = "photo"
