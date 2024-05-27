from django.urls import path
from .views import CategoryListEndpoint, AddCategoryEndpoint, ProductEndpoint

urlpatterns = [
    path('add/category', AddCategoryEndpoint.as_view(), name = "add-cate"),
    path('categories', CategoryListEndpoint.as_view(), name = "categories"),
    path('products', ProductEndpoint.as_view(), name = "products"),
]