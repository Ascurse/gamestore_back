from django.urls import include, path
from rest_framework import routers

from .views import GameViewSet, GenreViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'genres', GenreViewSet, basename='genres')
router_v1.register(r'games', GameViewSet, basename='games')

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
