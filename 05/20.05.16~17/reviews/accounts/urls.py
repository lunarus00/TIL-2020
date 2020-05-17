from django.urls import path
from crud.views import index
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', index),
    path('create/', views.create, name='create'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]