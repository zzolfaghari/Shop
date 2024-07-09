from django.core.files.uploadedfile import InMemoryUploadedFile
from main.model.products.product_entity import Product, Image
from main.model.user.user_entity import User
from main.model.vo.product_vo import ProductVO


class ProductDao:

    def create_product(self, **kwargs):
        return Product.objects.create(**kwargs)

    def create_product_images(self, product_id: int, image: InMemoryUploadedFile):
        return Image.objects.create(product_id=product_id, image=image)

    def get_all_products(self, seller: User) -> None:
        return Product.objects.prefetch_related(ProductVO.image_set).filter(seller=seller)
