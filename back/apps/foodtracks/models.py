from django.db import models

CHOISES_FACILITY_TYPE = (
    ("Truck", "Truck"),
    ("Push Cart", "Push Cart")
)


class TrackFood(models.Model):
    applicant = models.fields.CharField("Applicant", max_length=100)
    locationdescription = models.fields.CharField(
        "Description", max_length=150)
    address = models.fields.CharField("Address", max_length=250)
    # TODO: Agregar validación por maximo y minimo
    latitude = models.fields.FloatField("Latitude")
    longitude = models.fields.FloatField("Longitude")
    facilitytype = models.fields.CharField(
        "Facility Type", choices=CHOISES_FACILITY_TYPE, max_length=100)
    objectid = models.fields.IntegerField("Objectid", null=True)
    schedule = models.fields.TextField("Link Schedule")

    class Meta:
        verbose_name = 'FoodTruck'
        verbose_name_plural = 'FoodTrucks'

    def __str__(self) -> str:
        return self.applicant
