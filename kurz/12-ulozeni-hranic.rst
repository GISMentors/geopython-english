Krok 12 - uložení hranic
========================
Uložení hranic do formátu ESRI Shapefile

.. code:: python

    import os
    import shutil
    import ogr
    import osr

    wgs84 = osr.SpatialReference()
    wgs84.ImportFromEPSG(4326)
    shp_driver = ogr.GetDriverByName('ESRI Shapefile')

    def calculate_borders(borders_layer):
        # ...
        borders_layer_defn = borders_layer.GetLayerDefn()
        for a, geom_a in enumerate(geometries):
            for b, geom_b in enumerate(geometries):
                # ...
                wkt = shapely.wkt.dumps(common_border)
                border_feature = ogr.Feature(borders_layer_defn)
                border_feature.SetGeometry(ogr.CreateGeometryFromWkt(wkt))
                borders_layer.CreateFeature(border_feature)

    def main():
        if os.path.isdir('output'):
            shutil.rmtree('output')
        os.mkdir('output')
        # ...
        borders = shp_driver.CreateDataSource('output/borders.shp')
        borders_layer = borders.CreateLayer('layer', wgs84)
        calculate_borders(borders_layer)
        borders.Destroy()
        # ...
