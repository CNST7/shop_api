from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_is_item_value_greater_than_zero(value: int):
    if value <= 0:
        raise ValidationError(
            _("Item value %(value)s is not is not greater than zero"),
            params={"value": value},
        )
