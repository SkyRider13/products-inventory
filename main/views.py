from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Category, Product
from .serializers import CategorySerializer, ProductCreateSerializer, ProductSerializer

# Create your views here.

class AddCategoryEndpoint(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    
class CategoryListEndpoint(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    
class ProductEndpoint(generics.ListCreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()