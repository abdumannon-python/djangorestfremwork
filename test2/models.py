from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=20)
    brand=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    razmer=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    stock=models.IntegerField()
    desc=models.TextField()





