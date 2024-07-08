from django.db.transaction import atomic

from main.dao.product.product_dao import ProductDao


class ProductLogic:

    def __init__(self):
        self.dao = ProductDao()

    @atomic
    def create_product(self, **kwargs: dict):
        product = self.dao.create_product(**kwargs)
        if ProductVO.image in kwargs:
            list_of_images = kwargs.pop(ProductVO.image)
            for image in list_of_images:
                self.dao.create_product_images(product_id=product.id, image=image)
