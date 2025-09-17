from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    path('user', views.user, name='user'),
    path('logout', views.logout, name='logout'),
    path('login', views.Login.as_view(), name='login'),
]