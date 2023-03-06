from uuid import uuid4
import pytest
from cartAPI.models import Item, Cart
from cartAPI.utils.item import get_item


@pytest.mark.django_db
def test_get_not_existing_item_raises_error():
    with pytest.raises(Item.DoesNotExist):
        get_item(external_id="not existing item", cart_id=None)


@pytest.mark.django_db
def test_get_item():
    cart_id = uuid4()
    item_external_id: str = "test_item"
    item_name: str = "mouse"
    item_value: int = 15
    # given
    cart = Cart.objects.create(id=cart_id)
    item = Item.objects.create(
        external_id=item_external_id,
        name=item_name,
        value=item_value,
        cart=cart,
    )
    # when
    retrived_item = get_item(external_id=item_external_id, cart_id=cart.id)
    # then
    assert item.id == retrived_item.id
    assert item == retrived_item
