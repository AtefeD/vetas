import cartopy.crs
import csep
import numpy as np
from sklearn.metrics import v_measure_score


def get_region(name='Iceland', dh=0.05, dv=0.05, magnitudes=np.arange(3.0, 7.0, 0.1)):
    """
    Return (lon_min, lon_max, lat_min, lat_max) for a given region suffix.

    Regions supported (exact match or substring search):
      - "TFZ"   → Tjörnes Fracture Zone
      - "SW", "SISZ", "RPOR" → South‐West Iceland (SISZ–RPOR)
      - otherwise → full Iceland
    """
    REGION_BBOX = {
        "TFZ": (-20.3, -16.0, 65.5, 67.2),
        "SW": (-23.0, -19.5, 63.7, 64.4),
        "SISZ": (-21.0, -19.5, 63.7, 64.4),  #
        "RPOR": (-23.0, -21.0, 63.7, 64.3),  #
        "Iceland": (-24.7, -13.5, 63.3, 67.2)}

    bounds = REGION_BBOX.get(name)
    h_disc = np.arange(bounds[0], bounds[1], dh)
    v_disc = np.arange(bounds[2], bounds[3], dh)
    x, y = np.meshgrid(h_disc, v_disc)
    origins = np.vstack((x.ravel(), y.ravel())).T
    print(origins)
    region = csep.regions.CartesianGrid2D.from_origins(origins, dh=dh, magnitudes=magnitudes)
    return region

region = get_region('Iceland')
forecast = csep.load_catalog_forecast('etas_2016-01-28_2016-02-24.csv', filter_spatial=True, region=region)
# forecast.filter_spatial(region)
forecast.plot(show=True, plot_args={'projection': cartopy.crs.epsg(3057)})

