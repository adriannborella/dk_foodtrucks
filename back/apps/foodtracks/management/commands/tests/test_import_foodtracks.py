from django.test import TestCase
from unittest.mock import Mock, patch, MagicMock
from apps.foodtracks.api.views import TrackFoodApiViewSet
import pandas as pd
from rest_framework.response import Response


class TestImport_foodtruck(TestCase):

    def test_get_df(self):
        pass
