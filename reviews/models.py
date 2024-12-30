from django.db import models

from products.models import Product
from users.models import Customer


# Create your models here.
class Review(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    Comment = models.TextField()
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.CustomerID} rated {self.ProductID} {self.Rating} stars'
