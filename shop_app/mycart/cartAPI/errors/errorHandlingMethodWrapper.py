from functools import update_wrapper
from rest_framework.response import Response
from rest_framework import status
from shop_app.shop_domain import errors as shopDomainErrors


class HandleErrors:
    def __init__(self, func):
        self.func = func
        self.cache = dict()
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        try:
            x = self.func(self, *args, **kwargs)
            return x
        except shopDomainErrors.ShopBaseError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
