from django.urls import path
from .views import product_list, product_detail, manufacturer_details, manufacturer_list

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
    path("manufacturer/<int:pk>/", manufacturer_details, name="manufaturer-details"),
    path("active/", manufacturer_list, name="active-manufacturers"),
]