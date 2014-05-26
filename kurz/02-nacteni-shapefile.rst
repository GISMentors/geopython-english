Krok 2 - načtení polygonů obcí
==============================
Načtení souboru ve formátu ``ESRI Shapefile``. Doporučujeme používat oddělené
funkce pro pozdější větší přehlednost kódu.

.. code:: python

    from osgeo import ogr

    def calculate_hikers(cities_layer):
        for i in range(cities_layer.GetFeatureCount()):
            city = cities_layer.GetFeature(i)
            city_geom = city.GetGeometryRef()
            city_centroid = city_geom.Centroid()
            print city.GetField('uat_name_n'), city_centroid

    def main():
        cities = ogr.Open('input/ro_cities.shp')
        cities_layer = cities.GetLayer(0)
        calculate_hikers(cities_layer)
        cities.Destroy()
