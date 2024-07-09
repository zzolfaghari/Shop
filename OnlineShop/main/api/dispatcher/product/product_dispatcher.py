from django.urls import path

from main.api.controller.product.product_controller import ProductController

urlpatterns = [
    path('', ProductController.as_view({'post': 'post'}), name='create_product'),
    path('list/', ProductController.as_view({'get': 'products_list'}), name='get_all_products'),
]