from rest_framework import routers

from sign.views import SignViewSet

router = routers.DefaultRouter()
router.register(r'sign', SignViewSet)