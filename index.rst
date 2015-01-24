GeoPython
=========

Motivace
--------
* Python je dnes asi nejvíce geo-pozitivní programovací jazyk
* Python baví
* Množstí knihoven a nástrojů (GDAL, PROJ4, Shapely, Fiona, RasterIO, MapServer,
  gsconfig, OWSLib, PyWPS, pycsw, ...)
* Podpora v deskopech (GRASS GIS, ArcGIS, QGIS, ...) 
* Python se neučí, Python se píše

Pracovní prostředí 
------------------
* OSGeo Live:
  http://live.osgeo.org/en/index.html
* Data archive:
  https://github.com/GISMentors/dataset
* Jednotlivé kroky
  https://github.com/gismentors/pygis/tree/master/kurz

* Nastavení
    
    sudo apt-get install gedit gedit-plugins
    cd ~/Desktop

* Stažení dat RUIAN
  http://46.28.111.140/gismentors/skoleni/geodata/ruian/


Další čtení
-----------

Python
""""""

* Učebnice jazyka Python (česky): http://www.root.cz/knihy/ucebnice-jazyka-python/
* Python guide: http://docs.python-guide.org/en/latest/
* Resources for learning Python:
  http://docs.python-guide.org/en/latest/intro/learning.html


GeoPython
"""""""""

* **Python GDAL/OGR Cookbook** http://pcjericks.github.io/py-gdalogr-cookbook/
* Shapely manual: http://toblerity.github.io/shapely/manual.html
* PostGIS: http://postgis.net/
* GDAL: http://www.gdal.org/
* "Python Geospatial Development" book, Erik Westra:
  http://www.packtpub.com/python-geospatial-development/book
  (2nd edition just out)


Fóra, dokumentace
"""""""""""""""""

* The GIS Stack Exchange: http://gis.stackexchange.com/ (http://gis.stackexchange.com/?tags=python)
* Last but not least, https://www.google.com/


Obsah
-----

.. toctree::
   :maxdepth: 2

   uvod
   owslib/index
   vectors/index
   pyproj/index
   rasters/index
   mapscript/index
