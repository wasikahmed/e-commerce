from django.db import models

from sellers.models import Seller

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    seller = models.ForeignKey(
        Seller,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        blank=True,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
    

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} - {self.stock_quantity}'
    