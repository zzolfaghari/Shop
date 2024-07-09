from django.contrib import admin

from main.model.products.product_entity import Product, Image
from main.model.user.user_entity import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'creation_time', 'update_time', 'seller')
    list_filter = ('seller', 'creation_time', 'update_time')
    search_fields = ('title', 'description')
    ordering = ('-creation_time',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ('product__title',)
    list_filter = ('product',)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'is_staff', 'type')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    ordering = ('username',)


