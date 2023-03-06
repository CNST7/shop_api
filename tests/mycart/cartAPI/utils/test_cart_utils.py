import pytest
from uuid import UUID
from cartAPI.utils.cart import get_or_create_cart
from cartAPI.models import Cart


@pytest.mark.django_db
def test_create_cart():
    # given
    cart_id_from_cookie: UUID | None = None
    # when
    cart: Cart = get_or_create_cart(cart_id_from_client=cart_id_from_cookie)
    # then
    with pytest.raises(Cart.DoesNotExist):
        Cart.objects.get(pk=cart.id)

    cart.save()
    cart_from_db = Cart.objects.get(pk=cart.id)
    assert isinstance(cart_from_db, Cart)


@pytest.mark.django_db
def test_get_cart():
    # given
    cart = Cart()
    cart.save()
    # when
    acquired_cart = get_or_create_cart(cart_id_from_client=cart.id)
    # then
    cart_from_db = Cart.objects.get(pk=cart.id)
    assert acquired_cart == cart_from_db
