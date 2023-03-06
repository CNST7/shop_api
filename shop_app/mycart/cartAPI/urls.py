from django.urls import path
from rest_framework import routers
from django.urls import include

from .endpoints.item import ItemEndpoint

from .endpoints.item_using_domain import ItemEndpoint as ItemDomainEndpoint
from .endpoints.generic import CartViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r"carts", CartViewSet)
router.register(r"items", ItemViewSet)


urlpatterns = [
    path("item", ItemEndpoint.as_view(), name="Item"),
    path("itemDomain", ItemDomainEndpoint.as_view(), name="ItemDomain"),
    path("generic/", include(router.urls)),
]
