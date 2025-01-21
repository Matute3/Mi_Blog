from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('list/', views.user_list, name='user_list'),
    
]

