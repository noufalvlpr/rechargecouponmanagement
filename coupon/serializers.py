from rest_framework import serializers


class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
