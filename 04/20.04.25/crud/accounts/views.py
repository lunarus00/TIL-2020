from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def index(request):
    return render(request, 'accounts/index.html')

def login(request):
    if request.mehtod == 'POST':
        form = AthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index.html')
    else:
        form = AthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accoutns:index')