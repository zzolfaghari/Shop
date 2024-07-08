from django.urls import path

from main.api.controller.registration.login_controller import LoginController
from main.api.controller.registration.register_controller import RegisterController

urlpatterns = [
    path('register/', RegisterController.as_view({'post': 'post'}), name='create_register'),
    path('login/', LoginController.as_view({'post': 'post'}), name='login'),
]