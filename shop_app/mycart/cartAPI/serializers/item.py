from rest_framework import serializers
from ..models import Item


class ItemAllFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ["id", "cart"]
