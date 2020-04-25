from django.shortcuts import render, redirect

def index(request):
    return render(request, 'articles/index.html')