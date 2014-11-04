# -*- coding: utf-8 -*-
from osgeo import ogr
import csv
import osr
import pyproj
import os
import shutil
import argparse

MAX_LAZINESS_DISTANCE = 50000  # 50 Km
HIKER_FRACTION = 0.01  # 1%

jtsk = osr.SpatialReference()
jtsk.ImportFromEPSG(5514)
wgs84 = osr.SpatialReference()
wgs84.ImportFromEPSG(4326)
wgs84_to_jtsk = osr.CoordinateTransformation(wgs84, jtsk)
geod = pyproj.Geod(ellps='WGS84')
shp_driver = ogr.GetDriverByName('ESRI Shapefile')

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


def load_population_data():
    population = {}
    with open('obyvatelstvo.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            population[row['okres']] = int(row['obyvatel'])
    return population


def calculate_hikers(cities_layer, max_distance, hikers_fraction,
                     flux_layer, population, forest_data):

    flux_layer_defn = flux_layer.GetLayerDefn()

    for i in range(cities_layer.GetFeatureCount()):
        city = cities_layer.GetNextFeature()
        city_name = city.GetField('nazev')
        city_geom = city.GetGeometryRef()
        city_centroid = city_geom.Centroid()


        nearby_forests = []
        try:
            city_population = population[city_name]
        except:
            city_population = None
        for forest in forest_data:
            forest_centroid = forest['centroid']
            (angle1, angle2, distance) = geod.inv(
                city_centroid.GetX(), city_centroid.GetY(),
                forest_centroid.GetX(), forest_centroid.GetY())
            if distance < max_distance:
                nearby_forests.append(forest)

        if nearby_forests:
            hiker_population = city_population * hikers_fraction if city_population else 0
            people_per_forest = int(hiker_population / len(nearby_forests))
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

    parser = argparse.ArgumentParser(description='Find distances form cities to forests')
    parser.add_argument('--max_distance', dest='distance',
                default=MAX_LAZINESS_DISTANCE,
                help='Maximum distance to forest')
    parser.add_argument('--hikers', dest='hikers',
                default=HIKER_FRACTION,
                help='Hikers ratio in population')

    args = parser.parse_args()

    natural = ogr.Open('natural.shp')
    natural_layer = natural.GetLayer(0)
    natural_data = load_natural_data(natural_layer)

    population = load_population_data()
    ruian = ogr.Open('ruian_cr.gpkg')
    cities_layer = ruian.GetLayer(16)

    if os.path.isdir('output'):
        shutil.rmtree('output')
    os.mkdir('output')

    flux = shp_driver.CreateDataSource('output/flux.shp')
    flux_layer = flux.CreateLayer('layer', wgs84)
    flux_layer.CreateField(ogr.FieldDefn('people', ogr.OFTInteger))

    calculate_hikers(cities_layer, args.distance,
                     args.hikers,
                     flux_layer, population, natural_data)

    flux.Destroy()
    ruian.Destroy()



if __name__ == '__main__':
    main()
