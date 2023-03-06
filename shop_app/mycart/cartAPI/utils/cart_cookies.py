from rest_framework.request import Request
from rest_framework.response import Response
from .configuration import CART_COOKIE_NAME, COOKIE_EXPIRATION_TIME_IN_HOURS
from rest_framework import status
from datetime import datetime, timedelta
import uuid


def get_cart_id_from_client(request: Request) -> uuid.UUID | None:
    """Gets Cart object from database

    Args:
        request (Request): rest framework Request object

    Returns:
        uuid.UUID | None: returns Cart id (UUID) if it was previously set in client cookies, else returns None
    """
    cookie: str | None = request.COOKIES.get(CART_COOKIE_NAME)
    if not cookie:
        return None
    try:
        cookie_uuid = uuid.UUID(cookie)
    except:
        return None
    return cookie_uuid


def save_cart_cookie(
    cart_id_cookie_value: uuid.UUID,
    response: Response | None = Response(status=status.HTTP_204_NO_CONTENT),
) -> Response:
    """Prepares response with saved Cart cookie and expiration time

    Args:
        cart_id_cookie_value (uuid.UUID): cart UUID that will be save as a cookie

    Returns:
        Response: Returns prepared rest_framework Response
    """
    expires_on: datetime = datetime.now() + timedelta(
        hours=COOKIE_EXPIRATION_TIME_IN_HOURS
    )
    response.set_cookie(CART_COOKIE_NAME, str(cart_id_cookie_value), expires=expires_on)  # type: ignore
    return response
