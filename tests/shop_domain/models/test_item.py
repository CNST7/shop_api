from pytest import raises
from shop_app.shop_domain.models.item import Item
from pydantic import ValidationError


def test_create_item():
    item = Item(id=1, external_id="test", name="test", value=1)
    assert isinstance(item, Item)


def test_create_item_with_empty_name():
    item = Item(id=1, external_id="test", name=None, value=1)
    assert isinstance(item, Item)


def test_create_item_with_empty_value():
    item = Item(id=1, external_id="test", name="test", value=None)
    assert isinstance(item, Item)


def test_create_item_with_zero_value_raises_validation_error():
    with raises(ValidationError):
        Item(id=1, external_id="test", name="test", value=0)


def test_create_item_with_negtive_value_raises_validation_error():
    with raises(ValidationError):
        Item(id=1, external_id="test", name="test", value=-1)


def test_update_item_value_and_name():
    item = Item(id=1, external_id="test", name="old_name", value=1)

    item.name = "new_name"
    item.value = 2

    assert item.name == "new_name"
    assert item.value == 2


def test_update_item_value_with_zero_raises_error():
    item = Item(id=1, external_id="test", name="old_name", value=1)

    with raises(ValidationError):
        item.value = 0


def test_update_item_value_with_negative_value_raises_error():
    item = Item(id=1, external_id="test", name="old_name", value=1)

    with raises(ValidationError):
        item.value = -1
