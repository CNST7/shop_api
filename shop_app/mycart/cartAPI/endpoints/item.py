from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from dataclasses import asdict
from ..serializers.item import ItemSerializer
from ..tasks import save_item_task
from ..DTOs.item import ItemDTO


class ItemEndpoint(APIView):
    def post(self, request: Request) -> Response:
        # validate body
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # prepare DTO
        validated_data = {**serializer.validated_data}
        validated_data["cart"] = request.cart.id
        save_item_dto = ItemDTO(**validated_data)

        # async save in database
        save_item_task.delay(asdict(save_item_dto))

        return Response(status=status.HTTP_204_NO_CONTENT)
