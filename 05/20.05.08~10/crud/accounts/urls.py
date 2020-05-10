from django.urls import path
from . import views
from articles.views import index

app_name = 'accounts'

urlpatterns = [
    path('', index),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]