from django.contrib import admin
from django.urls import path
from customers import views

urlpatterns = [
  path('', views.welcome, name='welcome'),
  path("create", views.create),
  path("form", views.new),
  path("index", views.index),
  path('edit/<int:customer_id>', views.update),
  path('delete/<int:customer_id>', views.delete),
]
