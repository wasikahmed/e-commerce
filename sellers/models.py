from django.db import models

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    store_name = models.CharField(max_length=100)
    stroe_url = models.URLField()
    registration_date = models.DateField()
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
