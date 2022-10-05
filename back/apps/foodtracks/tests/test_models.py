from django.test import TestCase
from apps.foodtracks.models import TrackFood


class TestTrackFoodModel(TestCase):

    def test_str(self):
        expected = "Applicant"
        instance = TrackFood(applicant=expected)
        self.assertEqual(expected, instance.__str__())
