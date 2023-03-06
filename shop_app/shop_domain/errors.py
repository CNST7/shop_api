class ShopBaseError(Exception):
    """Base error class for this project"""

    pass


class UpdateItemError(ShopBaseError):
    """Raised while item update fails"""

    pass
