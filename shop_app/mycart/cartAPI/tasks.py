from cartAPI.models import Cart, Item
from celery import shared_task
from django.db import transaction
from cartAPI.DTOs.item import ItemDTO
from cartAPI.DTOs.cart import CartDTO


@shared_task
def save_item_task(item_dto: dict):
    # TODO this can be improved!
    # read data
    received_item_dto = ItemDTO(**item_dto)
    cart = Cart(id=received_item_dto.cart)
    item: Item
    try:
        # patch item
        item = Item.objects.get(external_id=received_item_dto.external_id, cart=cart)
        item.name = received_item_dto.name or item.name
        item.value = received_item_dto.value or item.value
    except Item.DoesNotExist:
        # create item
        item = Item(
            external_id=received_item_dto.external_id,
            cart=cart,
            name=received_item_dto.name,
            value=received_item_dto.value,
        )
    # save in database
    with transaction.atomic():
        if not Cart.objects.filter(id=cart.id).exists():
            cart.save()
        item.save()


@shared_task
def persist_cart(cart_dto: dict):
    received_cart = CartDTO.from_dict(cart_dto)
    cart, _ = Cart.objects.get_or_create(id=received_cart.id)
    items = [Item(**item.dict(), cart=cart) for item in received_cart.items]

    with transaction.atomic():
        for item in items:
            item.save()
