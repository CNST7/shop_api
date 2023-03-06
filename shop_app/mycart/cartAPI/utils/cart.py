from cartAPI.models import Cart
import uuid


def get_or_create_cart(cart_id_from_client: uuid.UUID | None) -> Cart:
    """Gets Cart object from database based on `cart_id_from_client` value
        or creates new Cart object (if `cart_id_from_client` was None).
        If value is incorrect or Cart was previously removed from db for some reason
        creates new Cart entity.


    Args:
        cart_id_from_client (uuid.UUID | None): Cart ID from client,
            might be empty if user visits endpoint for 1st time

    Returns:
        Cart: Returns Cart object
    """
    try:
        cart_persistent = Cart.objects.prefetch_related("item_set").get(
            pk=cart_id_from_client
        )
    except Cart.DoesNotExist:
        cart_persistent = Cart()
    return cart_persistent


async def aget_or_create_cart(cart_id_from_client: uuid.UUID | None) -> Cart:
    """Gets Cart object from database based on `cart_id_from_client` value
        or creates new Cart object (if `cart_id_from_client` was None).
        If value is incorrect or Cart was previously removed from db for some reason
        creates new Cart entity.


    Args:
        cart_id_from_client (uuid.UUID | None): Cart ID from client,
            might be empty if user visits endpoint for 1st time

    Returns:
        Cart: Returns Cart object
    """
    try:
        cart_persistent = await Cart.objects.prefetch_related("item_set").aget(
            pk=cart_id_from_client
        )
    except Cart.DoesNotExist:
        return Cart()
    return cart_persistent
