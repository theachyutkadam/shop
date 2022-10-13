from django.contrib import admin
from django.urls import path
from customers import views

urlpatterns = [
  path('', views.welcome, name='welcome'),
  path("index", views.index),

  path("form", views.new),
  path("create", views.create),
  path("update", views.update),

  path('edit/<int:id>', views.edit),
  path('show/<int:id>', views.show),
  path('delete/<int:id>', views.delete),

]
