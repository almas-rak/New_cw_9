from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, DetailView

from accounts.forms import LoginForm, CustomUserCreationForm
from accounts.models import AccountProfile
from gallery.models import GalleryPhoto, FavoriteModel


class Login(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, "Некорректные данные")
            return redirect('main_page')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.warning(request, "Пользователь не найден")
            return redirect('main_page')
        login(request, user)
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('main_page')


def logout_view(request):
    logout(request)
    return redirect('main_page')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


def profile_view(request, pk):
    user = get_user_model().objects.get(pk=pk)
    profile = AccountProfile.objects.get(user=user)
    publications = GalleryPhoto.objects.filter(author=pk, is_deleted=False)
    favorite = FavoriteModel.objects.filter(us_pk=pk)
    template_name = "user_detail.html"
    context = {
        "user_obj": user,
        "profile": profile,
        "publications": publications,
        "favorite": favorite
    }
    return render(request, template_name=template_name, context=context)

