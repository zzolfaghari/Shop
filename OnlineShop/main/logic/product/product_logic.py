from django.db.transaction import atomic

from main.dao.product.product_dao import ProductDao
from main.model.user.user_entity import User
from main.model.vo.product_vo import ProductVO


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

    def get_all_products(self, seller: User) -> None:
        return self.dao.get_all_products(seller)

    @atomic
    def update_product(self, product_id: int, **kwargs: dict):
        return self.dao.update_product(product_id, **kwargs)

    @atomic
    def delete_product(self, product_id: int, seller: User) -> None:
        return self.dao.delete_product(product_id, seller=seller)
