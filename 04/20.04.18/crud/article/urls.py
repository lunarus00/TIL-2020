from django.urls import path
from . import views

urlname = 'article'

urlpatterns = [
    path('', views.index, name = 'index'),
]