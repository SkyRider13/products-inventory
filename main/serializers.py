from rest_framework import serializers, exceptions
from .models import Category, Product

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class ProductCreateSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['id','name', 'description', 'price', 'brand', 'stock', 'category']

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'brand', 'category']
        

        
