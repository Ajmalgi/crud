from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table ='customer_tb'

class Seller(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_name=models.IntegerField(default=0)
    account=models.BigIntegerField()
    phone=models.BigIntegerField()
    ifsc=models.BigIntegerField()
    address=models.CharField(max_length=30)
    seller_pic= models.ImageField(upload_to='seller/')



    class Meta:
        db_table ='seller_tb'
