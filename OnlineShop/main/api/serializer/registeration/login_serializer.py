from rest_framework import serializers

from main.shared.utils.shop_utils import ShopUtils


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(validators=[ShopUtils.validate_username], required=True)
    password = serializers.CharField(validators=[ShopUtils.validate_password], required=True)