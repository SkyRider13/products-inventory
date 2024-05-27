from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 50)

class Product(models.Model):
    name =  models.CharField(max_length = 200)
    description = models.CharField(max_length = 10000)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length = 100)
    stock = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    

    
    