Krok 7 - Počet výletníků
========================
Spočítáme počet výletníků v každém městě, kteří dorazí do každého parku. Celkový
počet výletníků je pro každé město fixní a je vydělen počtem blízkých parků.

.. code:: python

    def calculate_hikers(cities_layer, population, parks_data):
        hiker_fraction = 0.01  # 1%
        # ...
        for i in range(cities_layer.GetFeatureCount()):
            city = cities_layer.GetFeature(i)
            # ...
            nearby_parks = []
            for park in parks_data:
                # ...
                if distance < max_distance:
                    nearby_parks.append(park)

            if nearby_parks:  # do people have a park nearby?
                hiker_population = city_population * hiker_fraction
                people_per_park = int(hiker_population / len(nearby_parks))
                for park in nearby_parks:
                    park_centroid = park['centroid']
                    print city_centroid, "->", park_centroid, people_per_park
