from django.shortcuts import render
from .models import Article, ArticleForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'article/index.html', context)

def create(request):
    return render(request, 'article/create.html')