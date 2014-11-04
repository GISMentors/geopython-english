Krok 7 - Počet výletníků
========================
Spočítáme počet výletníků v každé obci, kteří dorazí do každého lesa. Celkový
počet výletníků je pro každou obec fixní a je vydělen počtem blízkých lesů.

.. code:: python

    HIKER_FRACTION = 0.01  # 1%


    def calculate_hikers(cities_layer, population, forest_data):
        # ...
        for i in range(cities_layer.GetFeatureCount()):
            city = cities_layer.GetFeature(i)
            # ...
            nearby_forests = []
            for forest in forest_data:
                # ...
                if distance < max_distance:
                    nearby_forests.append(forest)

            if nearby_forests:  # do people have a forest nearby?
                hiker_population = city_population * HIKER_FRACTION if city_population else 0
                people_per_forest = int(hiker_population / len(nearby_forests))
                for forest in nearby_forests:
                    forest_centroid = forest['centroid']
                    print city_centroid, "->", forest_centroid, people_per_forest
