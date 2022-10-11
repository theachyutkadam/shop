from dataclasses import fields
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Customer(models.Model):
  first_name = models.CharField(max_length=25)
  last_name  = models.CharField(max_length=25)
  email      = models.CharField(max_length=30)
  contact    = models.CharField(max_length=10)
  desc       = models.TextField()

  def __str__(self):
    return self.first_name

# models.py create class customer with fields
# create form.py file for single form page, like form in ruby addjust new/edit
# admin.py  import and register in admin panel.``
