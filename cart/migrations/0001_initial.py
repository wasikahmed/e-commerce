# Generated by Django 5.1.4 on 2024-12-30 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cartID', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
