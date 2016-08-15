##################
GeoPython workshop
##################

Welcome to GeoPython workshop. This workshop should give you brief
overview about how to use Python when working with geospatial data.

.. only:: html

   `GISMentors <http://gismentors.cz>`_ | Workshop `GRASS GIS
   <http://gismentors.cz/skoleni/grass-gis>`_ | `QGIS
   <http://gismentors.cz/skoleni/qgis>`_ | `PostGIS
   <http://gismentors.cz/skoleni/postgis>`_ | `GeoPython
   <http://gismentors.cz/skoleni/geopython>`_

   **********
   Motivation
   **********

.. figure:: images/python-logo.png
   :class: small
        
* `Python <http://python.org>`_ is fun
* You do not "learn it", you "simply write it".
* Python is the most "geopositive" programming language today.
* There is a lot of tools out there (`GDAL <http://gdal.org>`_, `PROJ4
  <http://trac.osgeo.org/proj/>`_, `Shapely
  <http://toblerity.org/shapely/manual.html>`_, `Fiona
  <http://toblerity.org/fiona/manual.html>`_, `Rasterio
  <https://github.com/mapbox/rasterio>`_, `MapServer Python
  MapScript <http://mapserver.org/mapscript/python.html>`_, `GeoServer
  gsconfig <https://pypi.python.org/pypi/gsconfig>`_, `OWSLib
  <http://geopython.github.io/OWSLib/>`_, `PyWPS
  <http://pywps.wald.intevation.org/>`_, `pycsw <http://pycsw.org/>`_,
  ...)
* You can use it on desktops too (GRASS GIS - `PyGRASS <http://grass.osgeo.org/grass71/manuals/libpython/pygrass_index.html>`_, Esri ArcGIS - `arcpy <http://resources.arcgis.com/en/help/main/10.1/index.html#//000v000000v7000000>`_, QGIS - `PyQGIS <http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/plugins.html>`_,
...)
* Community - `GeoPythonConference <http://geopython.org>`_, `GeoPython on GitHub <http://geopython.github.io>`_

OSGeo-Live
----------

If you are using `OSGeo-live <https://live.osgeo.org>`__ DVD, you should
be fine. If something is missing, ``pip install package_name`` should
fix it

Custom environment
------------------

We advice you to work in `Virtual
environment <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`__.

Further reading
---------------

Online books
~~~~~~~~~~~~

-  Python GDAL/OGR Cookbook:
   http://pcjericks.github.io/py-gdalogr-cookbook/
-  Shapely manual: http://toblerity.github.io/shapely/manual.html
-  "Python Geospatial Development" book, Erik Westra:
   http://www.packtpub.com/python-geospatial-development/book
-  ...

Forums and documentation
~~~~~~~~~~~~~~~~~~~~~~~~

* The GIS Stack Exchange: http://gis.stackexchange.com/?tags=python
* Last but not least, https://www.google.com

============
Introduction
============
`Python <http://python.org>`_ is very popular programing language,
which has it's supporters and haters. It's syntax is (if compared to
other languages) specific. Among others, this is caused by the fact, that no
brackets are used - code blocks are separated by indentation.

Example of Python program with one function `main`:

.. code:: python

    # main function example

    def main(name):
        """Function doc string

        This function will print given name
        """

        print ("Hallo, %s!" % name)

    main('world')

.. .. note:: `Original workshop <http://training.gismentors.eu/geopython>`_ was prepared in
..         czech language on czech dataset. In Czech republic, EPSG:5514 coordinate
..         system is used, which is not supported directly Proj4 library. Please
..         adjust the ``/usr/share/proj/epsg`` file and add::
.. 
..             # Krovak S-JTSK
..             <5514> +proj=krovak +lat_0=49.5 +lon_0=24.83333333333333 +alpha=30.28813972222222 +k=0.9999 +x_0=0 +y_0=0 +ellps=bessel +pm=greenwich +units=m +no_defs +towgs84=570.8,85.7,462.8,4.998,1.587,5.261,3.56
.. 
..         line to the file

In the world of geomatics is Python very popular (and we can say, that
it's popularity is growing). It's standing between simple scripting
using SHELL commands and more advanced coding on the system level in e.g.
C. It can also be compared in some ways to Java platform. Most of the
existing libraries and programs do have their API suitable for Python,
like `GDAL Python API <http://gdal.org/python/>`_.

You can go pretty far with Python in today's world, we give you just
short overview about the tools available for you by today:

Desktop
-------

-  GRASS GIS: http://grass.osgeo.org
-  QGIS: http://qgis.org
-  ArcGIS: http://www.arcgis.com

Web
---

-  MapServer: http://mapserver.org
-  GeoServer: http://geoserver.org
-  TileCache: http://tilecache.org
-  PyWPS: http://pywps.wald.intevation.org
-  GeoDjango: http://geodjango.org

Tools and libraries
-------------------

-  GDAL: http://gdal.org
-  Fiona: http://toblerity.org/fiona
-  Rasterio: https://github.com/mapbox/rasterio
-  PyProj: https://github.com/jswhit/pyproj
-  R (rpy2): http://rpy.sourceforge.net
-  Shapely: http://toblerity.org/shapely

Databases
---------

-  PostGIS: http://postgis.net
-  SpatiaLite: https://www.gaia-gis.it/fossil/libspatialite/index
-  GeoAlchemy: http://geoalchemy.org
-  TopoJSON: https://github.com/calvinmetcalf/topojson.py
-  RTree index: https://github.com/Toblerity/rtree

The list is not complete by far of course.

In the workshop, we will focus on the introduction to GDAL library and
it's superstructures Rasterio and Fiona. We will have a look at OGC OWS
services and how to interact with them with help of the OWSLib library
and hopefully in the future, python-mapscript will be described too.

The scope of the workshop is not complete coverage of GIS and Python
topic. We would like to give you just and overview about the tools out
there, on which more complex applications can be build. This tools are
usually used in more up-level programs, so it is good if you have idea
about how they work and their principles.

Table of content
----------------

.. toctree::
   :maxdepth: 2

   vectors/index
   rasters/index
   owslib/index
   mapscript/index
   pyproj/index


License
-------

This material is supposed to be distributed align with Creative Commons
Attribution-ShareAlike 4.0 International License.

.. figure:: http://training.gismentors.eu/geopython/_images/cc-by-sa.png%20%22CC-BY-SA%204.0%22
   :alt: CC-BY-SA

   CC-BY-SA

Source
~~~~~~

Workshop source can be found at:
https://github.com/GISMentors/geopython"
