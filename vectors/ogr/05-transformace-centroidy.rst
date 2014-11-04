Krok 5 - souřadnicová transformace a centroidy
==============================================
Stáhneme data České republiky z projektu OpenStreetMap ve formátu
`ESRI
Shapefile<http://download.geofabrik.de/openstreetmap/europe/czech-republic-latest.shp.zip>`_
a rozbalíme.
    
.. code-block:: bash

    wget http://download.geofabrik.de/openstreetmap/europe/czech-republic-latest.shp.zip
    unzip czech-republic-latest.shp.zip

Vypočítáme a uložíme centroidy parků v paměti. Parky jsou uloženy v
souř. systému `WGS84`, aka `EPSG:4326`. 
Proto musíme tato vstupní data transformovat do systému `S-JTSK` aka `EPSG:5514`.

.. _`EPSG:4326`: http://epsg.io/4326
.. _`EPSG:5514`: http://epsg.io/5514

.. code:: python

    import osr

    jtsk = osr.SpatialReference()
    jtsk.ImportFromEPSG(5514)
    wgs84 = osr.SpatialReference()
    wgs84.ImportFromEPSG(4326)
    wgs84_to_jtsk = osr.CoordinateTransformation(wgs84, jtsk)

    def load_natural_data(natural_layer):
        forest_data = []
        for i in range(natural_layer.GetFeatureCount()):
            natural = natural_layer.GetNextFeature()
            land_type = natural.GetField('type')
            if land_type == 'forest':
                forest_centroid = natural.GetGeometryRef().Centroid()
                forest_centroid.Transform(wgs84_to_jtsk)
                forest_data.append({
                'centroid': forest_centroid,
                'name': natural.GetField('name'),
            })
        return forest_data

    def main():
        # ...
        natural = ogr.Open('natural.shp')
        natural_layer = natural.GetLayer(0)
        natural_data = load_natural_data(natural_layer)
        # ...

