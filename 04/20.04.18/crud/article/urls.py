from django.urls import path
from . import views

urlname = 'article'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
]