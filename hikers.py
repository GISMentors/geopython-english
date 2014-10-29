# -*- coding: utf-8 -*-
from osgeo import ogr
import csv
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


def load_population_data():
    population = {}
    with open('obyvatelstvo.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            population[row['okres']] = int(row['obyvatel'])
    return population


def calculate_hikers(cities_layer, population):
    for i in range(cities_layer.GetFeatureCount()):
        city = cities_layer.GetNextFeature()
        city_name = city.GetField('nazev')
        city_geom = city.GetGeometryRef()
        city_centroid = city_geom.Centroid()
        try:
            city_population = population[city_name]
        except:
            city_population = None
        #print city_name, city_population, city_centroid

def main():
    population = load_population_data()
    ruian = ogr.Open('vfr-uksg-2014-10.gpkg')
    cities_layer = ruian.GetLayer(16)
    calculate_hikers(cities_layer, population)
    ruian.Destroy()

    natural = ogr.Open('natural.shp')
    natural_layer = natural.GetLayer(0)
    natural_data = load_natural_data(natural_layer)





if __name__ == '__main__':
    main()
