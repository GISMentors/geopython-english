Krok 13 - Počet výletníků na park
=================================
Uložíme počet výletníků kteří se dostanou do každého parku. defaultdict_ je
vylepšená struktura `dict`, která vrací výchozí hodnotu, pokud hodnota pod
požadovaným klíčem není definována. V našem případ se prostě vrátí hodnota
``int()``, což je ``0``.

.. _defaultdict: http://docs.python.org/2/library/collections.html#collections.defaultdict

.. code:: python

    from collections import defaultdict

    def calculate_hikers(...):
        hikers = defaultdict(int)
        for i in range(cities_layer.GetFeatureCount()):
            # ...
            if nearby_parks:  # do people have a park nearby?
                # ...
                for park in nearby_parks:
                    # ...
                    hikers[park['name']] += people_per_park

        return dict(hikers)

    def main():
        # ...
        hikers = calculate_hikers(...)
        print hikers
        # ...
