from django.urls import path

from core.views import products_list, products_detail, category_list, category_detail

urlpatterns = [
    path('products/', products_list),
    path('products/<int:product_id>/', products_detail),
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_detail),
]
