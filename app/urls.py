from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.fachero),
    path("bd/<name>/<code>", views.template),
    path("show/", views.variables),
]