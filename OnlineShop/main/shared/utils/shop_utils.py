import re

from PIL import Image
from django.core.exceptions import ValidationError
from rest_framework import serializers


class ShopUtils:

    @staticmethod
    def get_product_image_path(image, filename: str) -> str:
        return 'products/{0}/images/{1}'.format(image.product.id, filename)

    @staticmethod
    def format_image_name(image):
        image.name.replace(' ', '-')

    @staticmethod
    def check_image_format(image):
        valid_formats = ['JPEG', 'PNG']
        try:
            img = Image.open(image)
            if img.format not in valid_formats:
                raise ValidationError(f"Unsupported image format. Allowed formats: {', '.join(valid_formats)}")
        except IOError:
            raise ValidationError("Invalid image file.")

    @staticmethod
    def validate_image_size(image):
        if image.size > 2 * 1024 * 1024:
            raise ValidationError("The maximum file size that can be uploaded is 2MB")
        return image

    @staticmethod
    def validate_username(username):
        if username.isnumeric():
            raise serializers.ValidationError("username must have characters too!")

    @staticmethod
    def validate_password(password):
        if len(password) < 5:
            raise serializers.ValidationError("Make sure the length of your password is more than 5 characters")
        elif re.search('[A-Z]', password) is None:
            raise serializers.ValidationError("Make sure your password has a capital letter in it")

