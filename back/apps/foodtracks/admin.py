from django.contrib import admin
from apps.foodtracks.models import TrackFood
from apps.foodtracks.filters import ImportedRecordFilter


@admin.register(TrackFood)
class TrackFoodAdmin(admin.ModelAdmin):
    ordering = ("applicant", "locationdescription", "address")
    search_fields = ("applicant", "locationdescription")
    list_display = ("applicant", "locationdescription", "address")
    list_filter = ("facilitytype", ImportedRecordFilter)
    icon_name = 'edit_location'
    fields = (
        ("applicant", "address"),
        ("locationdescription", "facilitytype"),
        ("latitude", "longitude"),
        "schedule"
    )
