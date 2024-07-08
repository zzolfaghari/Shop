from rest_framework import serializers

from main.model.user.user_entity import User
from main.shared.utils.shop_utils import ShopUtils


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[ShopUtils.validate_username])
    password = serializers.CharField(validators=[ShopUtils.validate_password])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']