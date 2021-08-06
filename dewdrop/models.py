from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Condition(models.Model):
    type = models.CharField(max_length=20)
    # products

    def __str__(self):
        return self.type 

class Product(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    description = models.TextField()
    link = models.URLField()
    conditions = models.ManyToManyField(Condition, related_name='products')


    def __str__(self):
        return self.name

# class ProductConditionSolution(models.Model):
#     product_id = models.ManyToManyField(Product)
#     condition_id = models.ManyToManyField(Condition)

class Remedy(models.Model):
    products = models.ManyToManyField(Product, related_name='product')
    conditions = models.ManyToManyField(Condition, related_name='condition')
    customer = models.ForeignKey(User,related_name="remedies", on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=100)
    # remedies 




