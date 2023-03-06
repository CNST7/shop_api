from django.urls import reverse
from rest_framework import status
from django.test.client import AsyncClient
from asgiref.sync import sync_to_async
from cartAPI.models import Item, Cart
from cartAPI.utils.configuration import CART_COOKIE_NAME
import uuid

import pytest
from django.test import override_settings

ITEM_EXTERNAL_ID: str = "test"
ITEM_NAME: str = "test_obj"
ITEM_VALUE: int = 15
NEW_ITEM_NAME: str = "new_test_obj"
NEW_ITEM_VALUE: int = 30
DATA = {
    "external_id": ITEM_EXTERNAL_ID,
    "name": NEW_ITEM_NAME,
    "value": NEW_ITEM_VALUE,
}
URL = reverse("ItemDomain")

# TODO refactor tests
pytestmark = pytest.mark.django_db(transaction=True)


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
@pytest.mark.asyncio
async def test_add_new_item_creates_new_cart():
    # when
    # adds ITEM to CART, updates it with new .name and .value if those
    # fields were passed in request body (in this case they should be updated)
    async_client = AsyncClient()

    response = await async_client.post(
        URL,
        data=DATA,
        format="json",
        content_type="application/json",
    )

    # then
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # checks if ITEM .name and .value were updated as intended
    expected_cart_id = response.cookies[CART_COOKIE_NAME].value
    cart = Cart(id=uuid.UUID(expected_cart_id))

    # TODO avoid constants
    # TODO avoid many variables in tests, literals are better

    created_item = await Item.objects.select_related("cart").aget(
        external_id=ITEM_EXTERNAL_ID
    )
    assert created_item.value == NEW_ITEM_VALUE
    assert created_item.name == NEW_ITEM_NAME
    assert created_item.cart.id == cart.id


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
@pytest.mark.asyncio
async def test_add_new_item_to_existing_cart():
    # given
    existing_cart_id = "be988522-941d-45d5-8868-ad99c8effb7d"

    @sync_to_async
    def create_cart():
        Cart(id=existing_cart_id).save()

    await create_cart()

    async_client = AsyncClient()
    async_client.cookies[CART_COOKIE_NAME] = existing_cart_id

    await async_client.post(
        URL,
        data={
            "external_id": "test",
            "name": "item_name",
            "value": 15,
        },
        format="json",
        content_type="application/json",
    )

    # then
    created_item = await Item.objects.select_related("cart").aget(external_id="test")

    assert created_item.cart.id == uuid.UUID(existing_cart_id)


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
@pytest.mark.asyncio
async def test_add_new_item_to_cart_that_does_not_exist():
    # given
    not_existing_cart_id = "be988522-941d-45d5-8868-ad99c8effb7d"
    async_client = AsyncClient()
    async_client.cookies[CART_COOKIE_NAME] = not_existing_cart_id

    # when
    response = await async_client.post(
        URL,
        data=DATA,
        format="json",
        content_type="application/json",
    )

    # then
    created_item = await Item.objects.select_related("cart").aget(
        external_id=ITEM_EXTERNAL_ID
    )

    assert created_item.cart.id != uuid.UUID(not_existing_cart_id)
    assert created_item.cart.id == uuid.UUID(response.cookies[CART_COOKIE_NAME].value)


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
@pytest.mark.asyncio
async def test_add_new_item_to_cart_that_has_specified_only_required_fields():
    # given
    item_external_id = "required_external_id"
    body = {"external_id": item_external_id}

    # when
    async_client = AsyncClient()
    await async_client.post(
        URL,
        data=body,
        format="json",
        content_type="application/json",
    )

    # then
    created_item = await Item.objects.select_related("cart").aget(
        external_id=item_external_id
    )

    assert created_item.cart.id != None
    assert created_item.external_id == item_external_id
    assert created_item.value is None
    assert created_item.name is None
