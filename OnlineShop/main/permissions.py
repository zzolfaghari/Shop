from rest_framework.permissions import BasePermission

from main.enum.user_type import UserType


class IsProducerOrAdmin(BasePermission):
    """
    Allows access only to users with the 'producer' user type.
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and request.user.type == UserType.PRODUCER.value) or request.user.is_superuser
