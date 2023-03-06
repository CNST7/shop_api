from shop_app.shop_domain.models.item import Item
from shop_app.shop_domain.models.cart import Cart


class TestCart:
    # given
    mouse = Item(id=1, external_id="test #1", name="mouse", value=50)
    keyboard = Item(id=2, external_id="test #2", name="keyboard", value=10)

    def test_add_item_to_cart(self):
        # given
        cart = Cart()
        # when
        cart.add_item(self.mouse)
        # then
        assert self.mouse in cart.items

    def test_remove_item_from_cart(self):
        # given
        cart = Cart()
        # when
        cart.add_item(self.mouse)
        cart.remove_item(self.mouse)
        # then
        assert self.mouse not in cart.items

    def test_cart_value(self):
        # given
        cart = Cart()
        # when
        cart.add_item(self.mouse)
        cart.add_item(self.keyboard)
        # then
        assert cart.cart_value == self.mouse.value + self.keyboard.value  # type: ignore

    def test_add_item_multiple_times(self):
        # given
        cart = Cart()
        # when
        cart.add_item(self.mouse)
        cart.add_item(self.mouse)
        cart.add_item(self.mouse)
        # then
        assert len(cart.items) == 1

    def test_find_item_finds_item(self):
        # given
        cart = Cart()
        # when
        cart.add_item(self.mouse)
        cart.add_item(self.keyboard)
        found_item = cart.find_item(external_id=self.mouse.external_id)
        # then
        assert found_item is not None
        assert isinstance(found_item, Item)
        assert found_item == self.mouse
        assert found_item.external_id == self.mouse.external_id

    def test_find_item_does_not_finds_item(self):
        # given
        cart = Cart()
        # when
        item = cart.find_item("not existing item")
        # then
        assert item is None
