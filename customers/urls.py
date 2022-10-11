from django.contrib import admin
from django.urls import path
from customers import views

urlpatterns = [
  path('', views.welcome, name='welcome'),
  path("form", views.new),
  path("create", views.create),
  path('edit/<int:id>', views.edit),
  path("update", views.update),
  path("index", views.index),
  path('delete/<int:id>', views.delete),
]
