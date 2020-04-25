from django.urls import render, redirect

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]