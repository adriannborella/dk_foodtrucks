from django.test import TestCase
from unittest.mock import Mock, patch, MagicMock
from apps.foodtracks.api.views import TrackFoodApiViewSet
import pandas as pd
from rest_framework.response import Response


class TestViewSet(TestCase):

    def setUp(self):
        self.instance = TrackFoodApiViewSet()

    def test_compute_distance(self):
        expected = 3.388064929311577
        result = self.instance.compute_distance(
            (37.791303, -122.398956),
            37.7639891554711,
            -122.41612672805788)
        self.assertEqual(expected, result)

    @patch("pandas.DataFrame.from_records")
    def test_get_df(self, from_records):
        from_records.return_value = "success"
        expected = "success"
        result = self.instance.get_df()
        self.assertEqual(expected, result)

    @patch.object(TrackFoodApiViewSet, 'get_serializer')
    @patch.object(TrackFoodApiViewSet, 'get_queryset')
    @patch.object(TrackFoodApiViewSet, 'get_df')
    @patch.object(TrackFoodApiViewSet, 'compute_distance')
    def test_list(self, compute_distance, get_df,
                  get_queryset, get_serializer):
        obj = {
            "id": 1,
            "latitude": 1,
            "longitude": 1
        }
        serializer_mock = MagicMock()
        serializer_mock.data = obj
        get_serializer.return_value = serializer_mock
        get_df.return_value = pd.DataFrame([obj])
        compute_distance.return_value = 1
        mock_request = MagicMock()
        expected = obj
        result = self.instance.list(mock_request)
        self.assertEqual(expected, result.data)
