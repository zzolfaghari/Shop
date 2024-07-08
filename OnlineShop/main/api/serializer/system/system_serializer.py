from rest_framework import serializers


class ResponseSerializer(serializers.Serializer):
    default_message = serializers.CharField()
    default_status_code = serializers.IntegerField(min_value=0)
