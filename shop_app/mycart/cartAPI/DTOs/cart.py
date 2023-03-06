from __future__ import annotations
from pydantic import BaseModel, Field
from uuid import UUID
from shop_app.shop_domain.models.cart import Cart
from shop_app.shop_domain.models.item import Item


class ItemDTO(BaseModel):
    id: int | None = None
    external_id: str
    name: str | None = None
    value: int | None = None

    def __hash__(self):
        return hash(self.external_id)

    @classmethod
    def from_domain(cls, item: Item) -> ItemDTO:
        item_dict = dict(item)
        return cls(**item_dict)


class CartDTO(BaseModel):
    id: UUID
    items: set[ItemDTO] = Field(default_factory=set)

    def as_dict(self):
        return {"id": self.id, "items": [dict(item) for item in self.items]}

    @classmethod
    def from_dict(cls, data: dict) -> CartDTO:
        items = {ItemDTO(**item) for item in data["items"]}
        return cls(id=data["id"], items=items)

    @classmethod
    def from_domain(cls, cart: Cart) -> CartDTO:
        items = {ItemDTO.from_domain(item) for item in cart.items}
        return cls(id=cart.id, items=items)


# mouse = ItemDTO(external_id="mouse")
# keyboard = ItemDTO(external_id="keyboard")

# my_cart = CartDTO(id=uuid4())

# my_cart.items.add(mouse)
# my_cart.items.add(keyboard)

# my_cart_dict = my_cart.as_dict()

# my_cart_from_dict = CartDTO.from_dict(my_cart_dict)
