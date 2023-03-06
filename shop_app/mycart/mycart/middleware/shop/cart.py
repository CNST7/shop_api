from cartAPI.utils.cart_cookies import get_cart_id_from_client, save_cart_cookie
from cartAPI.utils.cart import get_or_create_cart, aget_or_create_cart
from django.urls import reverse
import asyncio
from django.utils.decorators import sync_and_async_middleware


@sync_and_async_middleware
def Middleware(get_response):
    # One-time configuration and initialization.
    # This middleware will be used only with endpoints registered in path_registry
    path_registry: list[str] = list()
    path_registry.append(f"/{reverse('Item').split('/')[1]}")
    path_registry.append(f"/{reverse('ItemDomain').split('/')[1]}")

    if asyncio.iscoroutinefunction(get_response):

        async def middleware(request):
            path = request.get_full_path()
            apply_middleware = False
            for registered_path in path_registry:
                if path.startswith(registered_path):
                    apply_middleware = True
                    break
            if apply_middleware:
                cart_id = get_cart_id_from_client(request=request)
                request.cart = await aget_or_create_cart(cart_id_from_client=cart_id)
                response = await get_response(request)
                response = save_cart_cookie(
                    cart_id_cookie_value=request.cart.id, response=response
                )
            else:
                response = await get_response(request)
            return response

    else:

        def middleware(request):
            path = request.get_full_path()
            apply_middleware = False
            for registered_path in path_registry:
                if path.startswith(registered_path):
                    apply_middleware = True
                    break
            if apply_middleware:
                cart_id = get_cart_id_from_client(request=request)
                request.cart = get_or_create_cart(cart_id_from_client=cart_id)
                response = get_response(request)
                response = save_cart_cookie(
                    cart_id_cookie_value=request.cart.id,
                    response=response,
                )
            else:
                response = get_response(request)
            return response

    return middleware
