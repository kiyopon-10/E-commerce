# serializers.py
from rest_framework import serializers
from .models import Product, CartItem


class ProductSerializer(serializers.ModelSerializer):
    
    tag = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        fields = '__all__'
        
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
