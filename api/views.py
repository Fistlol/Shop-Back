from django.http.response import HttpResponse, JsonResponse

from core.models import Product, Category


def hello(request):
    return HttpResponse('<h1>Hello message</h1>')


def hours_ahead(request, hours):
    return HttpResponse(f'<h1>Hours ahead: {hours}</h1>')


def products_list(request):
    # select * from core_product;
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def products_detail(request, product_id):
    # select * from core_product where id = product_id;
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    return JsonResponse(product.to_json())


def category_list(request):
    # select * from core_product;
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    # select * from core_product where id = category_id;
    try:
        category = Category.objects.get(id=category_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(category.to_json())


# def products_list(request):
#     return HttpResponse('<h1>List of Products</h1>')
#
#
# def products_detail(request, product_id):
#     return HttpResponse(f'<h1>Product Page: {product_id}</h1>')

# products = [
#     {
#         'id': i,
#         'name': f'Product {i}',
#         'price': i * 1000
#     } for i in range(1, 11)
# ]
#
#
# def products_list(request):
#     return JsonResponse(products, safe=False)
#
#
# def products_detail(request, product_id):
#     for product in products:
#         if product['id'] == product_id:
#             return JsonResponse(product)
#     return JsonResponse({'message': 'Product with selected ID not found'})
#
#
# def category_list(request):
#     return HttpResponse('<h1>List of Categories</h1>')
#
#
# def category_detail(request, category_id):
#     return HttpResponse(f'<h1>Category Page: {category_id}</h1>')
