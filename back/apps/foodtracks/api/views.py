from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.response import Response
import pandas as pd
from geopy.distance import geodesic
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import TrackFoodSerializer
from apps.foodtracks.models import TrackFood
from django_filters.rest_framework import DjangoFilterBackend


class TrackFoodApiViewSet(ModelViewSet):
    permissions_classes = [IsAuthenticatedOrReadOnly]
    queryset = TrackFood.objects.all()
    serializer_class = TrackFoodSerializer
    filter_backends = [DjangoFilterBackend]

    def get_df(self):
        aux = TrackFood.objects.all().values("id", "latitude", "longitude")
        return pd.DataFrame.from_records(aux)

    def list(self, request, format=None):
        """
            Return a list of places
        """
        final = self.get_df()
        origin = (request.GET.get('lat'), request.GET.get('lng'))
        final['distance'] = final.apply(
            lambda x: self.compute_distance(
                origin,
                x["latitude"],
                x["longitude"]),
            axis=1)
        result = final.sort_values(by='distance').head(10)

        queryset = self.get_queryset().filter(id__in=result['id'].to_list())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def compute_distance(self, origin, latitude, longitude):
        final = (latitude, longitude)
        return geodesic(origin, final).kilometers
