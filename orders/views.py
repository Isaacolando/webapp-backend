from django.shortcuts import render
from rest_framework import viewsets
from .models import Cart,Order
from .serilaizer import CartSerializer,OrderSerializer



class CartViewSet(viewsets.ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
