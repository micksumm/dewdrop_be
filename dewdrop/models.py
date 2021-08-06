from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    ingredients = models.TextField()
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name

class Condition(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type 

class ProductConditionSolution(models.Model):
    product_id = models.ManyToManyField(Product)
    condition_id = models.ManyToManyField(Condition)

class Remedy(models.Model):
    product_id = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    condition_id = models.ForeignKey(Condition, related_name='condition', on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=100)
    remedies = models.ManyToManyField(Remedy)



