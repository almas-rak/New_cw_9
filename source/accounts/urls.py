from django.urls import path

from accounts import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', views.profile_view, name='profile'),
]
