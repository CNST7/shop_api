from cartAPI.models import Cart, Item
from cartAPI.serializers.cart import CartSerializer
from cartAPI.serializers.item import ItemAllFieldSerializer
from rest_framework import viewsets


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.prefetch_related("item_set").all()
    serializer_class = CartSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.select_related("cart").all()
    serializer_class = ItemAllFieldSerializer
