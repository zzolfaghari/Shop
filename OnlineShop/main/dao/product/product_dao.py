from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import get_object_or_404

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

    def update_product(self, product_id: int, **kwargs):
        images = kwargs.pop(ProductVO.image)
        query_set = Product.objects.prefetch_related(ProductVO.image_set).filter(id=product_id)
        query_set.update(**kwargs)
        product = query_set.first()
        if len(product.image_set.all()) < 5:
            if images is not None:
                for img in images:
                    Image.objects.create(product_id=product_id, image=img)
        else:
            raise ValueError('you should delete one of your images before')

    def delete_product(self, product_id: int, seller: User) -> None:
        product = get_object_or_404(Product, id=product_id, seller=seller)

        images = Image.objects.filter(product=product)

        images.delete()

        product.delete()
        # set is_deleted=True

