from django.urls import path
from rest_framework import routers
from django.urls import include
from . import endpoints

router = routers.DefaultRouter()
router.register(r"carts", endpoints.CartViewSet)
router.register(r"items", endpoints.ItemViewSet)


urlpatterns = [
    path("item", endpoints.ItemEndpoint.as_view(), name="Item"),
    path("itemDomain", endpoints.ItemDomainEndpoint.as_view(), name="ItemDomain"),
    path("generic/", include(router.urls)),
]
