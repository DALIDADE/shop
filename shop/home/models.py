from django.db import models
from django.contrib.auth.models import User

class Customer (models>Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255 ,null=True)
    email = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    data_order = models.DateTimeField(auto_now_add=True)
    complate = models.BooleanField(default=True)
    translation_id = models.CharField(max_length=255,null=True)

    def __str__(self):
        return str(self.id)


class OrderItiems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True,blank=True)
    address = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    zipcode = models.CharField(max_length=255,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address





