import numpy as np

def write_region_bboxes():
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

    for key, bounds in REGION_BBOX.items():
        array = np.array([[bounds[2], bounds[0]],
                          [bounds[2], bounds[1]],
                          [bounds[3], bounds[1]],
                          [bounds[3], bounds[0]],
                          [bounds[2], bounds[0]]
                         ])
        np.save(f'{key}.npy', array)

write_region_bboxes()
