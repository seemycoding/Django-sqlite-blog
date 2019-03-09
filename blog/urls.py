from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Home', views.Home, name='Home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('add', views.add, name='add'),
    path('viewpost', views.viewpost, name='viewpost'),
    path('logout', views.logout, name='logout'),
    path('details/<int:idd>', views.details, name='details'),


]
