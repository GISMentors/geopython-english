Krok 11 - Průnik za použití shapely
===================================
Průnik polygonů pomocí knihovny Shapely. Data načteme a uložíme pomocí formátu
WKT.

.. code:: python

    import shapely.wkt

    def calculate_borders():
        # ...
        geometries = []
        for row in cursor:
            geom = shapely.wkt.loads(row[1])
            geometries.append(geom)

        for a, geom_a in enumerate(geometries):
            for b, geom_b in enumerate(geometries):
                if b <= a:
                    continue  # don't compare polygons twice
                common_border = geom_a.intersection(geom_b)
                if common_border.is_empty:
                    continue
                wkt = shapely.wkt.dumps(common_border)
                print wkt
