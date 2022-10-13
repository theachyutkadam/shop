from django.db import models

# Create your models here.
class Order(models.Model):
    id = models.CharField(max_length=20)
    total = models.CharField(max_length=100)
    class Meta:
        db_table = "order"
