from __future__ import unicode_literals
from django.db import models
from apps.clothing_admin.models import *

class User(models.Model):
    user_level=models.IntegerField(default=1)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    claimed_shirt=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    password=models.CharField(max_length=255, null=True)
    cohort=models.ForeignKey(Cohort, related_name='students', null=True)

class Cart(models.Model):
    user=models.OneToOneField(User, primary_key=True, null=False)
    total=models.DecimalField(max_digits=9, decimal_places=2, default=0)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, related_name='items')
    product=models.ForeignKey(Product, related_name='cart_items')
    color=models.ForeignKey(Color, related_name='cart_items')
    size=models.CharField(max_length=3, default='-')
    quantity=models.IntegerField()
    total=models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    # first_name=models.CharField(max_length=255)
    # last_name=models.CharField(max_length=255)
    # email=models.CharField(max_length=255)
    user=models.ForeignKey(User, related_name='orders', null=True)
    # cohort=models.CharField(max_length=255)
    # cohort=models.ForeignKey(Cohort, related_name='orders')
    total=models.DecimalField(max_digits=9, decimal_places=2)
    num_items=models.IntegerField(default=0)
    status=models.CharField(max_length=55, default='Unclaimed')
    location=models.ForeignKey(Location, related_name='orders', null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    ordered=models.BooleanField(default=False)

class OrderItem(models.Model):
    product=models.ForeignKey(Product, related_name='orders')
    order=models.ForeignKey(Order, related_name='items')
    size=models.CharField(max_length=3)
    # color=models.CharField(max_length=100)
    color=models.ForeignKey(Color, related_name='order_items')
    quantity=models.IntegerField()
    total=models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at=models.DateTimeField(auto_now_add=True)



# Create your models here.
