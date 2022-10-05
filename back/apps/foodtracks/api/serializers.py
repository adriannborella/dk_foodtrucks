from rest_framework import serializers
from apps.foodtracks.models import TrackFood


class TrackFoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrackFood
        fields = ['objectid', 'applicant', 'facilitytype',
                  'locationdescription', 'latitude', 'longitude',
                  'address', 'schedule', 'facilitytype']
