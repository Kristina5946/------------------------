from django.db import models
from django.contrib.auth.models import Userclass 

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # или используйте User model
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

