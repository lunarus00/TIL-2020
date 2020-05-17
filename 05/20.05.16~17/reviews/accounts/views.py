from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout


def create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:index')
    else:
        form = CustomUserCreationForm
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'crud:index')
    else:
        form = AuthenticationForm
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('crud:index')

def detail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'user': user,
    }
    return render(request, 'accounts/detail.html', context)

def follow(request, user_pk):
    User = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user in User.followers.all():
        User.followers.remove(request.user)
    else:
        User.followers.add(request.user)
    return redirect('accounts:detail', User.pk)