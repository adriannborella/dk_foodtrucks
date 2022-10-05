from apps.foodtracks.models import TrackFood
from django.core.management.base import BaseCommand
import pandas as pd
import numpy as np
import logging
logger = logging.getLogger("django")


class Command(BaseCommand):
    help = 'Test connections to diferent systems'

    def get_df(self):
        url = f"https://data.sfgov.org/resource/rqzj-sfat.csv"
        df = pd.read_csv(url)
        clean_df = df[['objectid', 'applicant', 'facilitytype',
                       'locationdescription', 'latitude', 'longitude',
                       'address', 'schedule']]
        clean_df = clean_df.replace(0, np.nan)
        clean_df = clean_df.dropna()
        return clean_df

    def handle(self, *args, **options):
        # Elimina los registros importados, dejando los cargados por el usuario
        TrackFood.objects.filter(objectid__isnull=False).delete()
        df = self.get_df()
        dictionary = df.to_dict('records')
        to_save = [TrackFood(**record) for record in dictionary]
        TrackFood.objects.bulk_create(to_save)
