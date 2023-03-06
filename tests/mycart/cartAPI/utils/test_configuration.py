from cartAPI.utils.configuration import (
    CART_COOKIE_NAME,
    COOKIE_EXPIRATION_TIME_IN_HOURS,
)


def test_CART_COOKIE_NAME_is_not_changed():
    assert CART_COOKIE_NAME == "cart_id"


def test_COOKIE_EXPIRATION_TIME_IN_HOURS_is_not_changed():
    assert COOKIE_EXPIRATION_TIME_IN_HOURS == 72
