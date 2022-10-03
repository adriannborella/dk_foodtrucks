from django.test import TestCase
from unittest.mock import Mock, patch, MagicMock
from .views import TrackFoodApiViewSet
import pandas as pd
from rest_framework.response import Response


class TestViewSet(TestCase):

    def setUp(self):
        self.instance = TrackFoodApiViewSet()

    def test_compute_distance(self):
        expected = 2.105245944503833
        result = self.instance.compute_distance(
            (37.791303, -122.398956),
            37.7639891554711,
            -122.41612672805788)
        self.assertEqual(expected, result)

    @patch("pandas.read_csv")
    def test_get_df(self, read_csv):
        read_csv.return_value = pd.DataFrame(
            columns=['objectid', 'applicant', 'facilitytype',
                     'locationdescription', 'latitude', 'longitude',
                     'other', 'other2'])
        expected = ['objectid', 'applicant', 'facilitytype',
                    'locationdescription', 'latitude', 'longitude']
        result = self.instance.get_df()
        self.assertTrue((expected == result.columns).all())

    @patch.object(TrackFoodApiViewSet, 'get_df')
    @patch.object(TrackFoodApiViewSet, 'compute_distance')
    def test_list(self, compute_distance, get_df):
        obj = {
            'objectid': 100,
            'applicant': 'test',
            'facilitytype': 'Truck',
            'locationdescription': 'Description',
            'latitude': 11,
            'longitude': 12
        }
        get_df.return_value = pd.DataFrame([obj])
        compute_distance.return_value = 1
        mock_request = MagicMock()
        expected = 100
        result = self.instance.list(mock_request)
        self.assertEqual(expected, result.data[0]["objectid"])
