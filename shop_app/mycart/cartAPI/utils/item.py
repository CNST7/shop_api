from cartAPI.models import Item
from django.db.models import Q
import uuid


def get_item(external_id: str, cart_id: uuid.UUID | None = None) -> Item:
    """Gets specific Item

    Args:
        external_id (str): Item external id
        cart_id (uuid.UUID | None): Cart id

    Returns:
        Item: Returns Item entity

    Raises:
        Item.ObjectNotFound: When Item was not found in database
    """
    item: Item = Item.objects.select_related("cart").get(
        Q(external_id=external_id),
        Q(cart__id=cart_id) | Q(cart=None),
    )
    return item
