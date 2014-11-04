Krok 8 - Uložení cesty do forestu
=================================
Uložíme cestu, kterou musí urazit výletník ze středu své obce do nejbližšího lesa.
Cestu uložíme do nového souboru ESRI Shapefile. Některé obce
města nemají blízké lesy, musíme proto předejít potenciálnímu dělení nulou.

.. code:: python

    import os
    import shutil
    shp_driver = ogr.GetDriverByName('ESRI Shapefile')

    def calculate_hikers(cities_layer, flux_layer, population, forests_data):
        flux_layer_defn = flux_layer.GetLayerDefn()
        # ...
        for i in range(cities_layer.GetFeatureCount()):
            # ...
            if nearby_forests:  # do people have a forest nearby?
                # ...
                for forest in nearby_forests:
                    forest_centroid = forest['centroid']

                    # create linestring feature
                    line_feature = ogr.Feature(flux_layer_defn)
                    line_feature.SetField('people', people_per_forest)
                    line = ogr.Geometry(ogr.wkbLineString)
                    line.AddPoint(city_centroid.GetX(), city_centroid.GetY())
                    line.AddPoint(forest_centroid.GetX(), forest_centroid.GetY())
                    line_feature.SetGeometry(line)
                    flux_layer.CreateFeature(line_feature)

    def main():
        # ...

        if os.path.isdir('output'):
            shutil.rmtree('output')
        os.mkdir('output')

        flux = shp_driver.CreateDataSource('output/flux.shp')
        flux_layer = flux.CreateLayer('layer', wgs84)
        flux_layer.CreateField(ogr.FieldDefn('people', ogr.OFTInteger))
        calculate_hikers(cities_layer, flux_layer, population, natural_data)
        flux.Destroy()
