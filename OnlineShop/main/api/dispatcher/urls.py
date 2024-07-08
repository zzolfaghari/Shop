from django.urls import include, path

urlpatterns = [

    path('products/', include('main.api.dispatcher.product.product_dispatcher')),
]