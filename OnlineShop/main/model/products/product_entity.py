from django.db import models

from main.model.user.user_entity import User
from main.shared.utils.shop_utils import ShopUtils


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    creation_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    # use BaseModel

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=ShopUtils.get_product_image_path, validators=[ShopUtils.check_image_format,
                                                                                      ShopUtils.validate_image_size,
                                                                                      ShopUtils.format_image_name])

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
