Krok 8 - Uložení cesty do parku
===============================
Uložíme cestu, kterou musí urazit výletník do formátu ESRI Shapefile. Některá
města nemají blízké parky, musíme předejít potenciálnímu dělení nulou.

.. code:: python

    import os
    import shutil
    shp_driver = ogr.GetDriverByName('ESRI Shapefile')

    def calculate_hikers(cities_layer, flux_layer, population, parks_data):
        flux_layer_defn = flux_layer.GetLayerDefn()
        # ...
        for i in range(cities_layer.GetFeatureCount()):
            # ...
            if nearby_parks:  # do people have a park nearby?
                # ...
                for park in nearby_parks:
                    park_centroid = park['centroid']
                    line_feature = ogr.Feature(flux_layer_defn)
                    line_feature.SetField('people', people_per_park)
                    line = ogr.Geometry(ogr.wkbLineString)
                    line.AddPoint(city_centroid.GetX(), city_centroid.GetY())
                    line.AddPoint(park_centroid.GetX(), park_centroid.GetY())
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
        calculate_hikers(cities_layer, flux_layer, population, parks_data)
        flux.Destroy()
