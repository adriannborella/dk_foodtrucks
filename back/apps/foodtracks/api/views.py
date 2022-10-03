from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
import requests
import pandas as pd
from geopy.distance import geodesic
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from src.settings.config.dir import BASE_DIR


class TrackFoodApiViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_df(self):
        url = f"{BASE_DIR.ancestor(1)}/rqzj-sfat.csv"
        df = pd.read_csv(url)
        clean_df = df[['objectid', 'applicant', 'facilitytype',
                       'locationdescription', 'latitude', 'longitude',
                       'address', 'schedule', 'facilitytype']]
        clean_df = clean_df.dropna()
        return clean_df

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
        return Response(result.to_dict('records'))

    def compute_distance(self, origin, latitude, longitude):
        final = (latitude, longitude)
        return geodesic(origin, final).kilometers
