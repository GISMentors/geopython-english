Working with projections and Python
===================================

For projection definition and working, several approaches can be taken.

GDAL
----

In `GDAL <http://gdal.org>`__, projection definition can be found in the
osr package

.. code:: python

    >>> from osgeo import osr

    >>> # creating new spatial reference object
    >>> srs = osr.SpatialReference()
    >>> srs.ImportFromEPSG(3857)
    >>> print("Proj4 format:\n%s\n" % srs.ExportToProj4())
    Proj4 format:
    +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs

    >>> print("Well known text:\n%s\n" % srs.ExportToWkt())
    Well known text:
    PROJCS["WGS 84 / Pseudo-Mercator",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Mercator_1SP"],PARAMETER["central_meridian",0],PARAMETER["scale_factor",1],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["X",EAST],AXIS["Y",NORTH],EXTENSION["PROJ4","+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs"],AUTHORITY["EPSG","3857"]]



Perform coordinate transforamtion from once system to another

.. code:: python

    >>> # define source projection 
    >>> wgs = osr.SpatialReference()
    >>> wgs.ImportFromEPSG(4326)
    >>>
    >>> # define coordinate transformation
    >>> ct = osr.CoordinateTransformation(wgs, srs)
    >>>
    >>> # transform
    >>> print ct.TransformPoint(15, 51)
    (1669792.3618991044, 6621293.722740169, 0.0)


Fiona
-----

Fiona `has own
way <http://toblerity.org/fiona/manual.html#format-drivers-crs-bounds-and-schema>`__
of dealing with coordinate systems

Import from Proj4 string

.. code:: python

    >>> from fiona.crs import to_string, from_epsg, from_string

    >>> wgs = from_string("+datum=WGS84 +ellps=WGS84 +no_defs +proj=longlat")
    >>> print(wgs)
    {'no_defs': True, 'ellps': 'WGS84', 'datum': 'WGS84', 'proj': 'longlat'}


Import from EPSG

.. code:: python

    >>> from_epsg(3857)
    {'init': 'epsg:3857', 'no_defs': True}

Write projection to Proj4 string

.. code:: python

    >>> print(to_string(wgs))
    +datum=WGS84 +ellps=WGS84 +no_defs +proj=longlat


However, with Fiona, no transformation is possible - just for writing
and reading the dataset metadata

RasterIO
--------

Since Fiona and RasterIO are sister libraries, you
``from_string, from_epsg`` and ``to_string`` can be found too. But
RasterIO knows more

.. code:: python

    >>> from rasterio.crs import from_epsg, from_string, is_geographic_crs, is_projected_crs, is_same_crs, is_valid_crs

    >>> crs1 = from_epsg(4326)
    >>> print(crs1)
    {'init': 'epsg:4326', 'no_defs': True}

    >>> is_projected_crs(crs1)
    False

    >>> is_geographic_crs(crs1)

    True


Pyproj
------

The standard way of interacting with projections is to use
`Pyproj <https://github.com/jswhit/pyproj>`__

.. code:: python

    >>> import pyproj

    >>> # Define a projection with Proj4 notation - czech S-JTSK projection
    >>> krovak=pyproj.Proj("+proj=krovak +lat_0=49.5 +lon_0=24.83333333333333 +alpha=30.28813972222222 +k=0.9999 +x_0=0 +y_0=0 +ellps=bessel +pm=greenwich +units=m +no_defs +towgs84=570.8,85.7,462.8,4.998,1.587,5.261,3.56")

    >>> # Define some common projections using EPSG codes
    >>> wgs84=pyproj.Proj("+init=EPSG:4326")

    >>> mercator=pyproj.Proj("+init=EPSG:3857")

Do the projection

.. code:: python

    >>> krovak(12.806989, 49.452263)
    (-868280.2853028374, -1095867.5899331844)


Changing between two different systems

.. code:: python

    >>> pyproj.transform(krovak, mercator, -868280.2853028374, -1095867.5899331844)
    (1425576.6158538796, 6351822.307080091)


And back to WSG

.. code:: python

    >>> pyproj.transform(mercator, wgs84, 1425576.6158538796, 6351822.307080091)
    (12.806172627049238, 49.4515038313522)
