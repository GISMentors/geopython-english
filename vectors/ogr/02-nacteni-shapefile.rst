Krok 2 - načtení polygonů obcí
==============================
Načtení souboru ve formátu ``OGC GeoPackage``. GeoPackage je souborový formát,
který má potenciál nahradit dosud populární ``ESRI Shapefile``. Vzhledem k tomu,
že na pozadí běží knihovna OGR, je postup otevírání vektorých dat pro všechny
datové formáty stejný.

Doporučujeme používat oddělené funkce pro pozdější větší přehlednost kódu.

.. code:: python

    from osgeo import ogr

    def calculate_hikers(cities_layer):
        for i in range(cities_layer.GetFeatureCount()):
            city = cities_layer.GetNextFeature()
            city_geom = city.GetGeometryRef()
            city_centroid = city_geom.Centroid()
            print city.GetField('nazev'), city_centroid

    def main():
        ruian = ogr.Open('ruian_cr.gpkg')
        cities_layer = ruian.GetLayer(16)
        calculate_hikers(cities_layer)
        ruian.Destroy()
