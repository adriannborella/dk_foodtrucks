from rest_framework.routers import DefaultRouter
from apps.foodtracks.api.views import TrackFoodApiViewSet

router_api = DefaultRouter()

router_api.register(prefix='trackfoods',
                       basename='trackfoods',
                       viewset=TrackFoodApiViewSet)
