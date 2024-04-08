from django.urls import path
from gallery import views

urlpatterns = [
    path("", views.PhotoListView.as_view(), name="main_page"),
    path("add/photo/", views.CreatePhotoView.as_view(), name="add_photo"),
    path("detail/photo/<int:pk>/", views.DetailPhotoView.as_view(), name="detail_photo"),
    path("update/photo/<int:pk>/", views.UpdatePhotoView.as_view(), name="update_photo"),
    path("delete/photo/<int:pk>/", views.DeletePhotoview.as_view(), name="delete_photo"),
]
