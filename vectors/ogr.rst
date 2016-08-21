OGR
===

**OGR** is part of `GDAL <http://gdal.org/>`__ library. It is
traditional way how to interact with vector data.  Currently it
supports about `80 vector formats
<http://gdal.org/ogr_formats.html>`__.

OGR API overpasses differences between various vector formats, services,
database etc.:

-  **Driver** - driver for reading and writing the data to specified
   format
-  **Data Source** - whatever source (file, database, service, ...)
-  **Layer** - data layer within the source (file content, database
   table, ...)
-  **Feature** - vector feature
-  **Field, Geometry** - attributes and geomtry

.. aafig::
    :aspect: 70
    :scale: 90

                                               +-------+          +---------+
                                               |       |          |         |
                                          +--->+ Layer |     +--->+ Feature |
                                         /     |       |    /     |         |
                                        /      +-------+   /      +---------+
                                       /                  /
    +--------+         +------------+ /        +-------+ /        +---------+
    |        |         |            |/         |       |/         |         |
    | Driver +-------->+ DataSource +--------->+ Layer +--------->+ Feature |
    |        |         |            |\         |       |\         |         |
    +--------+         +------------+ \        +-------+ \        +---------+
                                       \                  \
                                        \      +-------+   \      +---------+
                                         \     |       |    \     |         |
                                          +--->+ ...   |     +--->+ ...     |
                                               |       |          |         |
                                               +-------+          +---------+
                                       

OGR-Python interface is abstract API on top of original classes and
methods of original C++ code. Also because of this, some approaches seem
complicated, compared native Python code, like e.g. :doc:`Fiona <fiona>`.

Documentation: http://www.gdal.org/ogr\_apitut.html

API: http://gdal.org/python/

Buffer
------

First we need to open *data source*

.. code:: python

    >>> from osgeo import ogr
    >>> ds = ogr.Open("data/protected_areas-etrs.shp")
    >>> print(ds)
    <osgeo.ogr.DataSource; proxy of <Swig Object of type 'OGRDataSourceShadow *' at 0x7febab282030> >

    >>> print(ds.GetLayerCount())
    1

Next we have to open *layer* (for files, there is usually no reason for
separate layer within data source, but for example for database data
source, a layer is reference to concrete table).

.. code:: python

    >>> l = ds.GetLayer(0)
    >>> print(l)
    <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7febac6e4090> >

    >>> print(l.GetFeatureCount())
    5626

Schema of the layer, definition of geometry type and attribution fields:

.. code:: python

    >>> l.GetGeomType()
    3

    >>> l.GetGeomType() == ogr.wkbPolygon
    True

    >>> l.schema
    [<osgeo.ogr.FieldDefn; proxy of <Swig Object of type 'OGRFieldDefnShadow *' at 0x7febac6d2db0> >,
    <osgeo.ogr.FieldDefn; proxy of <Swig Object of type 'OGRFieldDefnShadow *' at 0x7febab2822d0> >,
    <osgeo.ogr.FieldDefn; proxy of <Swig Object of type 'OGR
    ...
    ]

    >>> l.schema[4].name
    'NAZEV'

Print NAZEV attribute of all features

    >>> features_nr = l.GetFeatureCount()
    >>> for i in range(features_nr):
    ...    f = l.GetNextFeature()
    ...    print(f.GetField('NAZEV'))
    Kokořínsko
    Český ráj
    Kokořínsko
    Kokořínsko
    Český ráj
    Kokořínsko
    Broumovsko
    Broumovsko
    ...

Get vector feature bounding box (envelope):

.. code:: python

    >>> f = l.GetFeature(54)
    >>> geom = f.GetGeometryRef()
    >>> geom.GetEnvelope()
    (4685576.577618335, 4687748.187993193, 3067490.2318713292, 3069132.552762671)

Get geometry centroid

.. code:: python

    >>> c = geom.Centroid()
    >>> c.GetPoint()
    (4686578.099945216, 3068229.160325102, 0.0)

Create geometry buffer

.. code:: python

    >>> buff = c.Buffer(100)
    >>> geom.Intersects(buff)
    True

Complete example
----------------

In this example we will demonstrate work with vector data from
begining to the end: open data set, metadata, attribute change, saving
of new attribute back to the file. With :doc:`Fiona <fiona>`, this
would be about 3x simplier.  However, OGR accesses the data on much
lower level compared to Fiona, therefore bigger datasets can be
interfaced.

.. code:: python

    >>> from osgeo import osr
    
    >>> # Creating new file with GML driver
    >>> drv = ogr.GetDriverByName('GML')
    >>> ds = drv.CreateDataSource('data/out.gml')
    >>> srs = osr.SpatialReference()
    >>> srs.ImportFromEPSG(3035)
    >>> print(srs.ExportToProj4())
    +proj=laea +lat_0=52 +lon_0=10 +x_0=4321000 +y_0=3210000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs

    >>> layer = ds.CreateLayer('out.gml', srs, ogr.wkbLineString)
    
    >>> # create new attributes named and code
    >>> field_name = ogr.FieldDefn('name', ogr.OFTString)
    >>> field_name.SetWidth(24)
    >>> field_number = ogr.FieldDefn('code', ogr.OFTInteger)
    >>> layer.CreateField(field_name)
    >>> layer.CreateField(field_number)
    
    >>> # create new line geometry and read from WKT
    >>> line = ogr.CreateGeometryFromWkt('LINESTRING(%f %f, %f %f)' % (0, 0, 1, 1))
    
    >>> # create new feature, set attributes and geometry
    >>> feature = ogr.Feature(layer.GetLayerDefn())
    >>> feature.SetGeometry(line)
    >>> feature.SetField("name", 'the line')
    >>> feature.SetField("code", 42)
    
    >>> layer.CreateFeature(feature)
    
    >>> # final cleaning
    >>> feature.Destroy()
    >>> ds.Destroy()

And now we can check the result.

.. code:: python

    >>> ds = ogr.Open('data/out.gml')
    >>> layer = ds.GetLayer(0)
    >>> print(layer.GetFeatureCount())
    1

    >>> print(layer.GetFeature(0).GetField('name'))
    the line

    >>> f = layer.GetFeature(0)
    >>> print(f.GetGeometryRef().Length())
   1.4142135623730951

    >>> ds.Destroy()
