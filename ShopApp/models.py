from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    weight = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
