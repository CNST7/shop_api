from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from cartAPI.utils.configuration import (
    CART_COOKIE_NAME,
    COOKIE_EXPIRATION_TIME_IN_HOURS,
)
from uuid import UUID
from cartAPI.utils.cart_cookies import get_cart_id_from_client, save_cart_cookie
from datetime import datetime, timedelta

STR_COOKIE_VAL: str = "1fdd9f82-31b0-4ecb-8f0b-6baec5fecaac"
UUID_COOKIE_VAL: UUID = UUID(STR_COOKIE_VAL)


def test_get_cart_id_from_cookie():
    # given:
    request: Request = APIRequestFactory().request()
    request.COOKIES = {CART_COOKIE_NAME: STR_COOKIE_VAL}
    # when:
    cart_cookie = get_cart_id_from_client(request=request)
    # then:
    assert cart_cookie == UUID_COOKIE_VAL


def test_save_cart_id_as_cookie():
    # when:
    COOKIE_EXPIRATION_OFFSET_IN_MINUTES: int = 2
    resp: Response = save_cart_cookie(cart_id_cookie_value=UUID_COOKIE_VAL)
    # then:
    # checks cookie value
    assert resp.cookies[CART_COOKIE_NAME].value == STR_COOKIE_VAL
    cookie_expiration: datetime = datetime.strptime(
        resp.cookies[CART_COOKIE_NAME]["expires"], "%a, %d %b %Y %H:%M:%S %Z"
    )
    # checks cookie expiration time
    assert cookie_expiration > datetime.now() + timedelta(
        hours=COOKIE_EXPIRATION_TIME_IN_HOURS
    ) - timedelta(minutes=COOKIE_EXPIRATION_OFFSET_IN_MINUTES)
    assert cookie_expiration < datetime.now() + timedelta(
        hours=COOKIE_EXPIRATION_TIME_IN_HOURS
    ) + timedelta(minutes=COOKIE_EXPIRATION_OFFSET_IN_MINUTES)
