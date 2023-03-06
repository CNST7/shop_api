from django.db import models
from .validators.item_validator import validate_is_item_value_greater_than_zero
from shop_app.shop_domain import models as domain
import uuid


class Cart(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField()
    # created_in_db_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField()
    # updated_in_db_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Cart #{self.id}"

    def to_domain(self) -> domain.Cart:
        return domain.Cart(
            id=self.id, items=set([item.to_domain() for item in self.item_set.all()])
        )


class Item(models.Model):
    external_id = models.TextField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    name = models.TextField(
        blank=True,
        default=None,
        null=True,
    )
    value = models.PositiveIntegerField(
        blank=True,
        default=None,
        null=True,
        validators=[validate_is_item_value_greater_than_zero],
    )

    def __str__(self) -> str:
        return f"Item #{self.external_id} at Cart #{self.cart.id} "

    def to_domain(self) -> domain.Item:
        return domain.Item(
            external_id=self.external_id, name=self.name, value=self.value
        )
