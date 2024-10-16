from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image_url=models.URLField()# ****
    discount=models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    description=models.TextField()
    seller=models.ForeignKey(User, on_delete=models.CASCADE)
    related_name='products'




    def __str__ (self): 
         return self.name

