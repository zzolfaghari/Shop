from django.core.files.uploadedfile import InMemoryUploadedFile
from main.model.products.product_entity import Product, Image


class ProductDao:

    def create_product(self, **kwargs):
        return Product.objects.create(**kwargs)

    def create_product_images(self, product_id: int, image: InMemoryUploadedFile):
        return Image.objects.create(product_id=product_id, image=image)
