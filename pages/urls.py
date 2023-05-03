from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('sign-up/', views.signup),
    path('chat/', views.chat),
    path('news/', views.news),
    path('about/', views.about),
]