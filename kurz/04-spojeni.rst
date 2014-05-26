Krok 4 - Spojení dat populace a měst
====================================
Spojením dat měst a populace vytvoříme slovníkovou strukturu

.. code:: python

    def calculate_hikers(cities_layer, population):
        for i in range(cities_layer.GetFeatureCount()):
            # ...
            city_code = city.GetField('siruta')
            city_population = population[city_code]
            # ...
            print city.GetField('uat_name_n'), city_population, city_centroid
