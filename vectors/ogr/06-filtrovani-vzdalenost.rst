Krok 6 - Filtrování pomocí vzdálenosti
======================================
Vypočítat geodetickou vzdálenost a vytisknout pouze blízké parky

.. code:: python

    import pyproj
    geod = pyproj.Geod(ellps='WGS84')

    MAX_LAZINESS_DISTANCE = 50000  # 50 Km


    def calculate_hikers(cities_layer, population, parks_data):

        for i in range(cities_layer.GetFeatureCount()):
            # ...
            city_centroid = city_geom.Centroid()
            city_centroid.Transform(stereo70_to_wgs84)
            for park in parks_data:
                park_centroid = park['centroid']
                (angle1, angle2, distance) = geod.inv(
                    city_centroid.GetX(), city_centroid.GetY(),
                    park_centroid.GetX(), park_centroid.GetY())
                if distance < MAX_LAZINESS_DISTANCE:
                    print '->', park['name'], distance
