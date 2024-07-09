from rest_framework import serializers

from main.model.products.product_entity import Image, Product
from main.shared.utils.shop_utils import ShopUtils


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=True, required=False, validators=[ShopUtils.check_image_format,
                                                                                        ShopUtils.validate_image_size,
                                                                                        ShopUtils.format_image_name], ),
        write_only=True,
        required=False, max_length=5
    )

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image']


class ProductsListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(source='image_set', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'creation_time', 'update_time', 'seller', 'images']
