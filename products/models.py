from django.db import models
from dataclasses import fields
from unittest.util import _MAX_LENGTH

# Create your models here.
class Product(models.Model):
  name         = models.CharField(max_length=25)
  price        = models.CharField(max_length=25)
  is_available = models.CharField(max_length=30)
  expire_date  = models.DateField()
  desc         = models.TextField()

  def __str__(self):
    return self.name
