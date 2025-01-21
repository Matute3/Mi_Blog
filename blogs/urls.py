from django.contrib import admin
from django.urls import path, include
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('', views.home, name='home'),
]
