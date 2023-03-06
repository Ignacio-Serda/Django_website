from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.inicio),
    path("bd/<name>/<code>", views.template),
    path("show/", views.variables),
]