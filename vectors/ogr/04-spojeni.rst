Krok 4 - Spojení dat populace a měst
====================================
Spojením dat měst a populace vytvoříme slovníkovou strukturu

.. code:: python

    ...
    def calculate_hikers(cities_layer, population):
        for i in range(cities_layer.GetFeatureCount()):
            city = cities_layer.GetNextFeature()
            city_name = city.GetField('nazev')
            city_geom = city.GetGeometryRef()
            city_centroid = city_geom.Centroid()
            try:
                city_population = population[city_name]
            except:
                city_population = None
            print city_name, city_population, city_centroid
    ...
