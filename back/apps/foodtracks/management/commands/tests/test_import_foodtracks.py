from django.test import TestCase
from unittest.mock import Mock, patch, MagicMock
import pandas as pd
from rest_framework.response import Response
from ..import_foodtracks import Command
from apps.foodtracks.models import TrackFood


class TestImport_foodtruck(TestCase):

    def setUp(self):
        self.instance = Command()

    @patch("pandas.read_csv")
    def test_get_df(self, read_csv):
        read_csv.return_value = pd.DataFrame(
            columns=['objectid', 'applicant', 'facilitytype',
                     'locationdescription', 'latitude', 'longitude',
                     'address', 'schedule',
                     'other', 'other2'])
        expected = ['objectid', 'applicant', 'facilitytype',
                    'locationdescription', 'latitude', 'longitude',
                    'address', 'schedule', ]
        result = self.instance.get_df()
        self.assertTrue((expected == result.columns).all())

    @patch.object(TrackFood, "objects")
    @patch.object(Command, "get_df")
    def test_handle(self, get_df, objects_mock):
        objects_mock.filter = MagicMock()
        objects_mock.bulk_create = MagicMock()
        get_df.return_value = pd.DataFrame(
            columns=['objectid', 'applicant', 'facilitytype',
                     'locationdescription', 'latitude', 'longitude',
                     'address', 'schedule',
                     'other', 'other2'])

        self.instance.handle()
        self.assertTrue(objects_mock.filter.called)
        self.assertTrue(objects_mock.bulk_create.called)
