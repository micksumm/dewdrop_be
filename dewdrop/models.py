from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name
    
class Condition(models.Model):
    type = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.type

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    conditions = models.ManyToManyField(Condition)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

