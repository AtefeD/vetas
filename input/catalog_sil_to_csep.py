import numpy as np
import pandas
import datetime

sil_catalog_path = './SILcat_csep_Iceland.csv'
sil_cat = pandas.read_csv(sil_catalog_path)



csep_catalog = pandas.DataFrame(
    data={
        'lon': sil_cat['lon'],
        'lat': sil_cat['lat'],
        'mag': sil_cat['Ml'],
        'time_string': pandas.to_datetime(sil_cat['datetime']),
        'depth': sil_cat['depth'],
        'catalog_id': np.ones(len(sil_cat), dtype=int),
        'event_id': np.arange(len(sil_cat))
    })

csep_catalog.to_csv('catalog.csv',
                    index=False,
                    date_format='%Y-%m-%dT%H:%M:%S'
                    )
