from django.urls import path, re_path

from api.views import hello, hours_ahead, products_list, products_detail, category_list, category_detail

urlpatterns = [
    path('hi/', hello),
    re_path(r'time/plus/(\d{1,2})/', hours_ahead),
    path('products/', products_list),
    path('products/<int:product_id>/', products_detail),
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_detail),
]
