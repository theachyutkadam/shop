from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
  path('', views.welcome, name='welcome'),
  path("products/index", views.index),

  path("products/form", views.new),
  path("products/create", views.create),
  path("products/update", views.update),

  path('products/edit/<int:id>', views.edit),
  path('products/show/<int:id>', views.show),
  path('products/delete/<int:id>', views.delete),
]
