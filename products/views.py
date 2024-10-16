from django.shortcuts import render
from rest_framework import viewsets
from .models import product
from serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=ProductSerializer

