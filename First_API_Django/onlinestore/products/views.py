
from django.http import JsonResponse
from .models import Manufacturer, Product


def product_list(request):
    products = Product.objects.all()
    data = { 
        "products" : list(products.values())
    }
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "shipping_cost": product.shipping_cost,
            "quantity": product.quantity
        }}

        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": { "code": 404,
            "message": "product Does Not Exist"
        }}, status=404)

    return response


def manufacturer_details(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
    except Manufacturer.DoesNotExist:
        response = JsonResponse(
            {
                "error": {
                    "code": 404,
                    "message": "manufacturer not found"
                }
            }, status=404
        )
    else:
        manufacturer_product = manufacturer.products.all()
        data = {
            "manufacturer": {
                "name": manufacturer.name,
                "location": manufacturer.location,
                "active": manufacturer.active,
                "products": list(manufacturer_product.values()),
            }
        }
        response = JsonResponse(data)
    return response

def manufacturer_list(request):
    manufacturer = Manufacturer.objects.filter(active=True)
    data = {"manufacturers": list(manufacturer.values())}
    response = JsonResponse(data)
    return response

# def active_manufacturers(request):
#     manufacturer = Manufacturer.objects.all()
#     active_users = []
#     for obj in manufacturer:
#         if obj.active == True:
#             active_users.append(obj.name)
#     data = {
#         "active_users": active_users,
#     }
#     return JsonResponse(data)

# Create your views here.

# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"