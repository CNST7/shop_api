from shop_app.shop_domain.models.item import Item
from pydantic import BaseModel, Field
import uuid


class Cart(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    items: set[Item] = Field(default_factory=set)

    def add_item(self, item: Item) -> None:
        """Adds Item to Cart

        Args:
            item (Item): Item entity

        Raises:
            ItemAlreadyAssignedToCartError: Raised while trying to assign Item that is already assigned to a different Cart
        """

        self.items.add(item)

    def remove_item(self, item: Item) -> None:
        """Removes Item from Cart

        Args:
            item (Item): Item entity that will be removed from Cart
        """
        self.items.remove(item)

    @property
    def cart_value(self) -> int:
        """Computes value of Items that are currently assigned to this Cart

        Returns:
            int: Returns Cart value
        """
        return sum([item.value for item in self.items if item.value])

    def __hash__(self) -> int:
        return hash(self.id)

    def find_item(self, external_id: str) -> Item | None:
        return next(
            (item for item in self.items if item.external_id == external_id), None
        )
