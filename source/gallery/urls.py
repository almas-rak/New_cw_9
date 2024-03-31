from django.urls import path
from gallery import views

urlpatterns = [
    path("", views.PhotoListView.as_view(), name="main_page")
]