from rest_framework.serializers import ModelSerializer
from ..models import Cart
from ..serializers.item import ItemSerializer


class CartSerializer(ModelSerializer):
    items = ItemSerializer(source="item_set", many=True, required=False)

    class Meta:
        model = Cart
        fields = ["id", "created_at", "items"]
