from django.db import models

# 1. Staff
# * Attributes:
#     * StaffID (Primary Key)
#     * Name
#     * Email (Unique)
#     * Phone
#     * Role (e.g., Admin, Support, Manager)
#     * PasswordHash
#     * CreatedAt
#     * UpdatedAt

class Staff(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Support', 'Support'),
        ('Management', 'Management'),
        ('IT', 'IT'),
    ]
    
    StaffID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Phone = models.CharField(max_length=15)
    Role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='IT')
    Password = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
