from django.urls import include, path

urlpatterns = [

    path('products/', include('main.api.dispatcher.product.product_dispatcher')),
    path('auth/', include('main.api.dispatcher.registration.register_dispatcher')),
]