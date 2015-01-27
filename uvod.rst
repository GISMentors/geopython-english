Úvod
====

**Python** je populární programovací jazyk, který má své četné příznivce stejně
jako zarputilé odpůrce. Oproti jiným běžně rozšířeným jazykům je jeho syntaxe
zvláštní mimo jiné v tom, že nepoužívá závorky - bloky kódu jsou odděleny
navzájem odsazením zdrojového textu.

.. note:: **Příklad funkce main() v jazyku Python**

   .. code:: bash

      def main():
          print "ahoj"

Ve světe geoinformačních technologií je Python velice oblíbený (a
můžeme říci, že čím dál oblíbenější). Stojí rozkročen mezi jednoduchým
skriptováním v shellu a pokročilým programováním na takřka systémové
úrovni v~jazyce :wikipedia:`C <C (programovací jazyk)>`. Má v sobě
něco i z přístupů jazyka :wikipedia:`Java <Java (programovací
jazyk)>`. Většina existujících knihoven a programů má pro tento jazyk
svoje rozhraní, jako příklad můžeme uvést `GDAL Python API
<http://gdal.org/python/>`_.

S Pythonem lze ve světě GIS dojít daleko, níže uvádíme malý přehled
vybraných nástrojů a jejich napojení na jazyk Python:

**Desktop**
    * *GRASS GIS*: http://grass.osgeo.org
    * *QGIS*: http://qgis.org
    * *ArcGIS*: http://www.arcgis.com

**Web**
    * *MapServer*: http://mapserver.org
    * *GeoServer*: http://geoserver.org
    * *TileCache*: http://tilecache.org
    * *PyWPS*: http://pywps.wald.intevation.org
    * *GeoDjango*: http://geodjango.org

**Knihovny a nástroje**
    * *GDAL*: http://gdal.org
    * *Fiona*: http://toblerity.org/fiona/manual.html
    * *Rasterio*: https://github.com/mapbox/rasterio
    * *PyProj*: https://github.com/jswhit/pyproj
    * *R (rpy2)*: http://rpy.sourceforge.net
    * *Shapely*: http://toblerity.org/shapely/manual.html

**Databáze**
    * *PostGIS*: http://postgis.net
    * *SpatiaLite*: https://www.gaia-gis.it/fossil/libspatialite/index
    * *GeoAlchemy*: http://geoalchemy.org

**Specializované nástroje**
    * *TopoJSON*: https://github.com/calvinmetcalf/topojson.py
    * *RTree index*: https://github.com/Toblerity/rtree

Seznam samozřejmě není úplný či konečný.

V tomto kurzu se zaměříme na úvod do práce s knihovnou :doc:`GDAL
<rasters/gdal>` a jejími nadstavbami :doc:`Rasterio
<rasters/rasterio>` a :doc:`Fiona <vectors/fiona/index>`. Vyzkoušíme si na
práci s knihovnou pro webové služby OGC :doc:`OWSLib <owslib/index>` a
nakonec se podíváme na serverové aplikace pomocí rozhraní
:doc:`python-mapscript <mapscript/index>`.

Cílem kurzu přirozeně není kompletní pokrytí problematiky GIS a jazyka Python.
Cílem je poskytnout přehled o nejčastěji používaných základních nástrojích, nad
kterými lze stavět další aplikace. Tyto nástroje jsou ve své většině používány i
dalšími programy a knihovnami a proto je dobré o nich vědět a chápat jejich
principy.
    
