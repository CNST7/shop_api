from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.item import ItemSerializer
from ..errors.errorHandlingMethodWrapper import HandleErrors
from ..tasks import persist_cart
from ..DTOs.cart import CartDTO
from shop_app.shop_domain.models.item import Item as DomainItem


class ItemEndpoint(APIView):
    @HandleErrors
    def post(self, request: Request) -> Response:

        item_serializer = ItemSerializer(data=request.data)
        item_serializer.is_valid(raise_exception=True)

        cart = request.cart.to_domain()

        item = cart.find_item(request.data.get("external_id"))
        if item:
            item.name = request.data.get("name", item.name)
            item.value = request.data.get("value", item.value)
        else:
            item = DomainItem(**request.data)
            cart.add_item(item)

        persist_cart.delay(cart_dto=CartDTO.from_domain(cart).as_dict())
        return Response(status=status.HTTP_204_NO_CONTENT)
