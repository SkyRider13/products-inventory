from rest_framework import serializers, exceptions
from .models import Category, Product

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'brand', 'stock', 'category']