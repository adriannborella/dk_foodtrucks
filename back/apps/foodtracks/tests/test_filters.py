from django.test import TestCase
from apps.foodtracks.models import TrackFood
from apps.foodtracks.filters import ImportedRecordFilter
from apps.foodtracks.admin import TrackFoodAdmin
from unittest.mock import MagicMock


class TestViewSet(TestCase):

    def setUp(self):
        self.Model = TrackFood
        self.ModelAdmin = TrackFoodAdmin
        self.FilterType = ImportedRecordFilter

    def get_instance(self, request):
        return self.FilterType(None, request, self.Model, self.ModelAdmin)

    def execute_quetyset(self, request):
        queryset_mock = MagicMock()
        queryset_mock.filter = MagicMock()
        self.instance = self.get_instance(request)
        self.instance.queryset(request, queryset_mock)
        return queryset_mock

    def test_queryset_yes(self):
        expected = {'objectid__isnull': False}
        request = {'was_imported': 'Yes'}
        result = self.execute_quetyset(request)
        self.assertEqual(
            expected,
            result.filter.call_args_list[0].kwargs)

    def test_queryset_no(self):
        expected = {'objectid__isnull': True}
        request = {'was_imported': 'No'}
        result = self.execute_quetyset(request)
        self.assertEqual(
            expected,
            result.filter.call_args_list[0].kwargs)
