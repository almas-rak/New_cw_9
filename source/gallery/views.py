from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView

from gallery.gallery_photo_form import GalleryPhotoForm
from gallery.models import GalleryPhoto


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['photo'] = get_object_or_404(GalleryPhoto, pk=kwargs['pk'])
    #     context['form'] = GalleryPhotoForm(instance=context['photo'])
    #     return context

    def get_success_url(self):
        return reverse("detail_photo", kwargs={"pk": self.object.pk})
