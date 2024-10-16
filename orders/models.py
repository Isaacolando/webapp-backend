from django.db import models
from django.contrib.auth.models import User
from products.models import  Product

class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    products=models.ManyToManyField(Product,
                                    through='CartItem')
class CartItem(models.Model):
        cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
        product=models.ForeignKey(Product,
                                  on_delete=models.CASCADE)
        quantity=models.PositiveIntegerField(default=1)

class Order(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      products=models.ManyToManyField(Product, through='OrderItem')
      created_at =models.DateTimeField(auto_now_add=True)
      total=models.DecimalField(max_digits=10, decimal_places=2)
      is_paid=models.BooleanField(default=False)
class OrderItem(models.Model):
      order=models.ForeignKey(Order, on_delete=models.CASCADE)
      product=models.ForeignKey(Product,
                               on_delete=models.CASCADE )
      quantity=models.PositiveIntegerField(default=1)
      price=models.DecimalField(max_digits=10, decimal_places=2)

