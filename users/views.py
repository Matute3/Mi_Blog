from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


@login_required
def user_list(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def test_view(request):
    User = get_user_model()
    users = User.objects.all()
    return HttpResponse(f"Usuarios registrados: {users.count()}")
