from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class ArticleForm(ModelForm):
    class meta:
        model = Article
        fields = '__all__'
