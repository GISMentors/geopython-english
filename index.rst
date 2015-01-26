Motivace
========

* Python baví
* Python se neučí, Python se píše
* :wikipedia:`Python` je dnes asi nejvíce "geopozitivní" programovací jazyk
    
  * Množství knihoven a nástrojů (`GDAL <http://gdal.org>`_, `PROJ4
    <http://trac.osgeo.org/proj/>`_, `Shapely
    <https://pypi.python.org/pypi/Shapely>`_, `Fiona
    <https://pypi.python.org/pypi/Fiona>`_, `RasterIO
    <https://pypi.python.org/pypi/rasterio>`_, `MapServer Python
    MapScript <http://mapserver.org/mapscript/python.html>`_, `GeoServer
    gsconfig <https://pypi.python.org/pypi/gsconfig>`_, `OWSLib
    <http://geopython.github.io/OWSLib/>`_, `PyWPS
    <http://pywps.wald.intevation.org/>`_, `pycsw <http://pycsw.org/>`_,
    ...)
  * Podpora v deskopech (GRASS GIS - `PyGRASS
    <http://grass.osgeo.org/grass71/manuals/libpython/pygrass_index.html>`_,
    Esri ArcGIS - `arcpy
    <http://resources.arcgis.com/en/help/main/10.1/index.html#//000v000000v7000000>`_,
    QGIS - `PyQGIS
    <http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/plugins.html>`_,
    ...)

Pracovní prostředí
==================

* OSGeo Live:
  http://live.osgeo.org/en/index.html
* Nastavení

  .. code:: bash

            sudo apt-get install gedit gedit-plugins
            cd ~/Desktop

* Geodata:
    
  * Datové sady:
    https://github.com/GISMentors/dataset
  * Předpřipravené data RÚIAN:
    http://training.gismentors.eu/geodata/ruian/

Obsah
=====

.. toctree::
   :maxdepth: 2

   uvod
   owslib/index
   vectors/index
   pyproj/index
   rasters/index
   mapscript/index

Další čtení
===========

Python
------

* Učebnice jazyka Python (česky): http://www.root.cz/knihy/ucebnice-jazyka-python
* Python guide: http://docs.python-guide.org/en/latest
* Dive into Python: http://www.diveintopython.net


GeoPython
---------

* **Python GDAL/OGR Cookbook**: http://pcjericks.github.io/py-gdalogr-cookbook/
* Shapely manual: http://toblerity.github.io/shapely/manual.html
* "Python Geospatial Development" book, Erik Westra:
  http://www.packtpub.com/python-geospatial-development/book

Fóra, dokumentace
-----------------

* The GIS Stack Exchange: http://gis.stackexchange.com/ (http://gis.stackexchange.com/?tags=python)
* Last but not least, https://www.google.com

Licence dokumentu
=================

Text školení je licencován pod `Creative Commons Attribution-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-sa/4.0/>`_.

.. figure:: images/cc-by-sa.png 
   :width: 110px
   :scale-latex: 100
              
*Verze textu školení:* |release| (|today|)

Autoři
------

Za `GISMentors <http://www.gismentors.eu/>`_:

* Jáchym Čepický ``<jachym.cepicky opengeolabs.cz>``
* Martin Landa ``<martin.landa opengeolabs.cz>``
    
.. only:: latex

   Online HTML verze textu školení je dostupná na adrese: http://training.gismentors.eu/geopython/

Zdrojové texty školení jsou dostupné na adrese: https://github.com/GISMentors/geopython

