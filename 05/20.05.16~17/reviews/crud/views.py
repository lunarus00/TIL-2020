from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'crud/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('crud:detail', article.pk)
    else:
        form = ArticleForm
    context = {
        'form': form
    }
    return render(request, 'crud/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'crud/detail.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('crud:index')

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('crud:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'crud/form.html', context)

def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return redirect('crud:detail', article.pk)
    else:
        return redirect('crud:detail', article.pk)

def comment_delete(request, article_pk, comment_pk):
    
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('crud:detail', article_pk)
